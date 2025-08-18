import streamlit as st
import random

st.set_page_config(page_title="숫자 맞히기 게임", layout="centered")

# ===== CSS 꾸미기 =====
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
        color: white;
    }
    /* 배경에 숫자 이미지 추가 */
    body::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('https://i.imgur.com/Z3r7Q9E.png');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0.15;
        z-index: -1;
    }
    .title {
        font-size: 40px !important;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    .stButton>button {
        background: #ff6a88;
        background: linear-gradient(45deg, #ff6a88, #ff99ac);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #ff99ac, #ff6a88);
    }
    .card {
        background: rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        margin-top: 20px;
        color: #fff;
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== 타이틀 =====
st.markdown("<h1 class='title'>🎲 숫자 맞히기 게임</h1>", unsafe_allow_html=True)

# 초기 상태 설정
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.tries = 0

st.write("1부터 100 사이의 숫자를 맞혀보세요!")

# 사용자 입력
user_input = st.number_input("숫자를 입력하세요", min_value=1, max_value=100, step=1)

if st.button("도전!"):
    st.session_state.tries += 1
    if user_input < st.session_state.secret:
        st.markdown("<div class='card'>🔼 더 큰 숫자입니다!</div>", unsafe_allow_html=True)
    elif user_input > st.session_state.secret:
        st.markdown("<div class='card'>🔽 더 작은 숫자입니다!</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='card'>🎉 정답! {st.session_state.secret} 를 맞히셨어요!<br>시도 횟수: {st.session_state.tries} 번</div>", unsafe_allow_html=True)
        if st.button("다시 시작하기"):
            st.session_state.secret = random.randint(1, 100)
            st.session_state.tries = 0
            st.experimental_rerun()
