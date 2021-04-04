import pandas as pd 
import numpy as np 
import streamlit as st 


input=st.text_input('请输入：')

if input=='么么哒':
    '贼聪明'
    st.balloons()
elif input=='':
    st.write('')
else:
    '小沙雕，嘻嘻嘻~'


