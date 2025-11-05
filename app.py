from fastapi import FastAPI, HTTPException, Query
from datetime import date, datetime
from dummy import DUMMY_DATA
from schema import ConsumeInfo, DepositInfo, SavingInfo

app = FastAPI(title="Manual Dummy Person API")

@app.get("/consume", response_model=ConsumeInfo, response_model_by_alias=True)
def get_consume_info(name: str = Query(...), date: str = Query(...)):
    """
    소비 분석을 위한 더미 데이터를 가져오는 API
    """
    key = (name, date)
    if key not in DUMMY_DATA:
        raise HTTPException(status_code=404, detail="No dummy data for given name and date")
    
    all_data = DUMMY_DATA[key]
    consume_data = {}
    total_spend = 0
    for k, v in all_data.items():
        if k.startswith("CAT1_") or k.startswith("CAT2_"):
            consume_data[k] = v//10000
            total_spend += consume_data[k]
        if k=="age" or k=="name" or k=="region" or k=="gender":
            consume_data[k] = v
    
    consume_data['total_spend']=total_spend

    return consume_data

@app.get("/deposits", response_model=DepositInfo)
def get_deposits_info(name: str = Query(...), date: str = Query(...)):
    """
    예금 추천을 위한 더미 데이터를 가져오는 API
    """
    key = (name, date)
    if key not in DUMMY_DATA:
        raise HTTPException(status_code=404, detail="No dummy data for given name and date")
    
    all_data = DUMMY_DATA[key]
    deposit_data = {}
    for k, v in all_data.items():
        if k=="internet_banking" or k=="sms_agree" or k=="has_woori_account" or k=="has_saving_product" or k=="open_banking":
            deposit_data[k]=v

    return deposit_data


@app.get("/savings", response_model=SavingInfo)
def get_deposits_info(name: str = Query(...), date: str = Query(...)):
    """
    적금 추천을 위한 더미 데이터를 가져오는 API
    """
    key = (name, date)
    if key not in DUMMY_DATA:
        raise HTTPException(status_code=404, detail="No dummy data for given name and date")
    
    all_data = DUMMY_DATA[key]
    cols = set(SavingInfo.model_fields.keys())
    saving_data = {}
    for k, v in all_data.items():
        if k in cols:
            saving_data[k]=v

    return saving_data


@app.get("/health")
def health():
    return {"status": "ok"}
