from fastapi import FastAPI, HTTPException, Query
from datetime import date, datetime
from dummy import DUMMY_DATA
from schema import consumeInfo

app = FastAPI(title="Manual Dummy Person API")

@app.get("/consume", response_model=consumeInfo, response_model_by_alias=True)
def get_consume_info(name: str = Query(...), date: str = Query(...)):
    key = (name, date)
    if key not in DUMMY_DATA:
        raise HTTPException(status_code=404, detail="No dummy data for given name and date")
    
    all_data = DUMMY_DATA[key]
    consume_data = {}
    for k, v in all_data.items():
        if k.startswith("CAT1_") or k.startswith("CAT2_") or k=="total_spend":
            consume_data[k] = v//10000
        if k=="age" or k=="name" or k=="region" or k=="gender":
            consume_data[k] = v

    return consume_data

@app.post("/person")
def add_person(name: str, date: str, data: dict):
    """새 더미 데이터를 추가할 수 있는 임시 엔드포인트"""
    DUMMY_DATA[(name, date)] = data
    return {"message": f"Added dummy data for {name} on {date}"}

@app.get("/health")
def health():
    return {"status": "ok"}
