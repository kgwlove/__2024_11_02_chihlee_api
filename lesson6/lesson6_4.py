import streamlit as st
import tools

sitenames:list[str] = tools.get_sitenames(excel_name='aqi.xlsx')
#object notation
add_selectbox = st.sidebar.selectbox(  #提供站名選擇
    "請選擇站點名稱",
    sitenames
)


#執行方法:終端機輸入 $streamlit run lesson6_4.py
#https://docs.streamlit.io/develop/api-reference/layout/st.sidebar