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
    "임(壬)":"수", "계(癸)":"수"
}

# --- 계산 함수: 단순 연도 간지(안전 fallback) ---
def year_ganzhi_by_year(year):
    # 간: (year - 4) % 10, 지: (year - 4) % 12  (중국 전통 공식)
    g = (year - 4) % 10
    z = (year - 4) % 12
    return Gan[g], Zhi[z], ShX[z]

# --- 본문: 계산/출력 ---
if do_calc:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    try:
        import sxtwl
        have_sxtwl = True
    except Exception:
        have_sxtwl = False

    # 기본 입력값 정리
    y = date_input.year
    m = date_input.month
    d = date_input.day
    hour = time_input.hour
    minute = time_input.minute

    st.subheader("입력 확인")
    st.write(f"- 생년월일(양력) : {y}-{m:02d}-{d:02d}")
    st.write(f"- 출생시각 : {hour:02d}:{minute:02d}")
    st.write(f"- 성별 : {sex}")
    st.write(f"- 입춘 기준(년주) 적용 : {'예' if li_chun_boundary else '아니오'}")
    st.write("---")

    if use_sxtwl and have_sxtwl:
        # sxtwl로 정확 계산
        try:
            day = sxtwl.fromSolar(y, m, d)
            # 연간지: getYearGZ(True) -> 춘절(설)기준, getYearGZ() -> 입춘기준(문서 기준)
            if li_chun_boundary:
                yg = day.getYearGZ()   # 입춘기준(기본)
            else:
                yg = day.getYearGZ(True)  # 설(춘절) 기준
            mg = day.getMonthGZ()
            dg = day.getDayGZ()
            hg = day.getHourGZ(hour)

            year_gan = Gan[yg.tg]
            year_zhi = Zhi[yg.dz]
            month_gan = Gan[mg.tg]
            month_zhi = Zhi[mg.dz]
            day_gan = Gan[dg.tg]
            day_zhi = Zhi[dg.dz]
            hour_gan = Gan[hg.tg]
            hour_zhi = Zhi[hg.dz]

            st.subheader("사주(간·지)")
            st.markdown(f"- **년주(年柱)** : {year_gan} {year_zhi}  (生肖: {ShX[yg.dz]})")
            st.markdown(f"- **월주(月柱)** : {month_gan} {month_zhi}")
            st.markdown(f"- **일주(日柱)** : {day_gan} {day_zhi}")
            st.markdown(f"- **시주(時柱)** : {hour_gan} {hour_zhi}  ({hour:02d}시 기준)")

            # 간단 오행 요약
            stems = [year_gan, month_gan, day_gan, hour_gan]
            elements = [Five.get(s, "?") for s in stems]
            st.write("---")
            st.subheader("오행 분포 (간)")
            st.write({el: elements.count(el) for el in set(elements)})

            # 간단 해석 (템플릿)
            st.write("---")
            st.subheader("간단 해석 ✨")
            # 핵심: 일간(일주의 간) 중심 해석
            il = day_gan
            il_elem = Five.get(il, "알수없음")
            st.markdown(f"- **당신의 일간(主)**: **{il}** → 오행: **{il_elem}**")
            if interpret_level >= 2:
                st.markdown(f"- 요약: 일간이 **{il_elem}**인 당신은 기본적으로 **{il_elem}의 특성**을 띕니다. (예: 목→생성/성장, 화→열정/변화, 토→안정/중심, 금→정리/단호, 수→유연/지혜)")
            if interpret_level >= 3:
                st.markdown("- 더 디테일한 공망/대운/신살 분석은 전문 사주 프로그램과 비교하세요.")

        except Exception as e:
            st.error("sxtwl로 계산 중 오류가 발생했습니다. (내부 오류) — fallback 모드로 연도 간지만 출력합니다.")
            st.write("오류:", e)
            gg, zz, animal = year_ganzhi_by_year(y)
            st.subheader("(Fallback) 연주(年柱)")
            st.write(f"- {gg} {zz} (生肖: {animal})")
    else:
        # sxtwl 미설치 혹은 비활성: 연도 간지만 계산해서 보여줌
        if use_sxtwl and not have_sxtwl:
            st.warning("sxtwl 라이브러리가 설치되어 있지 않습니다. pip install sxtwl 로 설치하면 음력/절기 기준의 정확한 사주 계산이 가능합니다.")
        gg, zz, animal = year_ganzhi_by_year(y)
        st.subheader("연주(年柱) - 간이 계산")
        st.write(f"- {gg} {zz} (生肖: {animal})")
        st.write("※ 월·일·시의 정확한 간지는 음력/절기 계산이 필요합니다. sxtwl 설치를 권장합니다.")

    st.markdown("</div>", unsafe_allow_html=True)

    # 하단: 엔터테인먼트 뽑기(랜덤 운세 한줄)
    st.markdown("<div class='card' style='margin-top:12px;'>", unsafe_allow_html=True)
    st.subheader("오늘의 한줄 운세 (놀이용)")
    fortune_pool = [
        "오늘은 작은 기회가 큰 결실로 이어질 수 있어요. 눈에 띄는 제안이 오면 한 번 고민해보세요.",
        "타인과의 소통이 관건입니다. 오해가 생기기 쉬우니 말은 신중하게.",
        "재물운은 완만합니다. 지출을 살짝 줄이면 여유가 생깁니다.",
        "연애운이 좋습니다. 새로운 만남에 열린 태도를 유지하세요.",
        "건강 관리가 필요합니다. 충분한 수면과 수분을 잊지 마세요."
    ]
    st.markdown(f"- **{random.choice(fortune_pool)}**")
    st.markdown("</div>", unsafe_allow_html=True)

    st.info("사용 목적: **엔터테인먼트용**입니다. 전문적·정밀한 사주 분석은 전문 사주가에게 문의하세요.")
else:
    st.write("왼쪽 패널에서 생년월일·시간을 입력하고 '사주 보기' 버튼을 눌러주세요.")
