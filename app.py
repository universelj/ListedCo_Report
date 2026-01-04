import os
import re
import requests
import pandas as pd
from flask import Flask, render_template, request, jsonify, send_file
from datetime import datetime
from werkzeug.utils import secure_filename
import zipfile
import io

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')

# 确保上传目录存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 获取股票列表（与原版一致）
def get_stock_list():
    try:
        orgid_url = 'http://www.cninfo.com.cn/new/data/szse_stock.json'
        orgid_resp = requests.get(orgid_url, timeout=10)
        orgid_resp_stock = orgid_resp.json()['stockList']
        return pd.DataFrame(orgid_resp_stock)
    except Exception as e:
        print(f"获取股票列表失败: {e}")
        return pd.DataFrame()

df_orgid = get_stock_list()

# 报告类型映射
REPORT_TYPE_MAP = {
    "年报": 'category_ndbg_szsh',
    "半年报": 'category_bndbg_szsh',
    "一季度报": 'category_yjdbg_szsh',
    "三季度报": 'category_sjdbg_szsh',
    "其他": '',
}

# 板块映射
PLATE_MAP = {
    '主板[沪]': 'shmb',
    '主板[深]': 'szmb',
    '创业板': 'szcy',
    '科创板': 'shkcp',
    '北交所': 'bj'
}


def cnifo_data_convert(fram_dict):
    """
    转换请求参数为cninfo API格式
    """
    global df_orgid
    df_orgid_t = df_orgid
    
    dict_for_c = fram_dict.copy()
    
    # 处理搜索关键词
    search = dict_for_c.get('searchkey', [''])
    if search and search != ['']:
        search_j = ';'.join(search)
    else:
        search_j = ''
    dict_for_c['searchkey'] = search_j
    
    # 处理股票代码
    stock = dict_for_c.get('stock', [''])
    if stock and stock != ['']:
        new_dict_value_list = []
        for s in stock:
            # 兼容：如果传入的是str，先转列表
            if isinstance(s, str):
                s = s.strip()
            
            if s in list(df_orgid_t['code']):
                gssz_stock = list(df_orgid_t['orgId'][df_orgid_t['code'] == s])[0]
                new_v = f'{s},{gssz_stock}'
                new_dict_value_list.append(new_v)
        dict_for_c['stock'] = ';'.join(new_dict_value_list)
    else:
        dict_for_c['stock'] = ''
    
    # 处理板块
    plate = dict_for_c.get('plate', [''])
    plate_list = []
    if plate and plate != ['']:
        for p in plate:
            if p in PLATE_MAP:
                p_c = PLATE_MAP[p]
                plate_list.append(p_c)
        plate_c = ';'.join(plate_list)
        dict_for_c['plate'] = plate_c
    else:
        dict_for_c['plate'] = ''
    
    # 处理报告类型
    category = dict_for_c.get('category', [''])
    category_list = []
    if category and category != ['']:
        for cat in category:
            if cat in REPORT_TYPE_MAP:
                cat_c = REPORT_TYPE_MAP[cat]
                category_list.append(cat_c)
        category_c = ';'.join(category_list)
        dict_for_c['category'] = category_c
    else:
        dict_for_c['category'] = ''
    
    # 构建最终请求数据
    data = {
        'pageNum': 1,
        'pageSize': 30,
        'column': 'szse',
        'tabName': 'fulltext',
        'plate': dict_for_c['plate'],
        'stock': dict_for_c['stock'],
        'searchkey': dict_for_c['searchkey'],
        'secid': '',
        'category': dict_for_c['category'],
        'trade': '',
        'seDate': dict_for_c.get('seDate', ''),
        'sortName': '',
        'sortType': '',
        'isHLtitle': 'true'
    }
    return data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/check_stock', methods=['POST'])
def check_stock():
    """
    验证股票代码
    """
    global df_orgid
    data = request.json
    codes = data.get('codes', '')
    
    if isinstance(codes, str):
        codes = codes.replace(' ', '').replace('，', ',')
        codes = [c.strip() for c in codes.split(',') if c.strip()]
    
    valid_codes = []
    invalid_codes = []
    
    for code in codes:
        if code in list(df_orgid['code']):
            valid_codes.append(code)
        else:
            invalid_codes.append(code)
    
    return jsonify({
        'valid': valid_codes,
        'invalid': invalid_codes,
        'success': len(invalid_codes) == 0
    })


@app.route('/api/upload_excel', methods=['POST'])
def upload_excel():
    """
    上传Excel文件读取股票代码
    """
    global df_orgid
    
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': '未选择文件'})
    
    file = request.files['file']
    column_name = request.form.get('column', '股票代码')
    
    if file.filename == '':
        return jsonify({'success': False, 'error': '未选择文件'})
    
    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # 先读取Excel看看有哪些列
        df_stock = pd.read_excel(filepath)
        
        # 智能检测列名
        possible_columns = ['股票代码', '代码', 'code', 'Code', 'CODE', '证券代码']
        actual_column = None
        
        for col in possible_columns:
            if col in df_stock.columns:
                actual_column = col
                break
        
        # 如果指定的列名存在，优先使用
        if column_name in df_stock.columns:
            actual_column = column_name
        
        # 都找不到就用第一列
        if actual_column is None:
            actual_column = df_stock.columns[0]
        
        # 重新读取，确保股票代码是字符串
        df_stock = pd.read_excel(filepath, converters={actual_column: str})
        stock_list = list(df_stock[actual_column])
        
        valid_codes = []
        invalid_codes = []
        
        for s in stock_list:
            s = str(s).strip()
            if s in list(df_orgid['code']):
                valid_codes.append(s)
            else:
                invalid_codes.append(s)
        
        os.remove(filepath)
        
        if invalid_codes:
            return jsonify({
                'success': False,
                'valid': valid_codes,
                'invalid': invalid_codes,
                'error': f'以下代码无效: {", ".join(invalid_codes[:5])}{"..." if len(invalid_codes) > 5 else ""}'
            })
        
        return jsonify({
            'success': True,
            'valid': valid_codes,
            'count': len(valid_codes)
        })
        
    except KeyError:
        return jsonify({'success': False, 'error': f'未找到列名: {column_name}'})
    except Exception as e:
        return jsonify({'success': False, 'error': f'文件读取失败: {str(e)}'})

# --- UPDATED ROUTES FOR CLAUDE STYLE FRONTEND ---

@app.route('/api/search_reports', methods=['POST'])
def search_reports():
    """
    搜索公告
    """
    data = request.json
    mode = data.get('mode', 'single')
    
    stocks = data.get('stocks', [])
    if isinstance(stocks, str):
        stocks = [s.strip() for s in stocks.replace('，', ',').split(',') if s.strip()]
    
    keywords = data.get('keywords', '')
    if keywords:
        keywords = keywords.replace('   ', ' ').replace('  ', ' ')
        keyword_list = [k.strip() for k in keywords.split(' ') if k.strip()]
    else:
        keyword_list = []
    
    categories = data.get('categories', [])
    if not categories:
        if mode == 'periodic':
            categories = ['年报', '半年报', '一季度报', '三季度报']
        else:
            categories = ['']
    
    if mode == 'periodic':
        begin_year = data.get('beginYear', 2024)
        end_year = data.get('endYear', 2024)
        se_date = f'{begin_year}-01-01~{int(end_year)+1}-12-31'
    else:
        start_date = data.get('startDate', '2024-01-01')
        end_date = data.get('endDate', '2024-12-31')
        se_date = f'{start_date}~{end_date}'
    
    url = "http://www.cninfo.com.cn/new/hisAnnouncement/query"
    all_announcements = []
    seen_urls = set()
    
    try:
        search_keywords = keyword_list if keyword_list else ['']
        
        for kw in search_keywords:
            params = {
                'plate': data.get('plates', ['']),
                'stock': stocks if stocks else [''],
                'searchkey': [kw] if kw else [''],
                'category': categories,
                'seDate': se_date,
            }
            api_data = cnifo_data_convert(params)
            
            resp = requests.post(url, data=api_data, timeout=30)
            result = resp.json()
            
            total = result.get('totalAnnouncement', 0)
            announcements = result.get('announcements', []) or []
            
            if not announcements:
                continue
            
            total_pages = (total + 29) // 30
            if total_pages > 1:
                # 限制页数，防止请求过多
                for page in range(2, min(total_pages + 1, 6)):
                    api_data['pageNum'] = page
                    resp = requests.post(url, data=api_data, timeout=30)
                    page_result = resp.json()
                    page_announcements = page_result.get('announcements', []) or []
                    announcements.extend(page_announcements)
            
            for ann in announcements:
                ann_url = ann.get('adjunctUrl', '')
                if ann_url and ann_url not in seen_urls:
                    seen_urls.add(ann_url)
                    all_announcements.append(ann)
        
        announcements = all_announcements
        
        if mode == 'periodic':
            begin_year = int(data.get('beginYear', 2024))
            end_year = int(data.get('endYear', 2024))
            filtered = []
            for ann in announcements:
                ann_title = ann.get('announcementTitle', '')
                for year in range(begin_year, end_year + 1):
                    year_str = str(year)
                    if year_str in ann_title and '摘要' not in ann_title and '英文' not in ann_title and '取消' not in ann_title:
                        filtered.append(ann)
                        break
            announcements = filtered
        
        cleaned = []
        for ann in announcements:
            title = ann.get('announcementTitle', '')
            title = re.sub(r'<[^>]+>', '', title)
            
            cleaned.append({
                'secCode': ann.get('secCode', ''),
                'secName': ann.get('secName', ''),
                'announcementTitle': title, # Updated Key
                'adjunctUrl': ann.get('adjunctUrl', ''), # Updated Key
                'publishDate': ann.get('announcementTime', '') # Updated Key (timestamp)
            })
        
        # Sort by date desc
        cleaned.sort(key=lambda x: x['publishDate'], reverse=True)
        
        return jsonify({
            'success': True,
            'data': cleaned, # Updated Key: data
            'total': len(cleaned)
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        })


@app.route('/api/download_reports', methods=['POST'])
def download_reports():
    """
    下载选中的公告
    """
    data = request.json
    reports = data.get('reports', [])
    
    if not reports:
        return jsonify({'success': False, 'error': '没有选择公告'})
    
    memory_file = io.BytesIO()
    illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for ann in reports:
            try:
                ann_url = ann.get('adjunctUrl', '')
                if not ann_url: continue
                
                ann_allurl_for_download = f"http://static.cninfo.com.cn/{ann_url}"
                resp = requests.get(ann_allurl_for_download, timeout=60)
                
                ann_stock = ann.get('secCode', '')
                ann_stock_name = ann.get('secName', '')
                ann_title = ann.get('announcementTitle', '')
                
                ann_date = ''
                if ann_url:
                    url_parts = ann_url.split('/')
                    if len(url_parts) > 1:
                        ann_date = url_parts[1]
                
                ann_title = re.sub(r'<[^>]+>', '', ann_title)
                for char in illegal_chars:
                    ann_title = ann_title.replace(char, '')
                    ann_stock_name = ann_stock_name.replace(char, '')
                
                file_name = f"【{ann_date}】{ann_stock_name}_{ann_stock}_{ann_title}.pdf"
                zf.writestr(file_name, resp.content)
                
            except Exception as e:
                print(f"下载失败: {ann.get('announcementTitle', '')}, 错误: {e}")
    
    memory_file.seek(0)
    
    return send_file(
        memory_file,
        mimetype='application/zip',
        as_attachment=True,
        download_name=f'reports_{datetime.now().strftime("%Y%m%d_%H%M%S")}.zip'
    )


@app.route('/api/export_excel', methods=['POST'])
def export_excel():
    """
    导出搜索结果为Excel
    """
    data = request.json
    reports = data.get('reports', [])
    
    if not reports:
        return jsonify({'success': False, 'error': '没有数据可导出'})
    
    try:
        rows = []
        for ann in reports:
            ann_url = ann.get('adjunctUrl', '') 
            url_parts = ann_url.split('/') if ann_url else []
            ann_date = url_parts[1] if len(url_parts) > 1 else ''
            
            rows.append({
                '股票代码': ann.get('secCode', ''),
                '股票名称': ann.get('secName', ''),
                '公告日期': ann_date,
                '公告标题': ann.get('announcementTitle', ''),
                '下载链接': f"http://static.cninfo.com.cn/{ann_url}" if ann_url else ''
            })
        
        df = pd.DataFrame(rows)
        
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='公告列表')
        output.seek(0)
        
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=f'公告列表_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
        )
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
