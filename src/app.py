import streamlit as st
from random import randint
import requests
import json

st.title('APIテスト画面（ユーザー）')

with st.form(key='user'):
    # user_id: int = randint(0, 10)
    user_name: str = st.text_input('ユーザー名',max_chars=12)
    data = {
        # 'user_id': user_id,
        'user_name':user_name,
    }
    submit_button = st.form_submit_button(label='送信')
    
if submit_button:
    st.write('## 送信データ')
    st.json(data)
    st.write('##レスポンス結果')
    url = 'http://127.0.0.1:8000/users'
    res = requests.post(
        url,
        data=json.dumps(data)
    )
    if res.status_code == 200:
        st.success('ユーザー登録完了')
    st.write(res.status_code)
    st.json(res.json())