import streamlit as st

length = st.slider('슬라이더', 1, 100, 50)      # ('제목', 최솟값, 최댓값, 초기값)
st.text(length)