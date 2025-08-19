import streamlit as st
import random

# 배경 스타일 적용
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0');
    background-size: cover;
    background-position: center;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.title("🌸 낭만적인 여행/데이트 코스 추천")
st.write("입력한 장소를 중심으로, 당신만의 특별한 순간을 만들어 드려요 ✨")

# 사용자 입력
place = st.text_input("📍 가고 싶은 지역을 입력하세요:")
theme = st.selectbox("🎨 원하는 분위기를 선택하세요:", ["낭만적인", "재미있는", "힐링", "특별한 날"])

# 감성 멘트
romantic_quotes = [
    "별빛이 내려앉는 순간, 당신의 이야기가 시작됩니다...",
    "오늘의 바람은 두 사람을 위한 멜로디 같아요.",
    "작은 골목도 당신과 함께라면 낭만이 되죠.",
    "시간마저 천천히 흐르는 듯한 순간을 준비했어요."
]

# 예시 추천 데이터 (지역별 낭만 코스)
recommendations = {
    "서울": [
        ("남산 타워 야경", "도시 전체가 별빛처럼 반짝이는 곳 🌃"),
        ("석촌호수 산책", "잔잔한 물결과 함께하는 감성 데이트 🌸"),
        ("북촌 한옥마을", "고즈넉한 분위기 속에서 함께 걷는 낭만 ✨")
    ],
    "부산": [
        ("광안대교 야경", "바다 위 반짝이는 불빛과 함께 💫"),
        ("해운대 바닷가", "파도 소리에 마음을 맡기는 시간 🌊"),
        ("감천문화마을", "알록달록 예쁜 골목에서 인생샷 📸")
    ],
    "제주": [
        ("성산일출봉", "새벽의 햇살이 두 사람을 비추는 순간 🌅"),
        ("협재 해수욕장", "맑은 바다와 하얀 모래 위를 함께 🏖️"),
        ("오설록 티뮤지엄", "향긋한 차 향기와 함께하는 여유로운 시간 🍵")
    ]
}

if place:
    st.subheader(f"✨ {place} 추천 코스 ✨")
    if place in recommendations:
        for spot, desc in recommendations[place]:
            st.image("https://source.unsplash.com/800x500/?romantic,night,travel", use_column_width=True)
            st.markdown(f"### {spot}")
            st.write(desc)
            st.write("---")
        st.success(random.choice(romantic_quotes))
    else:
        st.warning("아직 준비되지 않은 지역이에요! 조금만 기다려주세요 🌙")

