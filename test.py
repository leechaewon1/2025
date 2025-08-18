import streamlit as st
import random

st.set_page_config(page_title="남자아이돌 이상형 월드컵", layout="centered")

st.title("🌟 남자아이돌 이상형 월드컵 🌟")

# 아이돌 후보 (이름 + 이미지 URL)
idols = [
    ("정국(BTS)", "https://i.imgur.com/3XbI7.jpg"),
    ("차은우(아스트로)", "https://i.imgur.com/9XcG5.jpg"),
    ("태민(샤이니)", "https://i.imgur.com/4rfg8.jpg"),
    ("지민(BTS)", "https://i.imgur.com/j9r7c.jpg"),
    ("민호(샤이니)", "https://i.imgur.com/VlKqM.jpg"),
    ("백현(EXO)", "https://i.imgur.com/kEr5K.jpg"),
    ("카이(EXO)", "https://i.imgur.com/Vzcd7.jpg"),
    ("RM(BTS)", "https://i.imgur.com/nKn5H.jpg"),
    ("진(BTS)", "https://i.imgur.com/Y3sH3.jpg"),
    ("재현(NCT)", "https://i.imgur.com/AD9qB.jpg"),
    ("도영(NCT)", "https://i.imgur.com/f9hQ2.jpg"),
    ("보검(배우)", "https://i.imgur.com/Er0pN.jpg"),
    ("영빈(SF9)", "https://i.imgur.com/f9w7r.jpg"),
    ("차훈(N.Flying)", "https://i.imgur.com/0fdfR.jpg"),
    ("은혁(슈퍼주니어)", "https://i.imgur.com/Qk2rP.jpg"),
    ("시우민(EXO)", "https://i.imgur.com/2c9Lg.jpg")
]

# 상태 저장
if "round" not in st.session_state:
    random.shuffle(idols)
    st.session_state.round = idols
    st.session_state.winners = []
    st.session_state.stage = 1

# 현재 라운드 표시
round_names = {16: "16강", 8: "8강", 4: "4강", 2: "결승"}
round_size = len(st.session_state.round)

if round_size > 1:
    st.subheader(f"🔥 {round_names[round_size]} - {st.session_state.stage}라운드")

    left, right = st.columns(2)
    idol1 = st.session_state.round[0]
    idol2 = st.session_state.round[1]

    with left:
        st.image(idol1[1], width=250)
        st.button(idol1[0], on_click=lambda: st.session_state.winners.append(idol1))

    with right:
        st.image(idol2[1], width=250)
        st.button(idol2[0], on_click=lambda: st.session_state.winners.append(idol2))

    # 버튼 클릭 시 진행
    if len(st.session_state.winners) > 0 and (len(st.session_state.winners) + round_size - 2) % 2 == 0:
        st.session_state.round = st.session_state.round[2:]

        if len(st.session_state.round) == 0:
            st.session_state.round = st.session_state.winners
            st.session_state.winners = []
            st.session_state.stage += 1
            st.experimental_rerun()

elif round_size == 1:
    winner = st.session_state.round[0]
    st.success(f"🏆 최종 우승자는 {winner[0]} 입니다!")
    st.image(winner[1], width=300)
