# ----------------------------
# 1. 필요한 라이브러리 불러오기
# ----------------------------
import streamlit as st   # 웹앱 제작용 라이브러리
import random            # 리스트에서 랜덤 선택용

# ----------------------------
# 2. 확장된 한국어 감정 분석 함수 정의
# ----------------------------
def extended_sentiment_analysis(text):
    """
    사용자의 문장을 분석하여 세부 감정을 반환하는 함수
    - 긍정: 행복, 즐거움, 설렘, 만족, 신남
    - 부정: 슬픔, 우울, 외로움, 짜증, 피곤, 긴장
    - 중립: 보통, 평온, 무난
    """
    text = text.lower()  # 입력 문장을 소문자로 변환하여 처리

    # 긍정 키워드 목록
    positive_keywords = ["좋아", "행복", "즐거", "신나", "기쁨", "만족", "설렘", "행복해", "신난", "좋은"]
    # 부정 키워드 목록
    negative_keywords = ["슬퍼", "우울", "짜증", "화나", "싫어", "힘들", "피곤", "외로움", "긴장", "불안"]
    # 중립 키워드 목록
    neutral_keywords = ["보통", "무난", "평온", "그냥"]

    # 키워드 매칭하여 감정 반환
    if any(word in text for word in positive_keywords):
        return "긍정"
    elif any(word in text for word in negative_keywords):
        return "부정"
    else:
        return "중립"

# ----------------------------
# 3. 감정별 음식 추천 데이터 (10개 이상)
# ----------------------------
mood_foods = {
    "긍정": [
        # 긍정 감정에 맞는 음식 10개, 이미지 URL 포함
        {"음식": "파스타", "이미지": "https://cdn.pixabay.com/photo/2017/12/09/08/18/spaghetti-3001311_1280.jpg"},
        {"음식": "초밥", "이미지": "https://cdn.pixabay.com/photo/2017/05/07/08/56/sushi-2297689_1280.jpg"},
        {"음식": "딸기 파르페", "이미지": "https://cdn.pixabay.com/photo/2016/11/21/15/46/strawberry-1846080_1280.jpg"},
        {"음식": "샐러드", "이미지": "https://cdn.pixabay.com/photo/2016/03/05/19/02/salad-1238249_1280.jpg"},
        {"음식": "치킨", "이미지": "https://cdn.pixabay.com/photo/2017/12/09/08/18/chicken-3001313_1280.jpg"},
        {"음식": "팬케이크", "이미지": "https://cdn.pixabay.com/photo/2017/05/07/08/56/pancake-2297687_1280.jpg"},
        {"음식": "아이스크림", "이미지": "https://cdn.pixabay.com/photo/2014/12/16/22/25/ice-cream-570802_1280.jpg"},
        {"음식": "스무디", "이미지": "https://cdn.pixabay.com/photo/2017/03/30/12/30/smoothie-2189736_1280.jpg"},
        {"음식": "와플", "이미지": "https://cdn.pixabay.com/photo/2018/03/16/20/28/waffles-3231974_1280.jpg"},
        {"음식": "마카롱", "이미지": "https://cdn.pixabay.com/photo/2018/06/21/21/28/macarons-3482312_1280.jpg"}
    ],
    "중립": [
        # 중립 감정에 맞는 음식 10개
        {"음식": "치즈 피자", "이미지": "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_1280.jpg"},
        {"음식": "샌드위치", "이미지": "https://cdn.pixabay.com/photo/2014/10/23/18/05/burger-500054_1280.jpg"},
        {"음식": "타코", "이미지": "https://cdn.pixabay.com/photo/2017/01/22/19/20/taco-2003468_1280.jpg"},
        {"음식": "볶음밥", "이미지": "https://cdn.pixabay.com/photo/2015/04/08/13/13/fried-rice-712665_1280.jpg"},
        {"음식": "계란말이", "이미지": "https://cdn.pixabay.com/photo/2018/05/07/12/24/egg-3387256_1280.jpg"},
        {"음식": "우동", "이미지": "https://cdn.pixabay.com/photo/2017/07/16/11/53/ramen-2509888_1280.jpg"},
        {"음식": "김밥", "이미지": "https://cdn.pixabay.com/photo/2016/06/17/06/53/kimbap-1462173_1280.jpg"},
        {"음식": "샐러리 스틱", "이미지": "https://cdn.pixabay.com/photo/2016/03/05/19/02/salad-1238249_1280.jpg"},
        {"음식": "치즈 토스트", "이미지": "https://cdn.pixabay.com/photo/2017/02/14/20/40/toast-2063034_1280.jpg"},
        {"음식": "컵케이크", "이미지": "https://cdn.pixabay.com/photo/2016/03/05/19/02/cupcake-1238248_1280.jpg"}
    ],
    "부정": [
        # 부정 감정에 맞는 음식 10개
        {"음식": "초콜릿 케이크", "이미지": "https://cdn.pixabay.com/photo/2017/01/26/02/06/chocolate-cake-2010993_1280.jpg"},
        {"음식": "라멘", "이미지": "https://cdn.pixabay.com/photo/2017/07/16/11/53/ramen-2509888_1280.jpg"},
        {"음식": "삼계탕", "이미지": "https://cdn.pixabay.com/photo/2020/06/22/08/56/chicken-soup-5327328_1280.jpg"},
        {"음식": "죽", "이미지": "https://cdn.pixabay.com/photo/2018/03/11/19/37/congee-3211216_1280.jpg"},
        {"음식": "떡볶이", "이미지": "https://cdn.pixabay.com/photo/2017/12/09/08/18/tteokbokki-3001314_1280.jpg"},
        {"음식": "카레", "이미지": "https://cdn.pixabay.com/photo/2016/03/05/19/02/curry-1238252_1280.jpg"},
        {"음식": "스프", "이미지": "https://cdn.pixabay.com/photo/2017/05/07/08/56/soup-2297684_1280.jpg"},
        {"음식": "김치찌개", "이미지": "https://cdn.pixabay.com/photo/2015/12/05/23/23/kimchi-1079815_1280.jpg"},
        {"음식": "라자냐", "이미지": "https://cdn.pixabay.com/photo/2017/01/13/14/29/lasagna-1975074_1280.jpg"},
        {"음식": "비빔밥", "이미지": "https://cdn.pixabay.com/photo/2017/06/03/11/52/korean-2378728_1280.jpg"}
    ]
}

# ----------------------------
# 4. Streamlit 화면 구성
# ----------------------------
# 페이지 설정
st.set_page_config(page_title="고급 랜덤 음식 추천", page_icon="🍽️", layout="centered")

# 앱 타이틀과 설명
st.title("🍽️ 기분 → 감정 분석 → 랜덤 음식 추천 (고급)")
st.write("👉 다양한 기분 키워드로 감정을 분석하고, 어울리는 음식을 랜덤으로 추천합니다!")

# 사용자로부터 기분 입력 받기
user_input = st.text_input("지금 기분을 자유롭게 입력해주세요 (예: '오늘 너무 우울해요')")

# 사용자가 입력하면 실행
if user_input:
    mood = extended_sentiment_analysis(user_input)       # 1) 감정 분석
    food_info = random.choice(mood_foods[mood])         # 2) 해당 감정 음식 중 랜덤 선택

    # 분석 결과 출력
    st.success(f"**분석 결과:** {mood}")

    # 음식 카드 형태로 이름과 이미지 출력
    st.markdown(f"""
    <div style="background-color:#f8f9fa; padding:20px; border-radius:15px; 
                box-shadow:2px 2px 10px rgba(0,0,0,0.1); text-align:center;">
        <h2>{food_info['음식']}</h2>
        <img src="{food_info['이미지']}" width="300" style="border-radius:10px; margin:10px 0;">
        <p><b>추천 이유:</b> {mood} 감정에 맞는 음식</p>
    </div>
    """, unsafe_allow_html=True)
