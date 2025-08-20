import streamlit as st

st.set_page_config(page_title="한국 여행지 추천", layout="wide")

st.title("🌸 낭만적인 여행지 추천 🌸")
st.markdown("분위기와 예산, 시간대에 맞춰 각 지역의 대표 여행지를 추천합니다!")

# ------------------ 지역별 명소 & 이미지 ------------------
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
    "부산": {
        "해운대 해수욕장": "https://upload.wikimedia.org/wikipedia/commons/5/55/Haeundae_Beach_Busan.jpg",
        "광안리 해수욕장": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Gwangalli_Beach_Busan.jpg",
        "자갈치시장": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Jagalchi_Market_Busan.jpg",
        "감천문화마을": "https://upload.wikimedia.org/wikipedia/commons/5/56/Gamcheon_Culture_Village_Busan.jpg",
        "태종대": "https://upload.wikimedia.org/wikipedia/commons/3/34/Taejongdae_Busan.jpg",
        "송정 해수욕장": "https://upload.wikimedia.org/wikipedia/commons/1/19/Songjeong_Beach_Busan.jpg",
        "동백섬 누리마루": "https://upload.wikimedia.org/wikipedia/commons/4/41/Dongbaekseom_Nurimaru.jpg",
        "부산시립미술관": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Busan_Museum_of_Art.jpg",
        "서면 번화가": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Seomyeon_Street_Busan.jpg",
        "영도대교 야경": "https://upload.wikimedia.org/wikipedia/commons/4/44/Yeongdo_Bridge_Busan.jpg"
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
    },
    "전주": {
        "전주한옥마을": "https://upload.wikimedia.org/wikipedia/commons/1/13/Jeonju_Hanok_Village.jpg",
        "경기전": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Gyeonggijeon_Jeonju.jpg",
        "남부시장 청년몰": "https://upload.wikimedia.org/wikipedia/commons/4/44/Nambu_Market_Jeonju.jpg",
        "덕진공원": "https://upload.wikimedia.org/wikipedia/commons/5/57/Deokjin_Park_Jeonju.jpg",
        "한벽당": "https://upload.wikimedia.org/wikipedia/commons/6/68/Hanbyeokdang_Jeonju.jpg",
        "오목대": "https://upload.wikimedia.org/wikipedia/commons/2/28/Omokdae_Jeonju.jpg",
        "전주수목원": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Jeonju_Botanical_Garden.jpg",
        "객사길 카페거리": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Jeonju_Cafe_Street.jpg",
        "전주향교": "https://upload.wikimedia.org/wikipedia/commons/3/35/Jeonju_Hyanggyo.jpg",
        "남천교": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Namcheon_Bridge_Jeonju.jpg"
    },
    # ... 강릉, 제주, 대구, 대전, 인천, 여수, 속초, 춘천 등 나머지 지역도 동일하게 추가 가능 ...
}

# ------------------ 사용자 선택 ------------------
region = st.selectbox("원하는 지역을 선택하세요:", list(places.keys()))

st.subheader(f"📍 {region}의 추천 명소")

for place, img_url in places[region].items():
    st.image(img_url, caption=place, use_container_width=True)
