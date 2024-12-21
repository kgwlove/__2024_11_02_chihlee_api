import streamlit as st

#手動建立counter_key,
if "counter" not in st.session_state:
    #st.session_state['counter'] = 0
    st.session_state.counter = 1

def increment_counter(*args):
   #st.session_state.counter += 1
   st.session_state.counter += args[0]
   st.session_state.counter -= args[1]

st.header(f"這個網頁已經執行{st.session_state.counter} 次")
st.button("再執行一次", key="reset",help='按下要加1', on_click=increment_counter,args=(5,3)) #自動建立reset_key
