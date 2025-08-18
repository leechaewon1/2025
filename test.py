import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="점메추 – 한식/양식/중식 추천", layout="centered")

# ====== Style ======
st.markdown(
    """
    <style>
      body { background: linear-gradient(135deg,#fff5f7 0%,#e6fffa 100%);}  
      .title { text-align:center; font-size:40px; font-weight:800; }
      .pill { display:inline-block; padding:4px 10px; border-radius:999px; background:rgba(0,0,0,0.08); margin-right:6px; font-size:12px; }
      .card { background: rgba(255,255,255,0.6); padding:18px; border-radius:16px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); margin:10px 0; }
      .dish { font-size:20px; font-weight:700; }
      .desc { opacity:0.8; }
      .footer { text-align:center; opacity:0.7; font-size:12px; margin-top:10px; }
      .bigbtn button { width:100%; padding:16px; border-radius:14px; font-size:18px; font-weight:800; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='title'>🍱 점메추 – 한식 · 양식 · 중식</div>", unsafe_allow_html=True)

# ====== Data (한식/양식/중식) ======
DISHES = [
    # 한식
    {"name":"비빔밥","cuisine":"한식","spicy":"중","price":"₩₩","veg":True,"desc":"채소 듬뿍, 고추장 비빔","emoji":"🥗"},
    {"name":"김치찌개","cuisine":"한식","spicy":"매움","price":"₩","veg":False,"desc":"돼지고기+김치의 정석","emoji":"🍲"},
    {"name":"불고기","cuisine":"한식","spicy":"순","price":"₩₩","veg":False,"desc":"달짝지근 소고기 볶음","emoji":"🥢"},
    {"name":"제육볶음","cuisine":"한식","spicy":"매움","price":"₩","veg":False,"desc":"매콤달콤 돼지고기","emoji":"🌶️"},
    {"name":"칼국수","cuisine":"한식","spicy":"순","price":"₩","veg":False,"desc":"담백한 바지락 육수","emoji":"🍜"},
    # 양식
    {"name":"마르게리타 피자","cuisine":"양식","spicy":"순","price":"₩₩","veg":True,"desc":"토마토·바질·모짜렐라","emoji":"🍕"},
    {"name":"까르보나라","cuisine":"양식","spicy":"순","price":"₩₩","veg":False,"desc":"크리미한 파스타","emoji":"🍝"},
    {"name":"스테이크","cuisine":"양식","spicy":"순","price":"₩₩₩","veg":False,"desc":"굽기 선택 가능한 메인","emoji":"🥩"},
    {"name":"시저샐러드","cuisine":"양식","spicy":"순","price":"₩₩","veg":True,"desc":"치즈 듬뿍 상큼","emoji":"🥗"},
    {"name":"바질페스토 파스타","cuisine":"양식","spicy":"순","price":"₩₩","veg":True,"desc":"향긋한 바질 풍미","emoji":"🌿"},
    # 중식
    {"name":"짜장면","cuisine":"중식","spicy":"순","price":"₩","veg":False,"desc":"춘장과 쫄깃 면발","emoji":"🍜"},
    {"name":"짬뽕","cuisine":"중식","spicy":"매움","price":"₩","veg":False,"desc":"얼큰한 해물 국물","emoji":"🔥"},
    {"name":"탕수육","cuisine":"중식","spicy":"순","price":"₩₩","veg":False,"desc":"찍먹·부먹 취향 존중","emoji":"🍖"},
    {"name":"마라탕","cuisine":"중식","spicy":"매움","price":"₩₩","veg":True,"desc":"마라+건두부 커스텀","emoji":"🌶️"},
    {"name":"볶음밥","cuisine":"중식","spicy":"순","price":"₩","veg":True,"desc":"파기름 향 가득","emoji":"🍚"},
]

# ====== Session State ======
if "history" not in st.session_state:
    st.session_state.history = []  # [(name, time)]
if "seed" not in st.session_state:
    st.session_state.seed = random.randint(0, 10**9)
random.seed(st.session_state.seed)

# ====== Sidebar Filters ======
st.sidebar.subheader("필터")
selected_cuisines = st.sidebar.multiselect(
    "종류", ["한식","양식","중식"], default=["한식","양식","중식"]
)
spicy = st.sidebar.multiselect("매운맛", ["순","중","매움"], default=["순","중","매움"])
price = st.sidebar.multiselect("가격대", ["₩","₩₩","₩₩₩"], default=["₩","₩₩","₩₩₩"])
veg_only = st.sidebar.checkbox("채식(또는 채식 옵션)만 보기", value=False)
count = st.sidebar.slider("추천 개수", 1, 3, 1)

# ====== Core Recommend ======
@st.cache_data(show_spinner=False)
def get_pool(selected_cuisines, spicy, price, veg_only):
    pool = [d for d in DISHES if d["cuisine"] in selected_cuisines and d["spicy"] in spicy and d["price"] in price]
    if veg_only:
        pool = [d for d in pool if d["veg"]]
    return pool

pool = get_pool(selected_cuisines, spicy, price, veg_only)

# Big random button
st.markdown("### 오늘 점심은?")
spin_col = st.container()
with spin_col:
    spin = st.button("🎰 추천 받기", type="primary")

if spin:
    if not pool:
        st.warning("조건에 맞는 메뉴가 없어요. 필터를 넓혀보세요!")
    else:
        picks = random.sample(pool, k=min(count, len(pool)))
        for p in picks:
            st.markdown(
                f"""
                <div class='card'>
                  <div class='dish'>{p['emoji']} {p['name']} <span class='pill'>{p['cuisine']}</span>
                    <span class='pill'>{p['spicy']}</span>
                    <span class='pill'>{p['price']}</span>
                    {'<span class=\'pill\'>VEG</span>' if p['veg'] else ''}
                  </div>
                  <div class='desc'>{p['desc']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.session_state.history.append((p["name"], datetime.now().strftime("%H:%M")))

# ====== Reroll & Seed ======
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🔄 다시 추천"):
        st.session_state.seed = random.randint(0, 10**9)
        st.experimental_rerun()
with col2:
    if st.button("🧹 히스토리 지우기"):
        st.session_state.history = []
        st.success("히스토리를 지웠어요!")
with col3:
    st.caption("필터를 바꿔서 취향을 좁혀보세요 👇")

# ====== History ======
with st.expander("📜 오늘의 추천 히스토리"):
    if st.session_state.history:
        for n, t in reversed(st.session_state.history[-15:]):
            st.write(f"{t} · {n}")
    else:
        st.caption("아직 추천 이력이 없어요.")

st.markdown("<div class='footer'>🍽️ 맛있게 드세요! – 점메추 봇</div>", unsafe_allow_html=True)
