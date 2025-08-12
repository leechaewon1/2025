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
