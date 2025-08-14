import streamlit as st

# --- 데이터 ---
mbti_data = {
    "ISTJ": {
        "desc": "신중하고 철저하며 체계적인 현실주의자",
        "jobs": ["📊 회계사", "⚖️ 변호사", "🛠️ 엔지니어", "📋 관리자"]
    },
    "ISFJ": {
        "desc": "성실하고 헌신적이며 타인을 돕는 조력자",
        "jobs": ["👩‍🏫 교사", "💉 간호사", "🤝 사회복지사", "📚 사서"]
    },
    "INFJ": {
        "desc": "통찰력 있고 가치 지향적인 이상주의자",
        "jobs": ["🧠 심리상담가", "✍️ 작가", "🔬 연구원", "🕊️ 인권운동가"]
    },
    "INTJ": {
        "desc": "전략적이고 목표 지향적인 비전가",
        "jobs": ["📈 전략가", "💻 데이터 사이언티스트", "📊 컨설턴트", "🛠️ 엔지니어"]
    },
    "ISTP": {
        "desc": "문제 해결에 능한 실용주의자",
        "jobs": ["🔧 정비사", "✈️ 파일럿", "🚓 경찰", "⚙️ 기술자"]
    },
    "ISFP": {
        "desc": "온화하고 예술적인 감각을 가진 사람",
        "jobs": ["🎨 아티스트", "📷 사진작가", "👩‍🍳 요리사", "🎭 디자이너"]
    },
    "INFP": {
        "desc": "이상과 가치를 추구하는 낭만주의자",
        "jobs": ["✍️ 작가", "💬 상담가", "👩‍🏫 교사", "🎨 예술가"]
    },
    "INTP": {
        "desc": "창의적이고 분석적인 사색가",
        "jobs": ["🔬 연구원", "💻 개발자", "📊 분석가", "💡 발명가"]
    },
    "ESTP": {
        "desc": "에너지 넘치고 도전적인 모험가",
        "jobs": ["💼 기업가", "📈 세일즈", "🏋️ 스포츠 코치", "🚒 구조대원"]
    },
    "ESFP": {
        "desc": "사교적이고 활발한 엔터테이너",
        "jobs": ["🎭 배우", "🎤 가수", "🎉 이벤트 기획자", "🌍 관광가이드"]
    },
    "ENFP": {
        "desc": "창의적이고 열정적인 아이디어 뱅크",
        "jobs": ["📢 마케터", "✍️ 작가", "👩‍🏫 교사", "🚀 창업가"]
    },
    "ENTP": {
        "desc": "변화를 즐기는 발명가",
        "jobs": ["💼 사업가", "📝 기획자", "⚖️ 변호사", "📺 방송인"]
    },
    "ESTJ": {
        "desc": "책임감 있고 체계적인 지도자",
        "jobs": ["📋 관리자", "🪖 군인", "👨‍💼 팀 리더", "📊 프로젝트 매니저"]
    },
    "ESFJ": {
        "desc": "친절하고 사교적인 협력가",
        "jobs": ["👩‍🏫 교사", "💉 간호사", "🧑‍💼 인사담당자", "💬 상담사"]
    },
    "ENFJ": {
        "desc": "영감을 주는 카리스마 있는 리더",
        "jobs": ["🏆 코치", "🎤 강사", "🏛️ 정치인", "🎬 프로듀서"]
    },
    "ENTJ": {
        "desc": "결단력 있는 전략가",
        "jobs": ["👔 CEO", "⚖️ 변호사", "📊 전략기획가", "💹 투자자"]
    }
}

# --- 페이지 설정 ---
st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼", layout="centered")

# --- 스타일 ---
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .job-card {
            background-color: white;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            font-size: 18px;
        }
        .desc-box {
            background-color: #e9ecef;
            border-radius: 10px;
            padding: 15px;
            margin-top: 10px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# --- 타이틀 ---
st.title("💼 MBTI 기반 직업 추천")
st.write("당신의 MBTI를 선택하면 맞춤 직업과 성격 설명을 알려드립니다.")

# --- 선택 박스 ---
selected_mbti = st.selectbox("MBTI를 선택하세요:", list(mbti_data.keys()))

# --- 결과 출력 ---
if selected_mbti:
    st.subheader(f"{selected_mbti} - {mbti_data[selected_mbti]['desc']}")
    
    # 설명 박스
    st.markdown(f"<div class='desc-box'>{mbti_data[selected_mbti]['desc']}</div>", unsafe_allow_html=True)
    
    st.write("### 추천 직업")
    for job in mbti_data[selected_mbti]["jobs"]:
        st.markdown(f"<div class='job-card'>{job}</div>", unsafe_allow_html=True)
