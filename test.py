import streamlit as st

# ----------------------------
# 간단한 한국어 감정 분석기 (키워드 기반)
# ----------------------------
def simple_sentiment_analysis(text):
    text = text.lower()

    positive_keywords = ["좋아", "행복", "즐거", "신나", "기쁨", "만족"]
    negative_keywords = ["슬퍼", "우울", "짜증", "화나", "싫어", "힘들"]
    
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
# 기분별 음식 추천 데이터
# ----------------------------
mood_foods = {
    "긍정 (기분 좋아요)": {
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
    "중립 (보통)": {
        "음식": "치즈 피자",
        "이미지": "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_1280.jpg",
        "레시피": [
            "피자 도우를 준비한다.",
            "토마토소스를 도우 위에 바른다.",
            "치즈와 토핑을 올린다.",
            "오븐에 200도에서 15분간 굽는다."
        ]
    },
    "부정 (기분 안 좋아요)": {
        "음식": "초콜릿 케이크",
        "이미지": "https://cdn.pixabay.com/photo/2017/01/26/02/06/chocolate-cake-2010993_1280.jpg",
        "레시피": [
            "밀가루, 코코아가루, 설탕을 섞는다.",
            "계란과 버터를 넣고 반죽한다.",
            "오븐에서 180도로 30분간 굽는다.",
            "초콜릿 크림을 위에 바른다."
        ]
    }
}

# ----------------------------
# Streamlit 앱 구성
# ----------------------------
st.set_page_config(page_title="간단 AI 감정 음식 추천", page_icon="🍽️", layout="centered")
st.title("🍽️ 기분 입력 → 간단 감정 분석 → 음식 추천")
st.write("지금 기분을 입력하면 간단한 감정 분석기를 통해 어울리는 음식을 추천해드려요!")

# 텍스트 입력 받기
user_input = st.text_input("지금 어떤 기분이신가요? (예: '오늘 너무 행복해요')")

if user_input:
    mood = simple_sentiment_analysis(user_input)
    food_info = mood_foods[mood]

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
