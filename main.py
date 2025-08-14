import streamlit as st

# --- MBTI 데이터 + 색상 + 이미지 ---
mbti_data = {
    "ISTJ": {
        "desc": "신중하고 철저하며 체계적인 현실주의자",
        "jobs": ["📊 회계사", "⚖️ 변호사", "🛠️ 엔지니어", "📋 관리자"],
        "color": "#4E6E81",
        "image": "https://images.unsplash.com/photo-1507679799987-c73779587ccf"
    },
    "ISFJ": {
        "desc": "성실하고 헌신적이며 타인을 돕는 조력자",
        "jobs": ["👩‍🏫 교사", "💉 간호사", "🤝 사회복지사", "📚 사서"],
        "color": "#8A9A5B",
        "image": "https://images.unsplash.com/photo-1524492449094-2d8a1dfb9d19"
    },
    "INFJ": {
        "desc": "통찰력 있고 가치 지향적인 이상주의자",
        "jobs": ["🧠 심리상담가", "✍️ 작가", "🔬 연구원", "🕊️ 인권운동가"],
        "color": "#6C5B7B",
        "image": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d"
    },
    "INTJ": {
        "desc": "전략적이고 목표 지향적인 비전가",
        "jobs": ["📈 전략가", "💻 데이터 사이언티스트", "📊 컨설턴트", "🛠️ 엔지니어"],
        "color": "#1F3B4D",
        "image": "https://images.unsplash.com/photo-1487014679447-9f8336841d58"
    },
    "ISTP": {
        "desc": "문제 해결에 능한 실용주의자",
        "jobs": ["🔧 정비사", "✈️ 파일럿", "🚓 경찰", "⚙️ 기술자"],
        "color": "#455A64",
        "image": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d"
    },
    "ISFP": {
        "desc": "온화하고 예술적인 감각을 가진 사람",
        "jobs": ["🎨 아티스트", "📷 사진작가", "👩‍🍳 요리사", "🎭 디자이너"],
        "color": "#A1887F",
        "image": "https://images.unsplash.com/photo-1522202195461-3c8e17b7812f"
    },
    "INFP": {
        "desc": "이상과 가치를 추구하는 낭만주의자",
        "jobs": ["✍️ 작가", "💬 상담가", "👩‍🏫 교사", "🎨 예술가"],
        "color": "#9C6D97",
        "image": "https://images.unsplash.com/photo-1487412912498-0447578fcca8"
    },
    "INTP": {
        "desc": "창의적이고 분석적인 사색가",
        "jobs": ["🔬 연구원", "💻 개발자", "📊 분석가", "💡 발명가"],
        "color": "#34495E",
        "image": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d"
    },
    "ESTP": {
        "desc": "에너지 넘치고 도전적인 모험가",
        "jobs": ["💼 기업가", "📈 세일즈", "🏋️ 스포츠 코치", "🚒 구조대원"],
        "color": "#E67E22",
        "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"
    },
    "ESFP": {
        "desc": "사교적이고 활발한 엔터테이너",
        "jobs": ["🎭 배우", "🎤 가수", "🎉 이벤트 기획자", "🌍 관광가이드"],
        "color": "#F39C12",
        "image": "https://images.unsplash.com/photo-1524253482453-3fed8d2fe12b"
    },
    "ENFP": {
        "desc": "창의적이고 열정적인 아이디어 뱅크",
        "jobs": ["📢 마케터", "✍️ 작가", "👩‍🏫 교사", "🚀 창업가"],
        "color": "#FF8A65",
        "image": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d"
    },
    "ENTP": {
        "desc": "변화를 즐기는 발명가",
        "jobs": ["💼 사업가", "📝 기획자", "⚖️ 변호사", "📺 방송인"],
        "color": "#D35400",
        "image": "https://images.unsplash.com/photo-1487412912498-0447578fcca8"
    },
    "ESTJ": {
        "desc": "책임감 있고 체계적인 지도자",
        "jobs": ["📋 관리자", "🪖 군인", "👨‍💼 팀 리더", "📊 프로젝트 매니저"],
        "color": "#2C3E50",
        "image": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d"
    },
    "ESFJ": {
        "desc": "친절하고 사교적인 협력가",
        "jobs": ["👩‍🏫 교사", "💉 간호사", "🧑‍💼 인사담당자", "💬 상담사"],
        "color": "#27AE60",
        "image": "https://images.unsplash.com/photo-1522202195461-3c8e17b7812f"
    },
    "ENFJ": {
        "desc": "영감을 주는 카리스마 있는 리더",
        "jobs": ["🏆 코치", "🎤 강사", "🏛️ 정치인", "🎬 프로듀서"],
        "color": "#8E44AD",
        "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"
    },
    "ENTJ": {
        "desc": "결단력 있는 전략가",
        "jobs": ["👔 CEO", "⚖️ 변호사", "📊 전략기획가", "💹 투자자"],
        "color": "#C0392B",
        "image": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d"
    }
}

# --- 페이지 설정 ---
st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼", layout="centered")

# --- 타이틀 ---
st.title("💼 MBTI 기반 직업 추천")
st.write("당신의 MBTI를 선택하면 맞춤 직업과 성격 설명을 카드 형식으로 보여드립니다.")

# --- 선택 박스 ---
selected_mbti = st.selectbox("MBTI를 선택하세요:", list(mbti_data.keys()))

if selected_mbti:
    color = mbti_data[selected_mbti]["color"]
    desc = mbti_data[selected_mbti]["desc"]
    jobs = mbti_data[selected_mbti]["jobs"]
    image_url = mbti_data[selected_mbti]["image"]

    # --- 카드 스타일 ---
    st.markdown(f"""
        <style>
            .profile-card {{
                background-color: white;
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                border-top: 6px solid {color};
                margin-top: 20px;
            }}
            .desc-box {{
                background-color: {color}20;
                padding: 15px;
                border-radius: 10px;
                margin-top: 10px;
            }}
            .job-card {{
                background-color: {color}15;
                border: 1px solid {color};
                color: {color};
                border-radius: 10px;
                padding: 8px 12px;
                margin-bottom: 8px;
                font-weight: 500;
                box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            }}
        </style>
    """, unsafe_allow_html=True)

    # --- 카드 UI ---
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(image_url, use_container_width=True)
        with col2:
            st.markdown(f"<div class='profile-card'>"
                        f"<h2 style='color:{color};'>{selected_mbti}</h2>"
                        f"<div class='desc-box'>{desc}</div>"
                        f"<h4 style='margin-top:20px;'>추천 직업</h4>",
                        unsafe_allow_html=True)
            for job in jobs:
                st.markdown(f"<div class='job-card'>{job}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
