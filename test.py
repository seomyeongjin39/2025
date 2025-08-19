import streamlit as st
import random

# 배경 스타일 적용 (가독성 높이기)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    filter: brightness(50%) blur(1px);
}
[data-testid="stHeader"] { background: rgba(0,0,0,0); }
h1, h2, h3, p { color: white; text-shadow: 2px 2px 5px rgba(0,0,0,0.7); }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🌸 시간대별 낭만 데이트 코스 추천")
st.write("남은 시간이나 하루 일정에 맞춰 낭만적인 코스를 추천해 드려요 ✨")

# 사용자 입력
place = st.text_input("📍 가고 싶은 지역을 입력하세요:")
time_left = st.number_input("⏰ 남은 시간 (시간 단위):", min_value=1, max_value=12, step=1)

# 감성 멘트
romantic_quotes = [
    "별빛이 내려앉는 순간, 당신의 이야기가 시작됩니다...",
    "오늘의 바람은 두 사람을 위한 멜로디 같아요.",
    "작은 골목도 당신과 함께라면 낭만이 되죠.",
    "시간마저 천천히 흐르는 듯한 순간을 준비했어요."
]

# 시간대별 추천 데이터 (모든 주요 지역 포함)
recommendations = {
    "서울": {
        "아침": [{"title": "북촌 한옥마을 산책", "desc": "고즈넉한 골목길에서 아침 산책", "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c"},
                   {"title": "카페 브런치", "desc": "향긋한 커피와 브런치", "image": "https://images.unsplash.com/photo-1529692236671-f1b06e8e5aa0"}],
        "점심": [{"title": "한강 피크닉", "desc": "도시를 바라보며 간단한 점심", "image": "https://images.unsplash.com/photo-1505761671935-60b3a7427bad"}],
        "저녁": [{"title": "남산 타워 야경", "desc": "도심 야경 감상", "image": "https://images.unsplash.com/photo-1505489304214-2956d54a5c9e"}]
    },
    "부산": {
        "아침": [{"title": "해운대 해변 산책", "desc": "바다 내음과 파도소리를 들으며 아침 산책", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"}],
        "점심": [{"title": "광안리 맛집", "desc": "바다를 바라보며 즐기는 점심", "image": "https://images.unsplash.com/photo-1498575207493-7e3df0a92ce5"}],
        "저녁": [{"title": "광안대교 야경 드라이브", "desc": "밤바다와 다리 불빛이 만드는 환상적인 풍경", "image": "https://images.unsplash.com/photo-1505489304214-2956d54a5c9e"}]
    },
    "제주": {
        "아침": [{"title": "성산일출봉 일출 감상", "desc": "새벽의 태양, 하루의 가장 낭만적인 시작", "image": "https://images.unsplash.com/photo-1526481280691-9069436fa76e"}],
        "점심": [{"title": "오설록 티뮤지엄", "desc": "향긋한 차와 함께하는 여유로운 시간", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"}],
        "저녁": [{"title": "협재 해수욕장 산책", "desc": "해질녘 바닷가에서 즐기는 로맨틱한 시간", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"}]
    },
    "광주": {
        "아침": [{"title": "펭귄마을 산책", "desc": "감각적인 벽화와 아기자기한 골목길", "image": "https://images.unsplash.com/photo-1501785888041-af3ef285b470"}],
        "점심": [{"title": "국립아시아문화전당 방문", "desc": "문화와 예술 속에서 즐기는 점심", "image": "https://images.unsplash.com/photo-1529119368496-2dfda6ec2804"}],
        "저녁": [{"title": "광주 밤거리 산책", "desc": "도심 속 밤하늘과 함께 걷는 낭만", "image": "https://images.unsplash.com/photo-1529119368496-2dfda6ec2804"}]
    },
    "여수": {
        "아침": [{"title": "여수 아침 바다 산책", "desc": "조용한 바닷가에서 즐기는 산책", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"}],
        "점심": [{"title": "오동도 동백꽃길", "desc": "꽃향기 가득한 길 위에서 즐기는 점심", "image": "https://images.unsplash.com/photo-1481833761820-0509d3217039"}],
        "저녁": [{"title": "여수 밤바다 산책", "desc": "노래 속 그 바다를 함께 걷는 낭만적인 순간", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"}]
    },
    "강릉": {
        "아침": [{"title": "안목해변 카페거리", "desc": "파도소리를 들으며 커피 한 잔", "image": "https://images.unsplash.com/photo-1493558103817-58b2924bce98"}],
        "점심": [{"title": "경포대 주변 산책", "desc": "수평선 너머 풍경과 함께 즐기는 점심", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"}],
        "저녁": [{"title": "경포대 일출/야경", "desc": "아름다운 하늘과 바다를 함께 감상", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"}]
    },
    "대구": {
        "아침": [{"title": "앞산 전망대 산책", "desc": "도심을 내려다보며 아침 운동", "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e"}],
        "점심": [{"title": "동성로 맛집 탐방", "desc": "쇼핑과 함께 즐기는 점심", "image": "https://images.unsplash.com/photo-1549692520-acc6669e2f0c"}],
        "저녁": [{"title": "앞산 야경 감상", "desc": "도심 야경과 함께하는 낭만적인 시간", "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e"}]
    }
}

# 추천 출력
if place:
    if place in recommendations:
        st.subheader(f"✨ {place} 시간대별 추천 코스 ✨")
        total_hours = time_left
        for period, spots in recommendations[place].items():
            if total_hours <= 0:
                break
            st.markdown(f"### {period}")
            for spot in spots:
                if total_hours <= 0:
                    break
                st.image(spot["image"], use_column_width=True)
                st.markdown(f"**{spot['title']}**")
                st.write(spot['desc'])
                st.write("---")
                total_hours -= 1  # 각 코스 1시간 가정
        st.success(random.choice(romantic_quotes))
    else:
        st.warning("아직 준비되지 않은 지역이에요! 조금만 기다려주세요 🌙")
