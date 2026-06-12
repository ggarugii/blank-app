import streamlit as st

# 웹 페이지 제목 설정
st.title("🌡️ 온·습도 모니터링 시스템")
st.write("온도와 습도를 입력하면 정상 여부를 자동으로 판별합니다.")

# 구분선
st.divider()

# 1. 입력 영역 (기존의 input 영역을 스트림릿 위젯으로 대체)
st.subheader("📊 데이터 입력")

# 스텝(step=1)을 지정하여 정수형(int) 입력 유도
온도 = st.number_input("온도를 입력하세요 (℃):", value=36, step=1)
습도 = st.number_input("습도를 입력하세요 (%):", value=80, step=1)

st.divider()

# 2. 출력 및 로직 영역 (기존의 if-else 및 print 영역을 스트림릿 화면 출력으로 대체)
st.subheader("🔍 판정 결과")

# 온도 판정 로직
if 35 <= 온도 <= 39:
    st.success(f"✅ 온도 정상 (현재 온도: {온도}℃)")
else:
    st.error(f"🚨 온도 경고 (현재 온도: {온도}℃ - 정상 범위: 35~39℃)")

# 습도 판정 로직
if 70 <= 습도 <= 90:
    st.success(f"✅ 습도 정상 (현재 습도: {습도}%)")
else:
    st.error(f"🚨 습도 경고 (현재 습도: {습도}% - 정상 범위: 70~90%)")