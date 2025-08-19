import streamlit as st
import random

# 지역별 추천 장소
places = {
    "서울": ["경복궁", "남산타워", "롯데월드", "홍대거리", "한강공원"],
    "부산": ["해운대", "광안리", "자갈치시장", "태종대", "감천문화마을"],
    "여수": ["오동도", "향일암", "여수해상케이블카", "아쿠아플라넷", "돌산대교"],
    "강릉": ["경포대", "안목해변", "오죽헌", "강릉커피거리", "정동진"],
    "제주": ["성산일출봉", "한라산", "협재해수욕장", "우도", "천지연폭포"],
    "대구": ["팔공산", "서문시장", "동성로", "수성못", "이월드"],
    "광주": ["무등산", "양림동역사마을", "펭귄마을", "충장로", "광주호"],
    "인천": ["차이나타운", "월미도", "송도센트럴파크", "을왕리해수욕장", "송월동 동화마을"],
    "수원": ["화성행궁", "광교호수공원", "수원통닭거리", "AK플라자", "수원야경투어"],
    "속초": ["속초중앙시장", "설악산", "영금정", "대포항", "속초해수욕장"]
}

# 지역별 이미지
images = {
    "서울": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Namsan_Seoul_Tower_2019.jpg",
    "부산": "https://upload.wikimedia.org/wikipedia/commons/0/08/Gwangalli_Bridge_Busan_South_Korea.jpg",
    "여수": "https://upload.wikimedia.org/wikipedia/commons/f/f1/Odongdo_Island_in_Yeosu_2019.jpg",
    "강릉": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Gyeongpo_Beach_2018.jpg",
    "제주": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Seongsan_Ilchulbong_sunrise_jeju.jpg",
    "대구": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Dalseong.jpg",
    "광주": "https://upload.wikimedia.org/wikipedia/commons/1/14/Gwangju_Skyline.jpg",
    "인천": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Incheon_Skyline.jpg",
    "수원": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Suwon_Hwaseong_Fortress.jpg",
    "속초": "https://upload.wikimedia.org/wikipedia/commons/5/56/Seoraksan_National_Park.jpg"
}

# 옵션 데이터
weather_options = ["맑음", "흐림", "비", "눈"]
time_options = ["아침", "점심", "저녁", "밤"]
budget_options = ["저렴", "적당", "플렉스"]
mood_options = ["로맨틱", "힐링", "활동적", "먹거리"]

st.title("🎡 조건 맞춤 데이트/놀거리 추천 앱 🎡")
st.write("지역, 날씨, 시간, 예산, 분위기 조건에 맞춰 추천해드려요!")

# 사용자 입력
region = st.selectbox("📍 지역 선택", list(places.keys()))
weather = st.selectbox("🌤️ 날씨 선택", weather_options)
time_of_day = st.selectbox("🕒 시간대 선택", time_options)
budget = st.selectbox("💰 예산 선택", budget_options)
mood = st.selectbox("💖 분위기 선택", mood_options)

# 추천 버튼
if st.button("추천 받기 ✨"):
    recommended_place = random.choice(places[region])
    st.subheader(f"🌍 {region} 추천 장소")
    st.write(f"➡️ 장소: **{recommended_place}**")
    st.write(f"➡️ 날씨: {weather}, 시간: {time_of_day}, 예산: {budget}, 분위기: {mood}")
    st.image(images[region], use_column_width=True)
