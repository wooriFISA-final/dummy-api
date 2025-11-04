# 1️⃣ 베이스 이미지
FROM python:3.11-slim

# 2️⃣ 작업 디렉터리 설정
WORKDIR /app

# 3️⃣ FastAPI 및 Uvicorn 설치
RUN pip install --no-cache-dir fastapi uvicorn

# 4️⃣ 코드 복사
COPY app.py .

# 5️⃣ 컨테이너 실행 명령
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7000"]
