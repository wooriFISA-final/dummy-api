### 배경
"우리 카드에서 사용자의 데이터를 편리하게 조회할 수 있는 API를 개발했다." 라는 배경에 맞게 고객의 데이터를 조회할 수 있는 가상의 API

### 실행
```bash
# 빌드
docker build -t dummy-api .

# 실행
docker run -d -p 700:7000 --name dummy-api dummy-api
```

### 요청
```bash
# 베이스 url
http://localhost:700

# 고객 정보 요청 url
http://localhost:700/person?name={name}&date={YYYY-MM}

# 고객 정보 요청 url 예시
http://localhost:700/person?name=이준혁&date=2025-10
```