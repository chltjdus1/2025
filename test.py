import streamlit as st

# ----------------------------
# 데이터: 기분별 음식 추천 딕셔너리
# ----------------------------
mood_foods = {
    "기분이 좋아요 😀": {
        "키워드": ["좋아", "행복", "신남", "기분좋"],
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
    "우울해요 😔": {
        "키워드": ["우울", "슬퍼", "눈물", "힘들"],
        "음식": "초콜릿 케이크",
        "이미지": "https://cdn.pixabay.com/photo/2017/01/26/02/06/chocolate-cake-2010993_1280.jpg",
        "레시피": [
            "밀가루, 코코아가루, 설탕을 섞는다.",
            "계란과 버터를 넣고 반죽한다.",
            "오븐에서 180도로 30분간 굽는다.",
            "초콜릿 크림을 위에 바른다."
        ]
    },
    "스트레스 받아요 😡": {
        "키워드": ["화나", "짜증", "스트레스", "열받"],
        "음식": "라멘",
        "이미지": "https://cdn.pixabay.com/photo/2017/07/16/11/53/ramen-2509888_1280.jpg",
        "레시피": [
            "라멘 육수를 끓인다.",
            "면을 삶아 건져낸다.",
            "계란, 차슈, 김을 준비한다.",
            "그릇에 면과 육수를 담고 토핑을 올린다."
        ]
    },
    "피곤해요 😴": {
        "키워드": ["피곤", "졸려", "지침", "힘듦"],
        "음식": "삼계탕",
        "이미지": "https://cdn.pixabay.com/photo/2020/06/22/08/56/chicken-soup-5327328_1280.jpg",
        "레시피": [
            "손질한 닭에 찹쌀, 인삼, 대추를 넣는다.",
            "물을 붓고 끓인다.",
            "중약불에서 1시간 정도 푹 고운다.",
            "소금과 후추로 간한다."
        ]
    },
    "설레는 기분 💕": {
        "키워드": ["설레", "좋아하는사람", "두근", "사랑"],
        "음식": "초밥",
        "이미지": "https://cdn.pixabay.com/photo/2017/05/07/08/56/sushi-2297689_1280.jpg",
        "레시피": [
            "밥에 식초, 설탕, 소금을 섞어 초밥밥을 만든다.",
            "생선을 얇게 썬다.",
            "밥 위에 생선을 얹고 모양을 잡는다.",
            "와사비, 간장과 함께 곁들인다."
        ]
    },
    "외로워요 😢": {
        "키워드": ["외로", "혼자", "쓸쓸"],
        "음식": "치즈 피자",
        "이미지": "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_1280.jpg",
        "레시피": [
            "피자 도우를 준비한다.",
            "토마토소스를 도우 위에 바른다.",
            "치즈와 토핑을 올린다.",
            "오븐에 200도에서 15분간 굽는다."
        ]
    }
}

# ----------------------------
# Streamlit 앱 구성
# ----------------------------
st.set_page_config(page_title="기분별 음식 추천", page_icon="🍽️", layout="centered")

# 헤더
st.title("🍽️ 기분 기반 음식 추천 웹사이트")
st.write("지금 기분을 입력하면 어울리는 음식을 추천해드려요!")

# 텍스트 입력
user_mood = st.text_input("현재 기분을 입력하세요 👇")

def find_food_by_mood(user_text):
    for mood, info in mood_foods.items():
        for keyword in info["키워드"]:
            if keyword in user_text:
                return mood, info
    return None, None

if user_mood:
    mood, food_info = find_food_by_mood(user_mood)

    if food_info:
        # 카드 UI
        st.markdown(
            f"""
            <div style="background-color:#f8f9fa; padding:20px; border-radius:15px; 
            box-shadow:2px 2px 10px rgba(0,0,0,0.1); text-align:center;">
                <h2>{food_info['음식']}</h2>
                <img src="{food_info['이미지']}" width="300" 
                style="border-radius:10px; margin:10px 0;">
                <p><b>추천 이유:</b> {mood}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # 레시피 출력
        st.subheader("📖 레시피")
        for step in food_info["레시피"]:
            st.write(f"- {step}")
    else:
        st.warning("😥 입력하신 기분을 이해하지 못했어요. 다른 표현으로 입력해보세요!")
