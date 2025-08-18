import streamlit as st
import random

st.set_page_config(page_title="남자아이돌 이상형 월드컵", layout="centered")

st.title("🌟 남자아이돌 이상형 월드컵 🌟")

# 후보 리스트
idols = [
    "정국(BTS)", "차은우(아스트로)", "태민(샤이니)", "지민(BTS)",
    "민호(샤이니)", "백현(EXO)", "카이(EXO)", "RM(BTS)",
    "진(BTS)", "재현(NCT)", "도영(NCT)", "보검(배우지만 특별출전)"
]

# 상태 저장
if "round" not in st.session_state:
    random.shuffle(idols)
    st.session_state.round = idols
    st.session_state.winners = []
    st.session_state.stage = 1

st.subheader(f"🔥 {len(st.session_state.round)}강 {st.session_state.stage}라운드")

if len(st.session_state.round) > 1:
    left, right = st.columns(2)
    idol1 = st.session_state.round[0]
    idol2 = st.session_state.round[1]

    with left:
        st.button(idol1, on_click=lambda: st.session_state.winners.append(idol1))
    with right:
        st.button(idol2, on_click=lambda: st.session_state.winners.append(idol2))

    # 버튼 클릭 후 진행
    if len(st.session_state.winners) > 0 and (len(st.session_state.winners) + len(st.session_state.round) - 2) % 2 == 0:
        st.session_state.round = st.session_state.round[2:]

        if len(st.session_state.round) == 0:
            st.session_state.round = st.session_state.winners
            st.session_state.winners = []
            st.session_state.stage += 1
            st.experimental_rerun()

elif len(st.session_state.round) == 1:
    winner = st.session_state.round[0]
    st.success(f"🏆 최종 우승자는 {winner} 입니다!")
