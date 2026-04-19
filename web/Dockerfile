FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8866
CMD ["voila", "web.ipynb", "--no-browser", "--port=8866", "--Voila.ip=0.0.0.0"]
