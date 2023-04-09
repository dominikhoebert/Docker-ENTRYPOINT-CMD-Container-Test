# 1. Base image
FROM python:3.10-slim
WORKDIR /app

# 2. Copy files
COPY requirements.txt .
COPY *.py ./

# 3. Install dependencies
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
CMD ["World"]