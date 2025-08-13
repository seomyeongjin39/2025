import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 패션 추천", page_icon="👗", layout="centered")

# CSS 스타일 적용
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #FF69B4;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #888;
            margin-bottom: 30px;
        }
        .style-card {
            padding: 20px;
            border-radius: 15px;
            background-color: #FFF0F5;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        img {
            border-radius: 15px;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# MBTI 스타일 데이터
mbti_styles = {
    "ISTJ": {
        "style": "클래식하고 깔끔한 정장 스타일 👔",
        "desc": "모노톤 셔츠와 슬랙스로 단정하고 신뢰감 있는 이미지를 연출해보세요.",
        "img": "https://i.pinimg.com/564x/28/f4/24/28f424118a2e78f6e48b91c4a2f5230d.jpg"
    },
    "ENFP": {
        "style": "컬러풀하고 자유로운 스타일 🌈",
        "desc": "밝은 색 오버사이즈 셔츠와 청바지로 에너지를 뿜뿜!",
        "img": "https://i.pinimg.com/564x/78/1d/0c/781d0c85d016e8e889b3b55cccfb9876.jpg"
    },
    "INTP": {
        "style": "편안하지만 개성있는 패션 🧢",
        "desc": "그래픽 티셔츠와 후드티로 자유로운 분위기를 연출하세요.",
        "img": "https://i.pinimg.com/564x/18/8b/d0/188bd046e2c9d7a2af7553ef3fc7564b.jpg"
    },
    "ISFP": {
        "style": "자연스러운 보헤미안 스타일 🌿",
        "desc": "플로럴 원피스나 루즈핏 셔츠로 부드럽고 자유로운 감성을 표현해보세요.",
        "img": "https://i.pinimg.com/564x/09/f1/5a/09f15ab7fa11dba1384a9fdd2ff03dd7.jpg"
    },
    # 필요하면 다른 MBTI도 여기에 추가 가능
}

# 제목
st.markdown('<div class="title">👗 MBTI 패션 추천</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 MBTI에 어울리는 옷 스타일을 찾아드려요!</div>', unsafe_allow_html=True)

# MBTI 입력
user_mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INFP)").upper()

# 결과 출력
if user_mbti:
    if user_mbti in mbti_styles:
        style_info = mbti_styles[user_mbti]
        st.markdown(f"""
            <div class="style-card">
                <img src="{style_info['img']}" width="300">
                <h2>{style_info['style']}</h2>
                <p>{style_info['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("올바른 MBTI를 입력해주세요. (예: INFP, ENFP, ISFP...)")

