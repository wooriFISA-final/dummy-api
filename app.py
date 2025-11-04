from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from datetime import date, datetime

app = FastAPI(title="Manual Dummy Person API")

# ✅ 여기에 직접 더미 데이터 추가
DUMMY_DATA = {
    ("김현주", "2025-10"): {
        "name": "김현주",
        "date": "2025-10",
        "salary": 5000000,
        "house_contract": True,
        "tenant_status": True,
        "owner_name": "김현주",
        "other_house_owned": False,
        "first_house_purchase": False,
        "discount_category": "부양 없음"
    },

    ("이준혁", "2025-10"): {
        "name": "이준혁",
        "date": "2025-10",
        "salary": 0,
        "house_contract": False,
        "tenant_status": False,
        "owner_name": "None",
        "other_house_owned": False,
        "first_house_purchase": True,
        "discount_category": "부양 있음"
    }
}

class PersonResponse(BaseModel):
    name: str
    date: str
    salary: int
    house_contract: bool
    tenant_status: bool
    owner_name: str
    other_house_owned: bool
    first_house_purchase: bool
    discount_category: str

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
