from pydantic import BaseModel, Field, ConfigDict


class ConsumeInfo(BaseModel):
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


class DepositInfo(BaseModel):
    internet_banking: bool                # 인터넷 뱅킹 사용여부
    sms_agree: bool                       # sms 수신동의 여부
    has_woori_account: bool               # 지난 1년간 우리은행 계좌 보유 여부
    has_saving_product: bool              # 지난 1년간 예적금 상품 보유 여부
    open_banking: bool                    # open 뱅킹 서비스 가입여부


class SavingInfo(BaseModel):
    is_corporate_employee: bool               # 단체 기업 임직원 여부
    has_pre_agreement: bool                   # 사전 협의 여부
    has_approval_number: bool                 # 승인 번호 소지 여부
    is_basic_living_recipient: bool           # 기초 생활 수급자 여부
    is_low_income_class: bool                 # 차상위 계층 여부
    is_orphan: bool                           # 소년/소녀 가장 여부
    is_marriage_immigrant: bool               # 결혼 이민자 여부
    is_north_defector: bool                   # 북한 이탈자 여부
    is_earned_income_beneficiary: bool        # 근로 장려금 수급자 여부
    is_smile_finance_recommended: bool        # 서민 금융진흥원 추천여부
    has_military_saving_eligibility: bool     # 장병내일준비적금 가입자격 여부
    is_below_250pct_median_income: bool       # 중위 소득 250% 이하여부
    has_business_registration: bool           # 개인 사업자 등록증 소지 여부
    has_npay_account: bool                    # n-pay 우리통장 가입 여부
