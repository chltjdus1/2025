import streamlit as st
import random

# ----------------------------
# 간단한 한국어 감정 분석기 (키워드 기반)
# ----------------------------
def simple_sentiment_analysis(text):
    text = text.lower()

    positive_keywords = ["좋아", "행복", "즐거", "신나", "기쁨", "만족"]
    negative_keywords = ["슬퍼", "우울", "짜증", "화나", "싫어", "힘들", "피곤"]

    # 긍정 감정 판별
    if any(word in text for word in positive_keywords):
        return "긍정 (기분 좋아요)"
    # 부정 감정 판별
    elif any(word in text for word in negative_keywords):
        return "부정 (기분 안 좋아요)"
    # 나머지는 중립
    else:
        return "중립 (보통)"

# ----------------------------
# 기분별 음식 추천 데이터 (여러 개 추가)
# ----------------------------
mood_foods = {
    "긍정 (기분 좋아요)": [
        {
            "음식": "파스타",
            "이미지": "https://cdn.pixabay.com/photo/2017/12/09/08/18/spaghetti-3001311_1280.jpg",
            "레시피": [
                "스파게티 면을 삶는다.",
                "올리브유에 마늘과 양파를 볶는다.",
                "토마토소스를 넣고 졸인다.",
                "삶은 면을 넣고 섞는다.",
                "파마산 치즈를 뿌려 마무리한다."
            ]
        },
        {
            "음식": "초밥",
            "이미지": "https://cdn.pixabay.com/photo/2017/05/07/08/56/sushi-2297689_1280.jpg",
            "레시피": [
                "밥에 식초, 설탕, 소금을 섞어 초밥밥을 만든다.",
                "생선을 얇게 썬다.",
                "밥 위에 생선을 얹고 모양을 잡는다.",
                "와사비, 간장과 함께 곁들인다."
            ]
        },
        {
            "음식": "딸기 파르페",
            "이미지": "https://cdn.pixabay.com/photo/2016/11/21/15/46/strawberry-1846080_1280.jpg",
            "레시피": [
                "컵에 시리얼을 깐다.",
                "요거트를 넣고 딸기를 올린다.",
                "생크림을 올리고 다시 과일을 얹는다.",
                "민트 잎으로 장식한다."
            ]
        }
    ],
    "중립 (보통)": [
        {
            "음식": "치즈 피자",
            "이미지": "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_1280.jpg",
            "레시피": [
                "피자 도우를 준비한다.",
                "토마토소스를 도우 위에 바른다.",
                "치즈와 토핑을 올린다.",
                "오븐에 200도에서 15분간 굽는다."
            ]
        },
        {
            "음식": "샌드위치",
            "이미지": "https://cdn.pixabay.com/photo/2014/10/23/18/05/burger-500054_1280.jpg",
            "레시피": [
                "식빵에 마요네즈를 바른다.",
                "햄, 치즈, 채소를 올린다.",
                "다른 빵으로 덮는다.",
                "반으로 잘라 접시에 담는다."
            ]
        },
        {
            "음식": "타코",
            "이미지": "https://cdn.pixabay.com/photo/2017/01/22/19/20/taco-2003468_1280.jpg",
            "레시피": [
                "토르티야를 데운다.",
                "소고기를 볶고 양념한다.",
                "채소와 고기를 넣고 접는다.",
                "살사소스를 곁들인다."
            ]
        }
    ],
    "부정 (기분 안 좋아요)": [
        {
            "음식": "초콜릿 케이크",
            "이미지": "https://cdn.pixabay.com/photo/2017/01/26/02/06/chocolate-cake-2010993_1280.jpg",
            "레시피": [
                "밀가루, 코코아가루, 설탕을 섞는다.",
                "계란과 버터를 넣고 반죽한다.",
                "오븐에서 180도로 30분간 굽는다.",
                "초콜릿 크림을 위에 바른다."
            ]
        },
        {
            "음식": "라멘",
            "이미지": "https://cdn.pixabay.com/photo/2017/07/16/11/53/ramen-2509888_1280.jpg",
            "레시피": [
                "라멘 육수를 끓인다.",
                "면을 삶아 건져낸다.",
                "계란, 차슈, 김을 준비한다.",
                "그릇에 면과 육수를 담고 토핑을 올린다."
            ]
        },
        {
            "음식": "삼계탕",
            "이미지": "https://cdn.pixabay.com/photo/2020/06/22/08/56/chicken-soup-5327328_1280.jpg",
            "레시피": [
                "손질한 닭에 찹쌀, 인삼, 대추를 넣는다.",
                "물을 붓고 끓인다.",
                "중약불에서 1시간 정도 푹 고운다.",
                "소금과 후추로 간한다."
            ]
        }
    ]
}

# ----------------------------
# Streamlit 앱 구성
# ----------------------------
st.set_page_config(page_title="랜덤 음식 추천", page_icon="🍽️", layout="centered")
st.title("🍽️ 기분 입력 → 감정 분석 → 랜덤 음식 추천")
st.write("기분을 입력하면 간단한 감정 분석 후, 어울리는 음식을 랜덤으로 추천해드려요!")

# 텍스트 입력 받기
user_input = st.text_input("지금 어떤 기분이신가요? (예: '오늘 너무 행복해요')")

if user_input:
    mood = simple_sentiment_analysis(user_input)
    food_info = random.choice(mood_foods[mood])  # 랜덤 선택

    st.success(f"**분석 결과:** {mood}")

    # 카드 스타일로 결과 표시
    st.markdown(f"""
    <div style="background-color:#f8f9fa; padding:20px; border-radius:15px; 
                box-shadow:2px 2px 10px rgba(0,0,0,0.1); text-align:center;">
        <h2>{food_info['음식']}</h2>
        <img src="{food_info['이미지']}" width="300" style="border-radius:10px; margin:10px 0;">
        <p><b>추천 이유:</b> {mood}</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📖 레시피")
    for step in food_info["레시피"]:
        st.write(f"- {step}")
