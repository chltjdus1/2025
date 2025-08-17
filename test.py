import streamlit as st

# ----------------------------
# 데이터: 기분별 음식 추천 딕셔너리
# ----------------------------
mood_foods = {
    "기분이 좋아요 😀": {
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
        "음식": "삼계탕",
        "이미지": "https://cdn.pixabay.com/photo/2020/06/22/08/56/chicken-soup-5327328_1280.jpg",
        "레시피": [
            "손질한 닭에 찹쌀, 인삼, 대추를 넣는다.",
            "물을 붓고 끓인다.",
            "중약불에서 1시간 정도 푹 고운다.",
            "소금과 후추로 간한다."
        ]
    }
}

# ----------------------------
# Streamlit 앱 구성
# ----------------------------
st.set_page_config(page_title="기분별 음식 추천", page_icon="🍽️", layout="centered")

# 헤더
st.title("🍽️ 기분 기반 음식 추천 웹사이트")
st.write("기분을 선택하면 어울리는 음식을 추천하고, 레시피까지 알려드려요!")

# 기분 입력
mood = st.selectbox("현재 기분을 선택하세요 👇", list(mood_foods.keys()))

if mood:
    food_info = mood_foods[mood]

    # 카드 UI
    st.markdown(
        f"""
        <div style="background-color:#f8f9fa; padding:20px; border-radius:15px; box-shadow:2px 2px 10px rgba(0,0,0,0.1); text-align:center;">
            <h2>{food_info['음식']}</h2>
            <img src="{food_info['이미지']}" width="300" style="border-radius:10px; margin:10px 0;">
        </div>
        """,
        unsafe_allow_html=True
    )

    # 레시피 출력
    st.subheader("📖 레시피")
    for step in food_info["레시피"]:
        st.write(f"- {step}")

