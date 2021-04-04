import pandas as pd 
import numpy as np 
import streamlit as st 
import time,random

sign_word_list=['啊?', '哈?!', '咦?~', '喵喵喵！', 'what？', '嘤嘤嘤~','天啦撸！']

input=st.text_input('请输入进入密码：')

if input=='么么哒':
    st.success('贼聪明！进入下一关')

    x=st.slider('请给我打分：')
    if x<90:
        st.warning(random.choice(sign_word_list))
    elif 90<x<100:
        st.info('嘻嘻')
        time.sleep(2)
        st.warning('但还是不对哦！')
    else:
        st.success('恭喜答对啦！')
        st.balloons()





