import streamlit as st
import random

# ===== 기본 페이지 설정 =====
st.set_page_config(
    page_title="MBTI 이상형 찾기",
    page_icon="💘",
    layout="wide"
)

# ===== 스타일 =====
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);
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

# ===== 질문 리스트 (영문 값, 한글 설명) =====
questions = [
    ("파티에서 처음 보는 사람과 대화를 시작하는 편인가요?", ("E", "외향(E)"), ("I", "내향(I)")),
    ("계획을 세우는 것을 좋아하나요?", ("J", "계획형(J)"), ("P", "즉흥형(P)")),
    ("감정보다 사실과 데이터를 더 중시하나요?", ("T", "사고형(T)"), ("F", "감정형(F)")),
    ("큰 그림을 먼저 보는 편인가요?", ("N", "직관형(N)"), ("S", "감각형(S)"))
]

# ===== 앱 제목 =====
st.markdown("<h1 style='text-align:center; color:white;'>💘 MBTI 이상형 찾기 💘</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; font-size:1.2em;'>간단한 질문에 답하면 MBTI와 이상형을 추천해 드립니다!</p>", unsafe_allow_html=True)

# ===== 질문지 =====
answers = []
for q, opt1, opt2 in questions:
    choice = st.radio(q, [opt1[1], opt2[1]], index=None, key=q)
    if choice == opt1[1]:
        answers.append(opt1[0])
    elif choice == opt2[1]:
        answers.append(opt2[0])
    else:
        answers.append("")

# ===== 결과 버튼 =====
if st.button("이상형 찾기 💡"):
    if "" in answers:
        st.warning("모든 질문에 답해주세요!")
    else:
        mbti_result = "".join(answers)
        partner = random.choice(ideal_type[mbti_result])
        st.markdown(
            f"""
            <div class='result-card'>
                <h2>당신의 MBTI: {mbti_result}</h2>
                <h3>이상형 MBTI는... <span style='color:#ff6b6b;'>{partner}</span> 💕</h3>
                <p>당신과 완벽하게 어울리는 타입이에요!</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ===== 하단 =====
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white;'>✨ Made with Streamlit & ❤️</p>", unsafe_allow_html=True)
