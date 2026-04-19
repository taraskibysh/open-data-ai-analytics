FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["jupyter", "nbconvert", "--execute", "--to", "notebook", "--inplace", "--ExecutePreprocessor.timeout=300", "data_quality_analysis.ipynb"]
