from tools import taipei
import streamlit as st

@st.dialog("目前網路出現狀況")
def vote(error):
    st.write(error)

try: #用try來接收tools.py內function的錯誤
    youbike_data:list[dict] = taipei.get_youbikes()
except Exception as error:
    vote(error)
    st.write("喝杯咖啡!請等一下再試")
    st.stop()
else:        
    st.table(youbike_data)