from pydantic import BaseModel, Field, ConfigDict


class consumeInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    total_spend: int
    age: int
    region: str
    gender: str
    

    CAT1_transportation: int = Field(..., alias="CAT1_교통")
    CAT1_shopping: int = Field(..., alias="CAT1_쇼핑")
    CAT1_food: int = Field(..., alias="CAT1_식품")
    CAT1_education_culture: int = Field(..., alias="CAT1_교육/문화")
    CAT1_living: int = Field(..., alias="CAT1_생활/주거")
    CAT1_leisure_travel: int = Field(..., alias="CAT1_레저/여행")
    CAT1_self_dev: int = Field(..., alias="CAT1_자기계발")
    CAT1_others: int = Field(..., alias="CAT1_기타 지출")

    CAT2_public_transport: int = Field(..., alias="CAT2_대중교통")
    CAT2_car_fuel: int = Field(..., alias="CAT2_자가용/연료")
    CAT2_taxi: int = Field(..., alias="CAT2_택시/대리")
    CAT2_air_train: int = Field(..., alias="CAT2_항공/기차")

    CAT2_clothing: int = Field(..., alias="CAT2_의류")
    CAT2_accessory_beauty: int = Field(..., alias="CAT2_잡화/뷰티")
    CAT2_luxury: int = Field(..., alias="CAT2_명품/쥬얼리")
    CAT2_electronics: int = Field(..., alias="CAT2_전자제품")

    CAT2_dining_delivery: int = Field(..., alias="CAT2_외식/배달")
    CAT2_home_food: int = Field(..., alias="CAT2_가정식/식재료")
    CAT2_pub_entertainment: int = Field(..., alias="CAT2_주점/유흥")
    CAT2_coffee_beverage: int = Field(..., alias="CAT2_커피/음료")

    CAT2_academy: int = Field(..., alias="CAT2_사교육/학원")
    CAT2_books_music: int = Field(..., alias="CAT2_도서/음반")
    CAT2_culture_hobby: int = Field(..., alias="CAT2_문화생활/취미")
    CAT2_online_course: int = Field(..., alias="CAT2_온라인강의")

    CAT2_utility_telecom: int = Field(..., alias="CAT2_공과금/통신")
    CAT2_hospital_pharmacy: int = Field(..., alias="CAT2_병원/약국")
    CAT2_interior_furniture: int = Field(..., alias="CAT2_인테리어/가구")
    CAT2_insurance_finance: int = Field(..., alias="CAT2_보험/금융")

    CAT2_domestic_travel: int = Field(..., alias="CAT2_국내여행/숙박")
    CAT2_overseas_travel: int = Field(..., alias="CAT2_해외여행/항공")
    CAT2_leisure_activity: int = Field(..., alias="CAT2_레포츠/취미")
    CAT2_other_leisure: int = Field(..., alias="CAT2_기타 여가")

    CAT2_certificate_language: int = Field(..., alias="CAT2_자격증/어학")
    CAT2_fitness: int = Field(..., alias="CAT2_운동/피트니스")
    CAT2_online_subscription: int = Field(..., alias="CAT2_온라인 구독")
    CAT2_tools_material: int = Field(..., alias="CAT2_도구/재료 구매")

    CAT2_cash_service: int = Field(..., alias="CAT2_현금서비스")
    CAT2_donation_event: int = Field(..., alias="CAT2_경조사/기부")
    CAT2_overseas_shopping: int = Field(..., alias="CAT2_해외 직구")
    CAT2_finance_fee: int = Field(..., alias="CAT2_금융 수수료")
