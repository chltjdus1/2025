import streamlit as st
from transformers import pipeline

# 1. 감정 분석 파이프라인 로드 (다국어 지원)
@st.cache_resource
def load_sentiment_pipeline():
    return pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

sentiment_pipeline = load_sentiment_pipeline()

# 2. 기분별 음식 추천 데이터
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

# 3. Streamlit UI 구성
st.set_page_config(page_title="AI 감정 음식 추천", page_icon="🤖🍽️", layout="centered")
st.title("🤖 기분 입력 → AI 감정 분석 → 음식 추천")
st.write("한국어로 기분을 입력하면, AI가 감정을 분석해 어울리는 음식을 추천해드려요!")

# 텍스트 입력 받기
user_input = st.text_input("지금 어떤 기분이신가요? 예: '오늘 너무 기뻐요!'")

if user_input:
    with st.spinner("AI가 기분을 분석 중이에요..."):
        result = sentiment_pipeline(user_input)[0]
        label = result["label"]  # 예: '1 star' ~ '5 stars'
        score = result["score"]

    # 점수 기반 감정 구간 설정
    if label in ["5 stars", "4 stars"]:
        mood = "긍정 (기분 좋아요)"
    elif label == "3 stars":
        mood = "중립 (보통)"
    else:
        mood = "부정 (기분 안 좋아요)"

    food_info = mood_foods[mood]

    st.write(f"**AI 감정 분석 결과:** {label} ({mood}), 신뢰도: {score:.2f}")

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

