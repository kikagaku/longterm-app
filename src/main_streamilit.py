import streamlit as st
import pandas as pd
import pickle

# 学習済みのモデルの読み込み
model = pickle.load(open('models/model_iris', 'rb'))

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

# 予測値のデータフレーム
pred_probs = model.predict_proba(value_df)
pred_df = pd.DataFrame(pred_probs,columns=['setosa','versicolor','virginica'],index=['probability'])

st.write('## Prediction')
st.write(pred_df)

# 予測結果の出力
name = pred_df.idxmax(axis=1).tolist()
st.write('## Result')
st.write('このアイリスはきっと',str(name[0]),'です!')