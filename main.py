import streamlit as st

# MBTI별 직업 추천 데이터
mbti_jobs = {
    "ISTJ": ["회계사", "변호사", "엔지니어", "관리자"],
    "ISFJ": ["교사", "간호사", "사회복지사", "도서관 사서"],
    "INFJ": ["심리상담가", "작가", "연구원", "인권운동가"],
    "INTJ": ["전략가", "데이터 사이언티스트", "컨설턴트", "엔지니어"],
    "ISTP": ["정비사", "파일럿", "경찰", "기술자"],
    "ISFP": ["아티스트", "사진작가", "요리사", "디자이너"],
    "INFP": ["작가", "상담가", "교사", "예술가"],
    "INTP": ["연구원", "개발자", "분석가", "발명가"],
    "ESTP": ["기업가", "세일즈", "스포츠 코치", "구조대원"],
    "ESFP": ["배우", "가수", "이벤트 기획자", "관광가이드"],
    "ENFP": ["마케터", "작가", "교사", "창업가"],
    "ENTP": ["사업가", "기획자", "변호사", "방송인"],
    "ESTJ": ["관리자", "군인", "팀 리더", "프로젝트 매니저"],
    "ESFJ": ["교사", "간호사", "인사담당자", "상담사"],
    "ENFJ": ["코치", "강사", "정치인", "프로듀서"],
    "ENTJ": ["CEO", "변호사", "전략기획가", "투자자"]
}

st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼")

st.title("💼 MBTI 기반 직업 추천 앱")
st.write("당신의 MBTI를 선택하면 추천 직업을 알려드립니다.")

# MBTI 선택
selected_mbti = st.selectbox("MBTI를 선택하세요:", list(mbti_jobs.keys()))

# 결과 표시
if selected_mbti:
    st.subheader(f"{selected_mbti} 유형 추천 직업")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")

