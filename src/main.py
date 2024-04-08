"""
python main.py でFastAPIサーバを起動
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import uvicorn

# インスタンス化
app = FastAPI()

# 入力するデータ型の定義
class iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 学習済みのモデルの読み込み
model = pickle.load(open('models/model_iris', 'rb'))

# トップページ
@app.get('/')
async def index():
    return {"Iris": 'iris_prediction'}

# POST が送信された時（入力）と予測値（出力）の定義
@app.post('/make_predictions')
async def make_predictions(features: iris):
    # return({'prediction':str(model.predict([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])[0])})
    # 予測確率を返す場合は下記を使用
    return({'prediction':str(model.predict_proba([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])[0])})

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)