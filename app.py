import random
import streamlit as st

# 웹앱 제목 및 설명
st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천기")
st.write("아래 버튼을 누르면 오늘의 점심 메뉴를 랜덤으로 추천해 드립니다!")

# 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정할 수 있습니다)
lunch_menus = [
    "김치찌개",
    "돈까스",
    "제육볶음",
    "초밥",
    "파스타",
    "햄버거",
    "쌀국수",
    "떡볶이",
    "비빔밥",
    "짜장면",
    "순대국밥",
    "샌드위치",
]

# 버튼을 눌렀을 때 실행될 코드
if st.button("오늘의 점심 추천받기 🎲"):
    selected_menu = random.choice(lunch_menus)
    st.success(f"오늘의 추천 메뉴는 **{selected_menu}**입니다!")
    st.balloons()  # 축하 풍선 효과
