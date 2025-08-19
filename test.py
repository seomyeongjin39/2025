import streamlit as st
import random

# --- 배경 이미지 CSS ---
page_bg_img = """
<style>
body {
background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1470&q=80");
background-size: cover;
}
.stApp {
background-color: rgba(255,255,255,0.85);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("🎡 조건 맞춤 데이트/놀거리 추천 앱 🎡")
st.write("지역, 날씨, 시간, 예산, 분위기에 맞춰 추천해드려요!")

# --- 지역별 장소 ---
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

# --- 장소별 이미지 ---
place_images = {
    "경복궁": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Gyeongbokgung_Gate.jpg",
    "남산타워": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Namsan_Seoul_Tower_2019.jpg",
    "롯데월드": "https://upload.wikimedia.org/wikipedia/commons/3/35/Lotte_World_Tower_%28Seoul%29.jpg",
    "홍대거리": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Hongdae_Street_Seoul.jpg",
    "한강공원": "https://upload.wikimedia.org/wikipedia/commons/1/11/Hangang_River_Seoul.jpg",
    "해운대": "https://upload.wikimedia.org/wikipedia/commons/0/08/Gwangalli_Bridge_Busan_South_Korea.jpg",
    "광안리": "https://upload.wikimedia.org/wikipedia/commons/0/08/Gwangalli_Bridge_Busan_South_Korea.jpg",
    "자갈치시장": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Jagalchi_Market_Busan.jpg",
    "태종대": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Taejongdae_Busan.jpg",
    "감천문화마을": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Gamcheon_Culture_Village.jpg",
    "오동도": "https://upload.wikimedia.org/wikipedia/commons/f/f1/Odongdo_Island_in_Yeosu_2019.jpg",
    "향일암": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Hyangiram_yeosu.jpg",
    "여수해상케이블카": "https://upload.wikimedia.org/wikipedia/commons/4/49/Yeosu_cable_car.jpg",
    "아쿠아플라넷": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Aquaplanet_Yeosu.jpg",
    "돌산대교": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Dolsan_Bridge_Yeosu.jpg",
    "경포대": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Gyeongpo_Beach_2018.jpg",
    "안목해변": "https://upload.wikimedia.org/wikipedia/commons/3/36/Anmok_Beach.jpg",
    "오죽헌": "https://upload.wikimedia.org/wikipedia/commons/9/95/Ojukheon_Gangneung.jpg",
    "강릉커피거리": "https://upload.wikimedia.org/wikipedia/commons/4/44/Gangneung_coffee_street
