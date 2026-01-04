FROM python:3.11-slim

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# 复制项目文件
COPY . .

# 创建上传目录
RUN mkdir -p uploads

# 暴露端口
EXPOSE 5003

# 使用 gunicorn 运行（生产环境推荐）
CMD ["gunicorn", "--bind", "0.0.0.0:5003", "--workers", "2", "app:app"]
