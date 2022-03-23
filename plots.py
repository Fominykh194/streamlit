import streamlit as st
import pandas as pd


st.text_input("Введите точки", key="points", value=0)
chart_data = pd.DataFrame(
    map(int, st.session_state.points.split(' ')),
    columns=['a'])

st.line_chart(chart_data)
