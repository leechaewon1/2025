import streamlit as st
import random

# ===== 기본 페이지 설정 =====
st.set_page_config(
    page_title="MBTI 이상형 찾기",
    page_icon="💘",
    layout="wide"
)

# ===== 스타일 커스터마이징 =====
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fad0c4);
        font-family: 'Nanum Gothic', sans-serif;
    }
    .stButton > button {
        background: linear-gradient(45deg, #ff6b6b, #f06595);
        color: white;
        border: none;
        padding: 0.7em 1.5em;
        font-size: 1.2em;
        border-radius: 15px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #f06595, #ff6b6b);
        transform: scale(1.05);
    }
    .result-card {
        background: white;
        padding: 2em;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== MBTI 상성 데이터 =====
ideal_type = {
    "INTJ": ["ENFP", "ENTP"],
    "INTP": ["ENTJ", "ESTJ"],
    "ENTJ": ["INTP", "INFJ"],
    "ENTP": ["INFJ", "INTJ"],
    "INFJ": ["ENFP", "ENTP"],
    "INFP": ["ENFJ", "ENTJ"],
    "ENFJ": ["INFP", "ISFP"],
    "ENFP": ["INFJ", "INTJ"],
    "ISTJ": ["ESFP", "ESTP"],
    "ISFJ": ["ESFP", "ESTP"],
    "ESTJ": ["ISTP", "ISFP"],
    "ESFJ": ["ISFP", "ISTP"],
    "ISTP": ["ESTJ", "ESFJ"],
    "ISFP": ["ENFJ", "ESFJ"],
    "ESTP": ["ISFJ", "ISTJ"],
    "ESFP": ["ISFJ", "ISTJ"]
}

# ===== 메인 제목 =====
st.markdown("<h1 style='text-align:center; color:white;'>💘 MBTI로 이상형 찾기 💘</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; font-size:1.2em;'>당신의 MBTI를 입력하면 찰떡궁합 이상형을 알려드려요!</p>", unsafe_allow_html=True)

# ===== 입력 =====
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    mbti_input = st.text_input("당신의 MBTI를 입력하세요", placeholder="예: ENFP").upper()

# ===== 결과 =====
if st.button("이상형 찾기 💡"):
    if mbti_input in ideal_type:
        partner = random.choice(ideal_type[mbti_input])
        st.markdown(
            f"""
            <div class='result-card'>
                <h2>당신의 MBTI: {
