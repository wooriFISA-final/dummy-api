from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from datetime import date, datetime

app = FastAPI(title="Manual Dummy Person API")

# ✅ 여기에 직접 더미 데이터 추가
DUMMY_DATA = {
    ("김현우", "2025-10-20"): {
        "name": "김현우",
        "age": 29,
        "email": "hyunwoo@example.com",
        "job": "AI 연구원",
        "bio": "데이터 기반 문제 해결을 좋아합니다.",
    },
}

class PersonResponse(BaseModel):
    name: str
    age: int
    email: str
    job: str
    bio: str

@app.get("/person", response_model=PersonResponse)
def get_person(name: str = Query(...), date: str = Query(...)):
    key = (name, date)
    if key not in DUMMY_DATA:
        raise HTTPException(status_code=404, detail="No dummy data for given name and date")
    return DUMMY_DATA[key]

@app.post("/person")
def add_person(name: str, date: str, data: dict):
    """새 더미 데이터를 추가할 수 있는 임시 엔드포인트"""
    DUMMY_DATA[(name, date)] = data
    return {"message": f"Added dummy data for {name} on {date}"}

@app.get("/health")
def health():
    return {"status": "ok"}
