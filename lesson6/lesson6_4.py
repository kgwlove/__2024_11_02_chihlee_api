import streamlit as st
import tools

sitenames:list[str] = tools.get_sitenames(excel_name='aqi.xlsx')

#object notation
#add_selectbox = st.sidebar.selectbox(  #提供站名選擇
#    "請選擇站點名稱",
#    sitenames
#)

#"with" notation

with st.sidebar: #下面建立的元件都會在sidebar區塊
    add_selectbox = st.selectbox(
        "請選擇站點名稱",
        sitenames
    )
    st.title(f"{add_selectbox}")

allData:list[dict] = tools.get_aqi(excel_name='aqi.xlsx')

#selected_item:list[dict]=[]
#for item in allData:
#    if item['sitename'] == add_selectbox:
#        selected_item.append(item)

selected_item:list[dict] = [item for item in allData if item['sitename'] == add_selectbox] #comprehension寫法
st.table(data=selected_item)

#執行方法:終端機輸入 $streamlit run lesson6_4.py
#https://docs.streamlit.io/develop/api-reference/layout/st.sidebar