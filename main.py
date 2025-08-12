# app.py
import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="화려한 사주풀이", page_icon="🔮", layout="wide")

# 스타일 (화려하게)
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #654ea3 0%, #eaafc8 100%);
        font-family: 'Nanum Gothic', sans-serif;
    }
    .card {
        background: rgba(255,255,255,0.96);
        padding: 1.2rem;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    .pill {
        display:inline-block;
        background: linear-gradient(90deg,#ffd89b,#19547b);
        color:white;
        padding:6px 12px;
        border-radius:999px;
        font-weight:600;
    }
    .big {
        font-size:1.25rem;
        font-weight:700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align:center; color:#fff;'>🔮 화려한 사주풀이</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#fff;'>생년월일과 태어난 시간을 입력하면 사주(년·월·일·시)를 계산해 드립니다. (엔터테인먼트 용)</p>", unsafe_allow_html=True)

# --- 좌측: 입력 ---
with st.sidebar:
    st.header("입력")
    col1, col2 = st.columns(2)
    with col1:
        date_input = st.date_input("생년월일 (양력)", value=datetime(1990,1,1))
    with col2:
        time_input = st.time_input("출생시각 (24h)", value=datetime.strptime("12:00", "%H:%M").time())
    sex = st.selectbox("성별(음력 사용 시 참조용)", ["남성(남)","여성(여)"])
    use_sxtwl = st.checkbox("정확한 음력/절기 계산(sxtwl 사용)", value=True)
    li_chun_boundary = st.checkbox("년주: 입춘(立春) 기준으로 계산", value=True)
    interpret_level = st.slider("해석 디테일", 1, 3, 2)
    st.markdown("---")
    if st.button("사주 보기 ✨"):
        do_calc = True
    else:
        do_calc = False

# --- 도움용 상수(천간,지지,오행,띠) ---
Gan = ["갑(甲)","을(乙)","병(丙)","정(丁)","무(戊)","기(己)","경(庚)","신(辛)","임(壬)","계(癸)"]
Zhi = ["자(子)","축(丑)","인(寅)","묘(卯)","진(辰)","사(巳)","오(午)","미(未)","신(申)","유(酉)","술(戌)","해(亥)"]
ShX = ["쥐","소","호랑이","토끼","용","뱀","말","양","원숭이","닭","개","돼지"]
Five = {
    # 간 천간 오행 (간지는 기본적으로 음양+오행 속성 필요하지만 간단 표기)
    "갑(甲)":"목", "을(乙)":"목",
    "병(丙)":"화", "정(丁)":"화",
    "무(戊)":"토", "기(己)":"토",
    "경(庚)":"금", "신(辛)":"금",
    "임(壬)":"수"
