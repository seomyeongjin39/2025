# app.py
import streamlit as st
import random
from textwrap import dedent

# ============ 기본 설정 ============
st.set_page_config(
    page_title="MBTI 패션 추천 ✨",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============ CSS (애니메이션 + 그라데이션 + 글라스 카드) ============
st.markdown("""
<style>
/* 전체 배경 그라데이션 */
.stApp {
  background: linear-gradient(135deg, #fff5f8 0%, #f6f9ff 50%, #f7fff5 100%);
}

/* 상단 네온 그라데이션 타이틀 */
.gradient-title {
  font-size: 48px;
  font-weight: 900;
  line-height: 1.1;
  text-align: center;
  background: linear-gradient(90deg, #ff4d6d, #ff9f1c, #2ec4b6, #6c63ff, #ff4d6d);
  -webkit-background-clip: text; background-clip: text; color: transparent;
  animation: hue 8s linear infinite;
  margin: 6px 0 2px 0;
}
@keyframes hue { from { filter: hue-rotate(0deg);} to { filter: hue-rotate(360deg);} }

/* 서브타이틀 바운스 */
.subtitle {
  text-align: center; color: #444; font-size: 18px; opacity: 0.95;
  animation: floatY 3s ease-in-out infinite;
}
@keyframes floatY { 0%,100%{transform: translateY(0)} 50%{transform: translateY(-4px)}}

/* 유리카드 */
.glass {
  background: rgba(255,255,255,0.55);
  border-radius: 18px;
  padding: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,0.5);
}

/* 팔레트 칩 */
.palette-dot {
  width: 26px; height: 26px; border-radius: 50%;
  display: inline-block; margin-right: 6px; border: 2px solid rgba(0,0,0,0.08);
}

/* 힌트/칩 */
.chip {
  display:inline-block; padding:6px 10px; border-radius:999px;
  background:#00000008; border:1px dashed #00000015; margin:4px 6px; font-size:13px;
}

/* 버튼 강조 */
.stButton>button {
  border-radius: 12px !important;
  padding: 10px 16px !important;
  box-shadow: 0 6px 16px rgba(0,0,0,0.08) !important;
}

/* 이미지 라운딩 */
img { border-radius: 14px; }
</style>
""", unsafe_allow_html=True)

# ============ 데이터: 16 MBTI 스타일 사전 ============
MBTI = [
    "ISTJ","ISFJ","INFJ","INTJ","ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP","ESTJ","ESFJ","ENFJ","ENTJ"
]

STYLE_DB = {
    "ISTJ": {
        "title": "클래식 & 타임리스 👔",
        "desc": "규칙과 디테일을 중시하는 당신에겐 모노톤·핏 깔끔 코디가 가장 설득력 있어요.",
        "palette": ["#111111","#3A3A3A","#B0B0B0","#E6E6E6"],
        "tops": ["옥스포드 셔츠","니트 베스트","미니멀 셋업 자켓"],
        "bottoms": ["테이퍼드 슬랙스","폴딩 치노"],
        "shoes": ["더비슈즈","로퍼"],
        "acc": ["심플 가죽벨트","메탈 시계"],
        "images": [
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=1200",
            "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=1200",
            "https://images.unsplash.com/photo-1520975916090-3105956dac38?q=80&w=1200"
        ],
        "hashtags": ["#모노톤","#아이비리그","#깔끔핏"]
    },
    "ISFJ": {
        "title": "따뜻한 포근함 ☕",
        "desc": "배려 깊은 분위기엔 소프트 톤 니트·스커트·카디건의 조합이 찰떡!",
        "palette": ["#F5E6E0","#EAD7D1","#D7C4BB","#8A7E72"],
        "tops": ["파스텔 카디건","라운드 니트"],
        "bottoms": ["플리츠 스커트","크림진"],
        "shoes": ["메리제인","로우 힐"],
        "acc": ["진주 이어링","플랫 캡"],
        "images": [
            "https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=1200",
            "https://images.unsplash.com/photo-1520975682031-b46f52b8505a?q=80&w=1200",
            "https://images.unsplash.com/photo-1519741497674-611481863552?q=80&w=1200"
        ],
        "hashtags": ["#파스텔","#포근","#데일리"]
    },
    "INFJ": {
        "title": "감성 미니멀 📖",
        "desc": "선택과 집중. 롱코트와 롱스커트, 차분한 톤으로 분위기 장전.",
        "palette": ["#2E2F3E","#6D6F7B","#C9CBD3","#F2F2F5"],
        "tops": ["맥시 롱코트","실키 블라우스"],
        "bottoms": ["롱스커트","와이드 슬랙스"],
        "shoes": ["첼시부츠","스퀘어토 부츠"],
        "acc": ["미니멀 목걸이","슬림 숄더백"],
        "images": [
            "https://images.unsplash.com/photo-1503342394122-34b5829731d4?q=80&w=1200",
            "https://images.unsplash.com/photo-1520975842205-52b3e25f6b09?q=80&w=1200",
            "https://images.unsplash.com/photo-1516826957135-700dedea698c?q=80&w=1200"
        ],
        "hashtags": ["#롱실루엣","#모노톤","#은은한무드"]
    },
    "INTJ": {
        "title": "시크 테크 미니멀 🖤",
        "desc": "군더더기 없는 실루엣+블랙 그레이. 기능성 원단도 잘 어울려요.",
        "palette": ["#0E0E10","#1E1F22","#3C4043","#B0B3B8"],
        "tops": ["테크자켓","하이넥 탑"],
        "bottoms": ["테크 카고","슬림 슬랙스"],
        "shoes": ["첼시부츠","미니멀 스니커즈"],
        "acc": ["블랙 가죽백","메탈 프레임 글래스"],
        "images": [
            "https://images.unsplash.com/photo-1516826957135-700dedea698c?q=80&w=1200",
            "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?q=80&w=1200",
            "https://images.unsplash.com/photo-1519741497674-611481863552?q=80&w=1200"
        ],
        "hashtags": ["#블랙온블랙","#테크웨어","#전략적핏"]
    },
    "ISTP": {
        "title": "실용 캐주얼 🛠️",
        "desc": "툭 걸치고 뛰쳐나가도 멋짐. 데님+유틸리티 아우터 조합 굿.",
        "palette": ["#1F2937","#4B5563","#9CA3AF","#E5E7EB"],
        "tops": ["워크자켓","헨리넥 티"],
        "bottoms": ["스트레이트 데님","카고팬츠"],
        "shoes": ["스케이트 스니커즈","부츠"],
        "acc": ["캡 모자","레더 팔찌"],
        "images": [
            "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?q=80&w=1200",
            "https://images.unsplash.com/photo-1519741497674-611481863552?q=80&w=1200",
            "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?q=80&w=1200"
        ],
        "hashtags": ["#유틸리티","#데님","#툭걸쳐"]
    },
    "ISFP": {
        "title": "내추럴 보헤미안 🌿",
        "desc": "자연스러운 주름과 촉감. 플로럴/린넨/루즈핏이 핵심.",
        "palette": ["#7A9E7E","#F2E8CF","#E6B89C","#9C6644"],
        "tops": ["루즈 셔츠","보헤 원피스"],
        "bottoms": ["린넨 팬츠","맥시 스커트"],
        "shoes": ["에스파드류","크로그 샌들"],
        "acc": ["라탄 백","스카프"],
        "images": [
            "https://images.unsplash.com/photo-1520975682031-b46f52b8505a?q=80&w=1200",
            "https://images.unsplash.com/photo-1519741497674-611481863552?q=80&w=1200",
            "https://images.unsplash.com/photo-1503342394122-34b5829731d4?q=80&w=1200"
        ],
        "hashtags": ["#린넨","#플로럴","#자연광"]
    },
    "INFP": {
        "title": "빈티지 드리미 🎨",
        "desc": "감성 충만 레이어드. 니트 베스트, 체크, 코듀로이로 무드 완성.",
        "palette": ["#6B4E71","#CFC0BD","#E3D5CA","#D6CCC2"],
        "tops": ["니트 베스트","로맨틱 블라우스"],
        "bottoms": ["코듀로이 팬츠","롱스커트"],
        "shoes": ["메리제인","빈티지 스니커"],
        "acc": ["토트북","베레모"],
        "images": [
            "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?q=80&w=1200",
            "https://images.unsplash.com/photo-1520975842205-52b3e25f6b09?q=80&w=1200",
            "https://images.unsplash.com/photo-1503342394122-34b5829731d4?q=80&w=1200"
        ],
        "hashtags": ["#빈티지","#레이어드","#드리미"]
    },
    "INTP": {
        "title": "컴포트 지니어스 🧢",
        "desc": "그래픽 티+후디+와이드. 편안하지만 포인트는 확실하게.",
        "palette": ["#111827","#4B5563","#93C5FD","#D1D5DB"],
        "tops": ["그래픽 티","집업 후디"],
        "bottoms": ["와이드 팬츠","트랙팬츠"],
        "shoes": ["레트로 스니커","캔버스"],
        "acc": ["백팩","캡"],
        "images": [
            "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?q=80&w=1200",
            "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?q=80&w=1200",
            "https://images.unsplash.com/photo-1519741497674-611481863552?q=80&w=1200"
        ],
        "hashtags": ["#와이드핏","#그래픽","#편안"]
    },
    "ESTP": {
        "title": "액션 스트릿 🛹",
        "desc": "조거·트랙·테크 원단. 액세서리는 과감하게!",
        "palette": ["#0F172A","#1D4ED8","#06B6D4","#E2E8F0"],
        "tops": ["트랙 재킷","메쉬 티"],
        "bottoms": ["조거팬츠","카고 쇼츠"],
        "shoes": ["러닝 스니커","하이탑"],
        "acc": ["볼캡","체인 네크리스"],
        "images": [
            "https://images.unsplash.com/photo-1475180098004-ca77a66827be?q=80&w=1200",
            "https://images.unsplash.com/photo-1516826957135-700dedea698c?q=80&w=1200",
            "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?q=80&w=1200"
        ],
        "hashtags": ["#스트릿","#테크웨어","#과감"]
    },
    "ESFP": {
        "title": "글리터 트렌드 ✨",
        "desc": "패턴·광택·큐빅으로 스팟라이트 ON!",
        "palette": ["#F72585","#B5179E","#7209B7","#3A0CA3","#4CC9F0"],
        "tops": ["시퀸 탑","패턴 셔츠"],
        "bottoms": ["레더 스커트","플레어 팬츠"],
        "shoes": ["굽있는 앵클","유광 로퍼"],
        "acc": ["볼드 귀걸이","스테이트먼트 백"],
        "images": [
            "https://images.unsplash.com/photo-1520975682031-b46f52b8505a?q=80&w=1200",
            "https://images.unsplash.com/photo-1516826957135-700dedea698c?q=80&w=1200",
            "https://images.unsplash.com/photo-1519741497674-611481863552?q=80&w=1200"
        ],
        "hashtags": ["#반짝반짝","#포인트","#파티룩"]
    },
    "ENFP": {
        "title": "컬러 팝 🌈",
        "desc": "컬러 플레이! 오버사이즈 셔츠+데님으로 자유분방하게.",
        "palette": ["#FF6B6B","#FFD166","#06D6A0","#118AB2","#073B4C"],
        "tops": ["오버 셔츠","크롭 후디"],
        "bottoms": ["스트레이트 데님","버뮤다"],
        "shoes": ["플랫폼 스니커","클로그"],
        "acc": ["버킷햇","유머러스 양말"],
        "images": [
            "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?q=80&w=1200",
            "https://images.unsplash.com/photo-1503342394122-34b5829731d4?q=80&w=1200",
            "https://images.unsplash.com/photo-1519741497674-611481863552?q=80&w=1200"
        ],
        "hashtags": ["#컬러조합","#룩실험","#자유분방"]
    },
    "ENTP": {
        "title": "실험적 믹스매치 🎭",
        "desc": "패턴+소재+실루엣을 장난스럽게 섞기! 대담할수록 재밌다.",
        "palette": ["#0D1321","#FFB703","#FB8500","#8ECAE6","#219EBC"],
        "tops": ["패턴 셔츠","베스트 레이어드"],
        "bottoms": ["체크 팬츠","트랙 팬츠"],
        "shoes": ["하이톱","첼시"],
        "acc": ["스테이트먼트 글라스","볼드 링"],
        "images": [
            "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?q=80&w=1200",
            "https://images.unsplash.com/photo-1503342394122-34b5829731d4?q=80&w=1200",
            "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?q=80&w=1200"
        ],
        "hashtags": ["#믹스매치","#아이러니","#대담"]
    },
    "ESTJ": {
        "title": "포멀 퍼포머 💼",
        "desc": "셔츠+블레이저+클린 슈즈. 프로젝트가 코디에서도 완성된다.",
        "palette": ["#0B0C10","#1F2833","#C5C6C7","#66FCF1"],
        "tops": ["클래식 셔츠","네이비 블레이저"],
        "bottoms": ["크롭 슬랙스","치노"],
        "shoes": ["더비","옥스퍼드"],
        "acc": ["타이/스카프","레더 브리프"],
        "images": [
            "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=1200",
            "https://images.unsplash.com/photo-1520975916090-3105956dac38?q=80&w=1200",
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=1200"
        ],
        "hashtags": ["#비즈니스캐주얼","#정갈","#신뢰감"]
    },
    "ESFJ": {
        "title": "스윗 프렌들리 🫶",
        "desc": "밝은 뉴트럴, 부드러운 실루엣. 모두가 좋아하는 데일리.",
        "palette": ["#FFF3E2","#FFE7CC","#FFC6C6","#D7E9F7"],
        "tops": ["라이트 가디건","러플 블라우스"],
        "bottoms": ["에이라인 스커트","라이트 데님"],
        "shoes": ["플랫","로우 힐"],
        "acc": ["진주/골드 포인트","미니 숄더백"],
        "images": [
            "https://images.unsplash.com/photo-1483985988355-763728e1935a?q=80&w=1200",
            "https://images.unsplash.com/photo-1519741497674-611481863552?q=80&w=1200",
            "https://images.unsplash.com/photo-1520975682031-b46f52b8505a?q=80&w=1200"
        ],
        "hashtags": ["#라이트톤","#따뜻한매너","#착붙데일리"]
    },
    "ENFJ": {
        "title": "우아 카리스마 💃",
        "desc": "드레이프 실루엣과 심플 액세서리로 리더의 기품 완성.",
        "palette": ["#1C1C1E","#3A3A3C","#FFD6A5","#FAEDCD"],
        "tops": ["랩 원피스","실키 셔츠"],
        "bottoms": ["맥시 스커트","와이드슬랙스"],
        "shoes": ["뾰족토 힐","슬링백"],
        "acc": ["슬림 벨트","미니멀 이어링"],
        "images": [
            "https://images.unsplash.com/photo-1520975842205-52b3e25f6b09?q=80&w=1200",
            "https://images.unsplash.com/photo-1516826957135-700dedea698c?q=80&w=1200",
            "https://images.unsplash.com/photo-1503342394122-34b5829731d4?q=80&w=1200"
        ],
        "hashtags": ["#엘레강스","#실루엣","#품격"]
    },
    "ENTJ": {
        "title": "파워 수트 👑",
        "desc": "스트럭처드 자켓, 블랙/네이비, 날 선 실루엣으로 존재감 MAX.",
        "palette": ["#0F0F10","#1F2937","#4B5563","#9CA3AF"],
        "tops": ["스트럭처드 블레이저","터틀넥"],
        "bottoms": ["슬림 슬랙스","펜슬 스커트"],
        "shoes": ["포인트 힐/로퍼","첼시"],
        "acc": ["메탈 워치","레더 토트"],
        "images": [
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=1200",
            "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=1200",
            "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?q=80&w=1200"
        ],
        "hashtags": ["#파워드레싱","#리더십","#선명한실루엣"]
    },
}

# ============ 유틸 ============
def chips(lst): 
    return " ".join([f'<span class="chip">{x}</span>' for x in lst])

def palette_html(colors):
    return "".join([f'<span class="palette-dot" style="background:{c}"></span>' for c in colors])

def surprise_mbti():
    return random.choice(MBTI)

def make_outfit(mbti, mood):
    base = STYLE_DB[mbti]
    t = random.choice(base["tops"])
    b = random.choice(base["bottoms"])
    s = random.choice(base["shoes"])
    a = random.choice(base["acc"])
    tweak = {
        "데이트": "실루엣은 부드럽게, 광택 소품 하나로 포인트 💖",
        "면접/발표": "컬러는 절제, 소재는 고급스러운 텍스처로 신뢰감 🧠",
        "페스티벌": "손이 자유로운 크로스백 + 스테이트먼트 액세서리 🎉",
        "주말카페": "편안한 핏 + 낮은 굽, 상의는 레이어드로 볼륨 ☕",
    }[mood]
    return f"- 상의: **{t}**\n- 하의: **{b}**\n- 신발: **{s}**\n- 액세서리: **{a}**\n- 무드 팁: {tweak}"

# ============ 사이드바 ============
with st.sidebar:
    st.markdown("## 🎛️ 컨트롤")
    pick_mode = st.radio("입력 방식", ["드롭다운 선택","직접 입력","랜덤 추천"], horizontal=True)
    if pick_mode == "드롭다운 선택":
        user_mbti = st.selectbox("MBTI를 선택하세요", MBTI, index=MBTI.index("ENFP"))
    elif pick_mode == "직접 입력":
        user_mbti = st.text_input("MBTI 4글자 (예: INFP)").upper()
    else:
        user_mbti = surprise_mbti()
        st.info(f"🎲 오늘의 랜덤 MBTI: **{user_mbti}**")

    mood = st.select_slider("무드 선택", options=["주말카페","데이트","면접/발표","페스티벌"], value="주말카페")
    show_confetti = st.toggle("화려한 효과 켜기 (🎈/❄️)", value=True)
    if st.button("🎲 Surprise me (다른 MBTI 랜덤)"):
        user_mbti = surprise_mbti()
        st.toast(f"랜덤으로 {user_mbti} 선택!", icon="✨")

# ============ 헤더 ============
st.markdown('<div class="gradient-title">MBTI 패션 추천</div>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">나의 성향으로 찾는 착붙 코디 — 팔레트, 무드별 코디, 이미지 무드보드까지 ✨</p>', unsafe_allow_html=True)
st.write("")

# ============ 본문 렌더 ============
valid = user_mbti in STYLE_DB

if not valid:
    st.warning("올바른 MBTI를 선택/입력해 주세요! 예) INFP, ESTJ, ENFP ...")
else:
    data = STYLE_DB[user_mbti]

    # 효과
    if show_confetti:
        st.balloons() if user_mbti in ["ENFP","ESFP","ENTP"] else st.snow()

    # 상단 카드
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown(f"""
        <div class="glass">
          <h2 style="margin-top:0">{user_mbti} · {data['title']}</h2>
          <p style="font-size:16px; margin-top:-6px">{data['desc']}</p>
          <div style="margin:8px 0">{palette_html(data['palette'])}</div>
          <div style="margin-top:8px">{chips(data['hashtags'])}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 🧩 무드 맞춤 코디")
        st.markdown(make_outfit(user_mbti, mood))

        st.markdown("#### ✅ 잘 어울려요")
        st.write("• 상의:", ", ".join(data["tops"]))
        st.write("• 하의:", ", ".join(data["bottoms"]))
        st.write("• 신발:", ", ".join(data["shoes"]))
        st.write("• 액세서리:", ", ".join(data["acc"]))

        st.markdown("#### 🛒 어디서 살까?")
        st.write("무신사 · W CONCEPT · 29CM · 지그재그 (키워드로 검색: ", ", ".join([h.replace("#","") for h in data["hashtags"]]), ")")

    with col2:
        st.markdown('<div class="glass"><h4 style="margin-top:0">📸 무드보드</h4>', unsafe_allow_html=True)
        st.image(data["images"][0], use_container_width=True)
        c21, c22 = st.columns(2)
        with c21:
            st.image(data["images"][1], use_container_width=True)
        with c22:
            st.image(data["images"][2], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 밑단: 스타일 믹스 실험실
    st.markdown("### 🧪 스타일 믹스 실험실")
    colA, colB, colC = st.columns([1,1,1])
    with colA:
        alt_mbti = st.selectbox("다른 MBTI와 섞어보기", MBTI, index=MBTI.index("ISTP"))
    with colB:
        intensity = st.slider("섞는 강도", 0, 100, 40, help="높을수록 대담한 믹스매치!")
    with colC:
        btn_mix = st.button("🎨 믹스 생성")

    if btn_mix:
        base = STYLE_DB[user_mbti]
        alt = STYLE_DB[alt_mbti]
        pick_top = random.choice(base["tops"] + alt["tops"])
        pick_bottom = random.choice(base["bottoms"] + alt["bottoms"])
        pick_shoes = random.choice(base["shoes"] + alt["shoes"])
        tip = "소재/패턴을 1개만 강조" if intensity < 50 else "패턴+컬러 투스텝 과감하게!"
        st.success(dedent(f"""
        **{user_mbti} × {alt_mbti} 믹스 결과**
        - 상의: **{pick_top}**
        - 하의: **{pick_bottom}**
        - 신발: **{pick_shoes}**
        - 팁: {tip}
        """))

    # 해시태그 복사용
    st.markdown("### 🔖 해시태그 복사용")
    tag_text = " ".join(data["hashtags"])
    st.code(tag_text, language="markdown")

# 푸터
st.markdown("---")
st.markdown(
    '<p style="text-align:center; opacity:0.7">© MBTI Fashionmate • have fun & wear what feels you 💖</p>',
    unsafe_allow_html=True
)
