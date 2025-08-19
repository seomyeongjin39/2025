import streamlit as st
import random

# 배경 스타일 적용 (밝고 분위기 있는 배경)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
[data-testid="stHeader"] { background: rgba(0,0,0,0); }
h1, h2, h3, p { color: black; text-shadow: 1px 1px 2px rgba(255,255,255,0.7); }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🌸 시간대별 낭만 데이트 코스 추천")
st.write("남은 시간이나 하루 일정에 맞춰 낭만적인 코스를 추천해 드려요 ✨")

# 사용자 입력
place = st.text_input("📍 가고 싶은 지역을 입력하세요:")
time_left = st.number_input("⏰ 남은 시간 (시간 단위):", min_value=1, max_value=12, step=1)
current_location = st.text_input("📍 현재 위치를 입력하세요 (예: 서울역, 광주역 등):")

# 감성 멘트
romantic_quotes = [
    "별빛이 내려앉는 순간, 당신의 이야기가 시작됩니다...",
    "오늘의 바람은 두 사람을 위한 멜로디 같아요.",
    "작은 골목도 당신과 함께라면 낭만이 되죠.",
    "시간마저 천천히 흐르는 듯한 순간을 준비했어요."
]

# 지역별 시간대 추천 데이터 (여러 코스 + duration + travel)
recommendations = {
    "서울": {
        "아침": [
            {"title": "북촌 한옥마을 산책", "desc": "고즈넉한 골목길에서 아침 산책", "image": "https://images.unsplash.com/photo-1572228360580-79800c35b2a0", "duration": 1, "travel": 15},
            {"title": "카페 브런치", "desc": "향긋한 커피와 브런치", "image": "https://images.unsplash.com/photo-1506086679524-5b2f7c1980fc", "duration": 1, "travel": 10},
            {"title": "창덕궁 후원 산책", "desc": "고궁의 아침을 느껴보세요", "image": "https://images.unsplash.com/photo-1534131213450-d4828e5fc66a", "duration": 1, "travel": 15}
        ],
        "점심": [
            {"title": "한강 피크닉", "desc": "도시를 바라보며 간단한 점심", "image": "https://images.unsplash.com/photo-1549921296-3b32d20bfa41", "duration": 1, "travel": 20},
            {"title": "명동 맛집 탐방", "desc": "쇼핑과 함께하는 점심", "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836", "duration": 1, "travel": 10}
        ],
        "저녁": [
            {"title": "남산 타워 야경", "desc": "도심 야경 감상", "image": "https://images.unsplash.com/photo-1568605114967-8130f3a36994", "duration": 1, "travel": 25},
            {"title": "한강 야경 드라이브", "desc": "밤바다와 조명 속 낭만", "image": "https://images.unsplash.com/photo-1505489304214-2956d54a5c9e", "duration": 1, "travel": 20}
        ]
    },
    "부산": {
        "아침": [
            {"title": "해운대 해변 산책", "desc": "바다 내음과 파도소리를 들으며 아침 산책", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e", "duration": 1, "travel": 10},
            {"title": "광안리 해변 카페", "desc": "바다를 바라보며 아침 커피", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e", "duration": 1, "travel": 10}
        ],
        "점심": [
            {"title": "자갈치 시장 맛집", "desc": "신선한 해산물 점심", "image": "https://images.unsplash.com/photo-1498575207493-7e3df0a92ce5", "duration": 1, "travel": 15},
            {"title": "부산 타워 전망", "desc": "도심 풍경과 점심 후 산책", "image": "https://images.unsplash.com/photo-1505489304214-2956d54a5c9e", "duration": 1, "travel": 10}
        ],
        "저녁": [
            {"title": "광안대교 야경 드라이브", "desc": "밤바다와 다리 불빛이 만드는 환상적인 풍경", "image": "https://images.unsplash.com/photo-1505489304214-2956d54a5c9e", "duration": 1, "travel": 20}
        ]
    },
    "제주": {
        "아침": [
            {"title": "성산일출봉 일출 감상", "desc": "새벽의 태양, 하루의 가장 낭만적인 시작", "image": "https://images.unsplash.com/photo-1526481280691-9069436fa76e", "duration": 1, "travel": 20},
            {"title": "한라산 산책", "desc": "청정 자연과 함께하는 아침", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e", "duration": 1, "travel": 30}
        ],
        "점심": [
            {"title": "오설록 티뮤지엄", "desc": "향긋한 차와 함께하는 여유로운 시간", "image": "https://images.unsplash.com/photo-1513542789411-b6a5d4f31634", "duration": 1, "travel": 15}
        ],
        "저녁": [
            {"title": "협재 해수욕장 산책", "desc": "해질녘 바닷가에서 즐기는 로맨틱한 시간", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e", "duration": 1, "travel": 20}
        ]
    }
    # 광주, 여수, 강릉, 대구 등도 동일하게 여러 코스 추가 가능
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
                st.write(f"🕒 예상 체류 시간: {spot['duration']}시간")
                st.write(f"🚶 이동 시간: {spot['travel']}분 (현재 위치: {current_location})")
                st.write("---")
                total_hours -= spot['duration']
        st.success(random.choice(romantic_quotes))
    else:
        st.warning("아직 준비되지 않은 지역이에요! 조금만 기다려주세요 🌙")
