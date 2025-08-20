import streamlit as st
import random
import urllib.parse

# -------------------- 페이지/배경 세팅 --------------------
st.set_page_config(page_title="낭만 데이트 & 놀거리 추천", page_icon="💖", layout="wide")

ROMANTIC_BG = "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1920&q=80"
CSS = f"""
<style>
[data-testid="stAppViewContainer"] {{
  background: url('{ROMANTIC_BG}') no-repeat center/cover fixed;
}}
[data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}
.block-container {{
  backdrop-filter: blur(2px);
  background: rgba(255,255,255,0.85);
  border-radius: 16px;
  padding: 1.2rem 1.2rem 2rem;
}}
.card {{
  border-radius: 16px; padding: 10px; background: rgba(255,255,255,0.9);
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}}
.badge {{
  display:inline-block; padding: 2px 8px; margin-right:6px; border-radius: 999px;
  font-size: 12px; background: #f1f5f9;
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.title("💖 낭만 데이트 & 놀거리 맞춤 추천")
st.caption("지역 · 날씨 · 시간 · 예산 · 분위기에 맞춰 찰떡 코스를 골라줄게요!")

# -------------------- 도구 함수 --------------------
def img_for(place: str, city: str) -> str:
    """
    장소별 이미지: Unsplash 키워드 검색을 이용해 자동 매칭.
    (정확한 파일 URL을 하드코딩하지 않아도 안전하게 이미지가 떠요)
    """
    q = urllib.parse.quote(f"{city} {place}")
    # 1280x850 랜덤 이미지
    return f"https://source.unsplash.com/1280x850/?{q}"

def tag_place(name: str):
    """
    장소 이름에 따라 예산/분위기/시간/날씨 태그를 유추(룰 기반).
    너무 빡세게 구분하지 말고, 대략적으로 잘 맞도록 설계.
    """
    n = name
    moods = set()
    times = set()
    weather = "맑음"
    budget = "중간"

    # 장소 카테고리 추론
    if any(k in n for k in ["해변", "해수욕장", "호", "강", "공원", "섬", "대교", "전망대", "월지", "호수"]):
        moods.update(["힐링", "로맨틱"])
        times.update(["아침", "오후", "저녁", "밤" if any(k in n for k in ["대교", "전망대", "야경"]) else "저녁"])
        budget = "저렴"
    if any(k in n for k in ["시장", "거리", "푸드", "야시장"]):
        moods.update(["먹거리", "트렌디"])
        times.update(["점심", "저녁", "밤"])
        budget = "저렴"
        weather = "모든날씨"
    if any(k in n for k in ["궁", "사찰", "향교", "유적", "유림", "대릉원", "왕릉"]):
        moods.update(["고즈넉함", "힐링"])
        times.update(["아침", "오후"])
        budget = "저렴"
    if any(k in n for k in ["박물관", "미술관", "아쿠아", "도서관", "복합", "과학관"]):
        moods.update(["감성", "잔잔함"])
        times.update(["아침", "오후", "저녁"])
        budget = "중간"
        weather = "실내"
    if any(k in n for k in ["놀이공원", "월드", "레일바이크", "스파", "리조트"]):
        moods.update(["활동적", "신나는"])
        times.update(["아침", "오후", "저녁"])
        budget = "고급" if any(k in n for k in ["월드", "리조트", "스파"]) else "중간"
        weather = "모든날씨"
    if any(k in n for k in ["타워", "야경", "대교", "스카이"]):
        moods.add("야경")
        times.update(["저녁", "밤"])
    if "카페" in n:
        moods.update(["감성", "잔잔함"])
        times.update(["아침", "오후", "저녁"])
        weather = "실내"
        budget = "중간"

    # 기본 보정
    if not moods: moods.update(["로맨틱", "힐링"])
    if not times: times.update(["오후", "저녁"])

    return {
        "budget": budget,
        "moods": sorted(moods),
        "times": sorted(times),
        "weather": weather,
    }

BUDGET_LEVEL = {"저렴": 1, "중간": 2, "고급": 3}

def weather_ok(sel: str, p: str) -> bool:
    if sel == "맑음":   return p in ["맑음", "모든날씨"]
    if sel == "흐림":   return p in ["모든날씨", "맑음", "실내"]
    if sel == "비":     return p in ["실내", "모든날씨"]
    if sel == "눈":     return p in ["실내", "모든날씨", "맑음"]
    return True

# -------------------- 데이터: 대표 12개 도시 × 각 10스팟 이상 --------------------
CITY_PLACES = {
    "서울": [
        "한강공원", "남산타워", "롯데월드", "경복궁", "북촌 한옥마을",
        "홍대 걷고싶은거리", "청계천", "동대문 DDP", "광화문 광장", "코엑스 별마당도서관",
        "서울숲", "올림픽공원"
    ],
    "부산": [
        "해운대 해수욕장", "광안리 해변", "자갈치시장", "감천문화마을", "태종대",
        "송정 해수욕장", "동백섬 누리마루", "부산시립미술관", "서면 번화가", "영도대교 야경"
    ],
    "제주": [
        "성산일출봉", "협재 해수욕장", "우도", "용두암", "정방폭포",
        "천지연폭포", "서귀포 매일올레시장", "카멜리아 힐", "에코랜드", "한라산 국립공원"
    ],
    "강릉": [
        "경포대 해변", "안목 커피거리", "정동진", "오죽헌", "주문진수산시장",
        "사천진 해변", "송정 해변", "하슬라아트월드", "참소리축음기박물관", "경포호 산책"
    ],
    "여수": [
        "오동도", "향일암", "여수 해상케이블카", "아쿠아플라넷 여수", "돌산공원",
        "여수 밤바다", "만성리 검은모래해변", "이순신광장", "낭만포차거리", "거문도"
    ],
    "전주": [
        "전주 한옥마을", "경기전", "남부시장 청년몰", "전주향교", "남천교",
        "덕진공원", "한벽당", "오목대", "전주수목원", "객사길 카페거리"
    ],
    "경주": [
        "불국사", "석굴암", "첨성대", "동궁과 월지", "대릉원",
        "경주월드", "황리단길", "보문호", "국립경주박물관", "문무대왕릉"
    ],
    "속초": [
        "설악산", "속초 해수욕장", "영금정", "대포항", "아바이마을",
        "속초 중앙시장", "청초호", "외옹치", "바다향기로길", "설악 워터피아"
    ],
    "춘천": [
        "남이섬", "제이드가든", "소양강 스카이워크", "강촌 레일바이크", "공지천",
        "구봉산 전망대", "춘천막국수 골목", "춘천호", "김유정 문학촌", "애니메이션 박물관"
    ],
    "인천": [
        "차이나타운", "월미도", "송도 센트럴파크", "소래포구", "을왕리 해수욕장",
        "개항장 문화거리", "송월동 동화마을", "청라 호수공원", "파라다이스시티", "강화도 고려궁지"
    ],
    "대구": [
        "수성못", "동성로", "서문시장", "앞산 전망대", "팔공산",
        "이월드", "김광석 다시그리기길", "대구수목원", "근대골목", "83타워"
    ],
    "대전": [
        "한밭수목원", "엑스포과학공원", "대전오월드", "성심당 본점", "유림공원",
        "대청호", "보문산", "중앙로 스카이로드", "테미오래", "환범석길"
    ]
}

# 각 장소를 풍부한 메타로 확장
CITY_DATA = {}
for city, places in CITY_PLACES.items():
    CITY_DATA[city] = []
    for p in places:
        meta = tag_place(p)
        CITY_DATA[city].append({
            "name": p,
            "city": city,
            "budget": meta["budget"],
            "moods": meta["moods"],
            "times": meta["times"],
            "weather": meta["weather"],
            "img": img_for(p, city),
        })

# -------------------- 사이드바(필터) --------------------
with st.sidebar:
    st.subheader("🎯 필터")
    city = st.selectbox("지역", list(CITY_DATA.keys()))
    weather_sel = st.selectbox("날씨", ["맑음", "흐림", "비", "눈"])
    time_sel = st.selectbox("시간대", ["아침", "점심", "오후", "저녁", "밤"])
    budget_sel = st.selectbox("예산(최대)", ["저렴", "중간", "고급"])
    mood_sel = st.selectbox("분위기", ["로맨틱", "힐링", "활동적", "먹거리", "트렌디", "감성", "잔잔함", "고즈넉함", "야경"])

    top_n = st.slider("표시 개수", 3, 12, 9)
    st.caption("Tip: 조건이 까다로우면 결과가 적을 수 있어요. 개수를 조절해 보세요!")

# -------------------- 필터링 --------------------
cands = []
for place in CITY_DATA[city]:
    if not weather_ok(weather_sel, place["weather"]):
        continue
    if time_sel not in place["times"]:
        continue
    if mood_sel not in place["moods"]:
        continue
    if BUDGET_LEVEL[place["budget"]] > BUDGET_LEVEL[budget_sel]:
        continue
    cands.append(place)

# 부족하면 완화 로직(날씨 먼저 완화 → 분위기 완화)
if len(cands) == 0:
    loose = []
    for place in CITY_DATA[city]:
        if time_sel in place["times"] and BUDGET_LEVEL[place["budget"]] <= BUDGET_LEVEL[budget_sel]:
            if mood_sel in place["moods"] or weather_ok(weather_sel, place["weather"]):
                loose.append(place)
    cands = loose

# 랜덤 셔플해서 상위 N개
random.shuffle(cands)
show = cands[:top_n] if cands else []

# -------------------- 결과 렌더링 --------------------
if not show:
    st.warning("조건에 맞는 장소가 없어요. 필터를 완화해 볼까요?")
else:
    st.subheader(f"🌆 {city} 추천 스팟")
    cols = st.columns(3)
    for i, p in enumerate(show):
        with cols[i % 3]:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.image(p["img"], use_container_width=True)
            st.markdown(f"**{p['name']}**")
            st.markdown(
                f"<span class='badge'>예산: {p['budget']}</span>"
                f"<span class='badge'>분위기: {', '.join(p['moods'])}</span>"
                f"<span class='badge'>시간: {', '.join(p['times'])}</span>"
                f"<span class='badge'>날씨: {p['weather']}</span>",
                unsafe_allow_html=True
            )
            st.markdown('</div>', unsafe_allow_html=True)

# -------------------- 간단 코스 제안 --------------------
st.markdown("---")
st.subheader("🧭 3스톱 코스 제안")

# 선택 시간대 기준으로 인접 시간대 코스 구성
flow_map = {
    "아침": ["아침", "오후", "저녁"],
    "점심": ["점심", "오후", "저녁"],
    "오후": ["오후", "저녁", "밤"],
    "저녁": ["저녁", "밤", "밤"],
    "밤":   ["오후", "저녁", "밤"],
}
flow = flow_map[time_sel]

def pick_for(t):
    pool = [p for p in CITY_DATA[city]
            if (t in p["times"])
            and weather_ok(weather_sel, p["weather"])
            and BUDGET_LEVEL[p["budget"]] <= BUDGET_LEVEL[budget_sel]
            and (mood_sel in p["moods"])]
    if not pool:  # 완화
        pool = [p for p in CITY_DATA[city] if t in p["times"]]
    return random.choice(pool) if pool else None

step1, step2, step3 = pick_for(flow[0]), pick_for(flow[1]), pick_for(flow[2])
itinerary = [s for s in (step1, step2, step3) if s]

if itinerary:
    c = st.columns(len(itinerary))
    titles = ["1️⃣ 시작", "2️⃣ 메인", "3️⃣ 피날레"]
    for i, pl in enumerate(itinerary):
        with c[i]:
            st.markdown(f"**{titles[i]} · {flow[i]} · {pl['name']}**")
            st.image(pl["img"], use_container_width=True)
else:
    st.info("코스를 만들 수 있는 후보가 부족해요. 조건을 조금 넓혀볼까요?")
