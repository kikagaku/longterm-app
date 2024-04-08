"""
StreamlitとFastAPIを組み合わせたアプリケーションの例

FastAPIサーバをローカルで動かす場合は、main.py を実行してから、下記の設定でStreamlitを起動してください。
FASTAPI_SERVER = "http://127.0.0.1:8000"

既に、デプロイ済みのFastAPIサーバを使用する場合は、下記の設定でStreamlitを起動してください。
ASTAPI_SERVER = "https://longterm-firstapi.onrender.com"
"""

import streamlit as st
import pandas as pd
import requests
import json

FASTAPI_SERVER = "http://127.0.0.1:8000" # ロカールサーバで動かす場合
# FASTAPI_SERVER = "https://longterm-firstapi.onrender.com" # Rebderにデプロイしたものを使用する場合
url = f"{FASTAPI_SERVER}/make_predictions"

# ヘッダーの設定。サーバーにこのリクエストがJSON形式のボディを含んでいることを伝えます。
headers = {
    'Content-Type': 'application/json',
    'accept': 'application/json'
}

# サイドバー（入力画面）
st.sidebar.header('Input Features')

sepalLength = st.sidebar.slider('sepal length (cm)', min_value=0.0, max_value=10.0, step=0.1)
sepalWidth = 2.0
petalLength = st.sidebar.slider('petal length (cm)', min_value=0.0, max_value=10.0, step=0.1)
petalWidth = 1.0

# メインパネル
st.title('Iris Classifier')
st.write('## Input Value')

# インプットデータ（1行のデータフレーム）
columns=['sepal length (cm)', 'sepal width (cm)','petal length (cm)','petal width (cm)']
data = [[sepalLength, sepalWidth, petalLength, petalWidth]]
value_df = pd.DataFrame(data, columns=columns, index=['data'])
st.write(value_df)

data = {
    "sepal_length": sepalLength,
    "sepal_width": sepalWidth,
    "petal_length": petalLength,
    "petal_width":petalWidth
}

# 予測値のデータフレーム
response = requests.post(url, headers=headers, data=json.dumps(data))
# サーバーからのレスポンスを確認します。
if response.status_code == 200:
    # 成功した場合、予測結果を表示します。
    pred_probs = response.json()['prediction']
    # 数値のリストにするための前処理
    formatted_str = pred_probs.strip('[]')
    str_list = formatted_str.split()
    num_list = [float(num_str) for num_str in str_list]

    pred_df = pd.DataFrame([num_list], columns=['setosa','versicolor','virginica'],index=['probability'])
    st.write('## Prediction')
    st.write(pred_df)
else:
    # サーバーからエラーが返された場合、エラー情報を表示します。
    st.write("Failed to retrieve response. Status code: ", response.status_code)


# 予測結果の出力
name = pred_df.idxmax(axis=1).tolist()
st.write('## Result')
st.write('このアイリスはきっと',str(name[0]),'です!')