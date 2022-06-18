import streamlit as st

st.title('AI Reporter')
st.text_input('키워드')
st.slider('문장 길이', 2, 30, 7)