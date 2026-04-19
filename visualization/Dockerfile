FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV MPLBACKEND=Agg
CMD ["jupyter", "nbconvert", "--execute", "--to", "notebook", "--inplace", "--ExecutePreprocessor.timeout=300", "visualization.ipynb"]
