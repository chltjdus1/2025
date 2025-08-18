# ----------------------------
# 필요한 라이브러리 불러오기
# ----------------------------
import streamlit as st   # 웹앱 제작용
import random            # 랜덤 선택용

# ----------------------------
# 간단한 한국어 감정 분석 함수 (키워드 기반)
# ----------------------------
def simple_sentiment_analysis(text):
    """
    사용자가 입력한 문장을 분석해서 감정을 판별하는 함수
    - 긍정 키워드 포함 → '긍정'
    - 부정 키워드 포함 → '부정'
    - 그 외 → '중립'
    """
    text = text.lower()  # 소문자로 변환

    # 긍정 단어 목록
    positive_keywords = ["좋아", "행복", "즐거", "신나", "기쁨", "만족", "설렘"]
    # 부정 단어 목록
    negative_keywords = ["슬퍼", "우울", "짜증", "화나", "싫어", "힘들", "피곤"]

    if any(word in text for word in positive_keywords):
        return "긍정 (기분 좋아요)"
    elif any(word in text for word in negative_keywords):
        return "부정 (기분 안 좋아요)"
    else:
        return "중립 (보통)"

# ----------------------------
# 기분별 음식 추천 데이터 (7개씩)
# ----------------------------
mood_foods = {
    "긍정 (기분 좋아요)": [
        {"음식": "파스타", "이미지": "https://cdn.pixabay.com/photo/2017/12/09/08/18/spaghetti-3001311_1280.jpg",
         "레시피": ["스파게티 면 삶기", "올리브유에 마늘과 양파 볶기", "토마토소스 넣기", "면과 섞기", "치즈 뿌리기"]},
        {"음식": "초밥", "이미지": "https://cdn.pixabay.com/photo/2017/05/07/08/56/sushi-2297689_1280.jpg",
         "레시피": ["초밥밥 만들기", "생선 얇게 썰기", "밥 위에 생선 얹기", "와사비, 간장 곁들이기"]},
        {"음식": "딸기 파르페", "이미지": "https://cdn.pixabay.com/photo/2016/11/21/15/46/strawberry-1846080_1280.jpg",
         "레시피": ["컵에 시리얼 깔기", "요거트 넣기", "딸기 올리기", "생크림 올리기", "민트 장식"]},
        {"음식": "샐러드", "이미지": "https://cdn.pixabay.com/photo/2016/03/05/19/02/salad-1238249_1280.jpg",
         "레시피": ["채소 씻기", "채소 썰기", "드레싱 만들기", "섞기"]},
        {"음식": "치킨", "이미지": "https://cdn.pixabay.com/photo/2017/12/09/08/18/chicken-3001313_1280.jpg",
         "레시피": ["닭 손질", "양념 재우기", "오븐 또는 프라이팬에 굽기"]},
        {"음식": "팬케이크", "이미지": "https://cdn.pixabay.com/photo/2017/05/07/08/56/pancake-2297687_1280.jpg",
         "레시피": ["반죽 만들기", "팬에 굽기", "시럽 또는 과일 곁들이기"]},
        {"음식": "아이스크림", "이미지": "https://cdn.pixabay.com/photo/2014/12/16/22/25/ice-cream-570802_1280.jpg",
         "레시피": ["우유와 설탕 섞기", "냉동고에서 얼리기", "맛 토핑 추가"]}
    ],
    "중립 (보통)": [
        {"음식": "치즈 피자", "이미지": "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_1280.jpg",
         "레시피": ["도우 준비", "토마토소스 바르기", "치즈와 토핑 올리기", "오븐 15분 굽기"]},
        {"음식": "샌드위치", "이미지": "https://cdn.pixabay.com/photo/2014/10/23/18/05/burger-500054_1280.jpg",
         "레시피": ["빵에 마요네즈 바르기", "햄, 치즈, 채소 올리기", "덮어서 반으로 자르기"]},
        {"음식": "타코", "이미지": "https://cdn.pixabay.com/photo/2017/01/22/19/20/taco-2003468_1280.jpg",
         "레시피": ["토르티야 데우기", "소고기 볶기", "채소와 고기 넣기", "살사소스 곁들이기"]},
        {"음식": "볶음밥", "이미지": "https://cdn.pixabay.com/photo/2015/04/08/13/13/fried-rice-712665_1280.jpg",
         "레시피": ["밥 준비", "채소와 고기 볶기", "간장으로 간 맞추기"]},
        {"음식": "계란말이", "이미지": "https://cdn.pixabay.com/photo/2018/05/07/12/24/egg-3387256_1280.jpg",
         "레시피": ["계란 풀기", "팬에 부치기", "돌돌 말기"]},
        {"음식": "우동", "이미지": "https://cdn.pixabay.com/photo/2017/07/16/11/53/ramen-2509888_1280.jpg",
         "레시피": ["면 삶기", "육수 끓이기", "면과 함께 담기"]},
        {"음식": "김밥", "이미지": "https://cdn.pixabay.com/photo/2016/06/17/06/53/kimbap-1462173_1280.jpg",
         "레시피": ["밥과 재료 준비", "김 위에 얹기", "돌돌 말기", "썰기"]}
    ],
    "부정 (기분 안 좋아요)": [
        {"음식": "초콜릿 케이크", "이미지": "https://cdn.pixabay.com/photo/2017/01/26/02/06/chocolate-cake-2010993_1280.jpg",
         "레시피": ["밀가루, 코코아, 설탕 섞기", "계란, 버터 넣고 반죽", "오븐 180도 30분 굽기", "크림 바르기"]},
        {"음식": "라멘", "이미지": "https://cdn.pixabay.com/photo/2017/07/16/11/53/ramen-2509888_1280.jpg",
         "레시피": ["육수 끓이기", "면 삶기", "계란, 차슈 준비", "그릇에 담고 토핑 올리기"]},
        {"음식": "삼계탕", "이미지": "https://cdn.pixabay.com/photo/2020/06/22/08/56/chicken-soup-5327328_1280.jpg",
         "레시피": ["닭과 찹쌀, 인삼, 대추 넣기", "물 붓고 끓이기", "1시간 정도 푹 끓이기", "소금, 후추 간"]},
        {"음식": "죽", "이미지": "https://cdn.pixabay.com/photo/2018/03/11/19/37/congee-3211216_1280.jpg",
         "레시피": ["쌀 씻기", "물에 끓이기", "소금으로 간하기"]},
        {"음식": "떡볶이", "이미지": "https://cdn.pixabay.com/photo/2017/12/09/08/18/tteokbokki-3001314_1280.jpg",
         "레시피": ["떡 데우기", "양념장 만들기", "떡과 함께 볶기"]},
        {"음식": "카레", "이미지": "https://cdn.pixabay.com/photo/2016/03/05/19/02/curry-1238252_1280.jpg",
         "레시피": ["고기와 채소 볶기", "카레 가루 넣고 끓이기", "밥과 함께 담기"]},
        {"음식": "스프", "이미지": "https://cdn.pixabay.com/photo/2017/05/07/08/56/soup-2297684_1280.jpg",
         "레시피": ["재료 손질", "물과 함께 끓이기", "간 맞추기"]}
    ]
}

# ----------------------------
# Streamlit 앱 화면 설정
# ----------------------------
st.set_page_config(page_title="랜덤 음식 추천", page_icon="🍽️", layout="centered")

# 앱 타이틀 및 설명
st.title("🍽️ 기분 → 감정 분석 → 랜덤 음식 추천")
st.write("👉 기분을 입력하면 감정을 분석하고, 어울리는 음식을 랜덤으로 추천해드려요!")

# 사용자 입력 받기
user_input = st.text_input("지금 기분이 어떠신가요? (예: '오늘 너무 행복해요')")

# 사용자가 입력했을 때 실행
if user_input:
    mood = simple_sentiment_analysis(user_input)  # 감정 분석
    food_info = random.choice(mood_foods[mood])   # 해당 감정에 맞는 음식 중 랜덤 선택

    # 결과 출력
    st.success(f"**분석 결과:** {mood}")

    # 카드 형태로 음식 정보 보여주기 (HTML + CSS)
    st.markdown(f"""
    <div style="background-color:#f8f9fa; padding:20px; border-radius:15px; 
                box-shadow:2px 2px 10px rgba(0,0,0,0.1); text-align:center;">
        <h2>{food_info['음식']}</h2>
        <img src="{food_info['이미지']}" width="300" style="border-radius:10px; margin:10px 0;">
        <p><b>추천 이유:</b> {mood}</p>
    </div>
    """, unsafe_allow_html=True)

    # 레시피 단계별 출력
    st.subheader("📖 레시피")
    for step in food_info["레시피"]:
        st.write(f"- {step}")
