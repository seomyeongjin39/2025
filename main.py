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
    "ESFP": 
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
