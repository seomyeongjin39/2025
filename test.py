import streamlit as st

st.set_page_config(page_title="지역별 추천 여행지", layout="wide")

st.title("🌸 한국 지역별 추천 여행지 🌸")
st.markdown("낭만적인 분위기와 함께 각 지역의 대표 여행지를 소개합니다!")

# 지역별 명소와 이미지
places = {
    "서울": {
        "한강공원": "https://upload.wikimedia.org/wikipedia/commons/3/38/Han_River_Seoul.jpg",
        "남산타워": "https://upload.wikimedia.org/wikipedia/commons/2/23/Namsan_Tower_in_Seoul.jpg",
        "경복궁": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Gyeongbokgung_Geunjeongjeon.jpg",
        "롯데월드": "https://upload.wikimedia.org/wikipedia/commons/4/48/Lotte_World.jpg",
        "광화문": "https://upload.wikimedia.org/wikipedia/commons/5/58/Gwanghwamun_Gate.jpg",
        "북촌한옥마을": "https://upload.wikimedia.org/wikipedia/commons/3/39/Bukchon_Hanok_Village.jpg",
        "동대문디자인플라자": "https://upload.wikimedia.org/wikipedia/commons/2/20/DDP_Seoul.jpg",
        "홍대거리": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Hongdae_Street.jpg",
        "청계천": "https://upload.wikimedia.org/wikipedia/commons/8/81/Cheonggyecheon_Seoul.jpg",
        "코엑스": "https://upload.wikimedia.org/wikipedia/commons/5/56/Coex_Seoul.jpg"
    },
    "광주": {
        "무등산": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Mudeungsan_Mountain.jpg",
        "국립아시아문화전당": "https://upload.wikimedia.org/wikipedia/commons/4/4d/ACC_Gwangju.jpg",
        "펭귄마을": "https://upload.wikimedia.org/wikipedia/commons/6/67/Penguin_Village_Gwangju.jpg",
        "충장로거리": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Chungjangro_Gwangju.jpg",
        "광주호수생태원": "https://upload.wikimedia.org/wikipedia/commons/5/59/Gwangju_Lake_Ecology_Park.jpg",
        "송정떡갈비거리": "https://upload.wikimedia.org/wikipedia/commons/7/70/Songjeong_Tteokgalbi.jpg",
        "양림동역사문화마을": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Yangnimdong_Culture_Village.jpg",
        "광주비엔날레관": "https://upload.wikimedia.org/wikipedia/commons/2/28/Gwangju_Biennale_Hall.jpg",
        "사직공원": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Sajik_Park_Gwangju.jpg",
        "광주FC월드컵경기장": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Gwangju_Worldcup_Stadium.jpg"
    }
}

# 선택 UI
region = st.selectbox("원하는 지역을 선택하세요:", list(places.keys()))

st.subheader(f"📍 {region}의 추천 명소")

for place, img_url in places[region].items():
    st.image(img_url, caption=place, use_column_width=True)
