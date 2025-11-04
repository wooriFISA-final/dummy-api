### 배경
"우리 카드에서 사용자의 데이터를 편리하게 조회할 수 있는 API를 개발했다." 라는 배경에 맞게 고객의 데이터를 조회할 수 있는 가상의 API

### 실행
```bash
# 빌드
docker build -t dummy-api .

# 실행
docker run -d -p 7000:7000 --name dummy-api dummy-api
```

### 요청
```bash
https://localhost:7000
```
위의 베이스 url로 요청