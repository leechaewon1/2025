import streamlit as st
import random

st.set_page_config(page_title="숫자 맞히기 게임", layout="centered")

st.title("🎲 숫자 맞히기 게임")

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
        st.warning("🔼 더 큰 숫자입니다!")
    elif user_input > st.session_state.secret:
        st.warning("🔽 더 작은 숫자입니다!")
    else:
        st.success(f"🎉 정답! {st.session_state.secret} 를 맞히셨어요!")
        st.info(f"시도 횟수: {st.session_state.tries} 번")
        if st.button("다시 시작하기"):
            st.session_state.secret = random.randint(1, 100)
            st.session_state.tries = 0
            st.experimental_rerun()
