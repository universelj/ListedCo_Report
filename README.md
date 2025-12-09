# 上市公司报告下载工具

一个基于 Flask 的 Web 应用，用于批量下载上市公司年报、半年报、季报等公开披露文件。

## 功能特点

- **批量下载**：支持批量下载多家公司的报告
- **多报告类型**：支持年报、半年报、一季报、三季报
- **多板块支持**：覆盖主板（沪深）、创业板、科创板、北交所
- **股票搜索**：根据股票代码或名称快速查找
- **打包下载**：自动打包为 ZIP 文件下载
- **数据来源**：巨潮资讯网 (cninfo.com.cn)

## 技术栈

- **后端**：Python + Flask
- **数据获取**：Requests
- **数据处理**：Pandas
- **前端**：Jinja2 + Bootstrap

## 快速启动

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动应用

```bash
python app.py
```

### 3. 访问系统

浏览器打开：http://localhost:5000

## 使用说明

1. **选择板块**：选择需要下载的股票板块
2. **输入股票**：输入股票代码或名称（支持批量）
3. **选择报告类型**：选择年报、半年报等
4. **选择年份**：选择报告年份
5. **开始下载**：点击下载，系统自动获取并打包

## 项目结构

```
report/
├── app.py                  # Flask 应用主文件
├── listedreport.py         # 报告下载核心逻辑
├── templates/              # HTML 模板
│   └── index.html         # 主页面
├── uploads/                # 临时文件目录
├── requirements.txt        # Python 依赖
└── README.md
```

## 数据来源

- 巨潮资讯网：http://www.cninfo.com.cn
- 数据仅供学习研究使用

## 系统要求

- Python 3.8+
- Flask
- Requests
- Pandas

## 注意事项

- 请遵守数据来源网站的使用条款
- 建议适度使用，避免频繁请求
- 仅供学习研究使用

## 许可证

MIT License
