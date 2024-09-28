FROM python:3.9-slim

WORKDIR /app

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
