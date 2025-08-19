import streamlit as st import random

지역별 장소 DB (10개 이상, 여러 장소)

places_db = { "서울": [ {"name": "한강공원", "type": "야외/피크닉", "budget": "저렴", "mood": "자유로움", "weather": "맑음", "img": "https://i.imgur.com/6Iej2cR.jpg"}, {"name": "롯데월드", "type": "테마파크", "budget": "높음", "mood": "활기참", "weather": "모든날씨", "img": "https://i.imgur.com/7Hf3fEd.jpg"}, {"name": "북촌 한옥마을", "type": "산책/전통", "budget": "중간", "mood": "잔잔", "weather": "맑음", "img": "https://i.imgur.com/tFOEHuS.jpg"}, ], "부산": [ {"name": "해운대 해수욕장", "type": "바다/휴양", "budget": "저렴", "mood": "시원", "weather": "맑음", "img": "https://i.imgur.com/m9tZ2cn.jpg"}, {"name": "광안대교 야경", "type": "야경", "budget": "중간", "mood": "로맨틱", "weather": "밤", "img": "https://i.imgur.com/JBY4S3g.jpg"}, {"name": "자갈치 시장", "type": "시장/먹거리", "budget": "저렴", "mood": "활기참", "weather": "모든날씨", "img": "https://i.imgur.com/FaF8sya.jpg"}, ], "대구": [ {"name": "동성로", "type": "쇼핑/데이트", "budget": "중간", "mood": "트렌디", "weather": "모든날씨", "img": "https://i.imgur.com/TIG5OAy.jpg"}, {"name": "이월드", "type": "놀이공원", "budget": "높음", "mood": "활기참", "weather": "모든날씨", "img": "https://i.imgur.com/4aOngRw.jpg"}, ], "인천": [ {"name": "차이나타운", "type": "먹거리/문화", "budget": "중간", "mood": "이색적", "weather": "맑음", "img": "https://i.imgur.com/1wBgVZa.jpg"}, {"name": "송도 센트럴파크", "type": "공원", "budget": "저렴", "mood": "자연", "weather": "맑음", "img": "https://i.imgur.com/s8frz9j.jpg"}, ], "강릉": [ {"name": "경포해수욕장", "type": "바다", "budget": "저렴", "mood": "힐링", "weather": "맑음", "img": "https://i.imgur.com/ZrF4Zzj.jpg"}, {"name": "안목 커피거리", "type": "카페", "budget": "중간", "mood": "잔잔", "weather": "맑음", "img": "https://i.imgur.com/2jT8kMl.jpg"}, ], "전주": [ {"name": "전주 한옥마을", "type": "산책/전통", "budget": "중간", "mood": "잔잔", "weather": "맑음", "img": "https://i.imgur.com/bmApGxk.jpg"}, {"name": "남부시장 청년몰", "type": "시장/먹거리", "budget": "저렴", "mood": "활기참", "weather": "모든날씨", "img": "https://i.imgur.com/9bhyDVm.jpg"}, ], "제주": [ {"name": "성산일출봉", "type": "자연/등산", "budget": "중간", "mood": "웅장", "weather": "맑음", "img": "https://i.imgur.com/fuPJKOm.jpg"}, {"name": "협재 해수욕장", "type": "바다", "budget": "저렴", "mood": "힐링", "weather": "맑음", "img": "https://i.imgur.com/zThK7se.jpg"}, {"name": "제주 올레길", "type": "산책/트래킹", "budget": "저렴", "mood": "자연", "weather": "맑음", "img": "https://i.imgur.com/wmWmjTH.jpg"}, ], "광주": [ {"name": "펭귄마을", "type": "산책/이색", "budget": "저렴", "mood": "유니크", "weather": "맑음", "img": "https://i.imgur.com/DHj6h5m.jpg"}, {"name": "충장로", "type": "쇼핑", "budget": "중간", "mood": "트렌디", "weather": "모든날씨", "img": "https://i.imgur.com/j2I7M2Q.jpg"}, ], "속초": [ {"name": "속초 중앙시장", "type": "시장/먹거리", "budget": "저렴", "mood": "활기참", "weather": "모든날씨", "img": "https://i.imgur.com/Yd6J7I0.jpg"}, {"name": "설악산", "type": "등산/자연", "budget": "중간", "mood": "웅장", "weather": "맑음", "img": "https://i.imgur.com/wsmXH0m.jpg"}, ], "대전": [ {"name": "한밭수목원", "type": "자연", "budget": "저렴", "mood": "잔잔", "weather": "맑음", "img": "https://i.imgur.com/gYr5F7p.jpg"}, {"name": "성심당", "type": "맛집", "budget": "중간", "mood": "행복", "weather": "모든날씨", "img": "https://i.imgur.com/tOB9XY2.jpg"}, ] }

st.title("🌟 맞춤형 놀거리 & 데이트 코스 추천기")

조건 입력

region = st.selectbox("지역을 선택하세요", list(places_db.keys())) weather = st.selectbox("날씨를 선택하세요", ["맑음", "비", "눈", "밤", "모든날씨"]) budget = st.selectbox("예산을 선택하세요", ["저렴", "중간", "높음"]) mood = st.selectbox("분위기를 선택하세요", ["잔잔", "활기참", "자유로움", "힐링", "로맨틱", "트렌디", "웅장", "유니크", "이색적", "행복"])

추천 필터링

filtered = [p for p in places_db[region] if (p["weather"] == weather or p["weather"] == "모든날씨") and p["budget"] == budget and p["mood"] == mood]

if not filtered: st.warning("조건에 딱 맞는 곳은 없지만 이런 곳 어때요?") filtered = random.sample(places_db[region], min(2, len(places_db[region])))

결과 보여주기

for place in filtered: st.subheader(f"✅ {place['name']}") st.image(place["img"], use_column_width=True) st.write(f"종류: {place['type']} | 예산: {place['budget']} | 분위기: {place['mood']}")

