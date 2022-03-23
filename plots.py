import streamlit as st
import pandas as pd
import plotly.express as px


st.text_input("Введите точки", key="points", value=0)
chart_data = pd.DataFrame(
    map(int, st.session_state.points.split(' ')),
    columns=['a'])

st.line_chart(chart_data)


st.text_input("Введите координаты через пробел, иксы от игреков отделите \";\"", key="cords", value="0 1 2 3 ;0 1 2 3")
axis1, axis2 = st.session_state.cords.split(';')
axis1 = list(map(int, axis1.strip(' ').split(' ')))
axis2 = list(map(int, axis2.strip(' ').split(' ')))
fig = px.scatter(x=axis1, y=axis2)
fig.show()

st.plotly_chart(fig, use_container_width=True)
