from fastapi import FastAPI
# 追加：Pydentic から BaseModel をインポート
from pydantic import BaseModel

# FastAPI のインスタンス化
app = FastAPI()

# 追加：商品情報を表すクラス
class Item(BaseModel):
    name: str
    price: int

# ルートディレクトリへの GET で Hellp World の表示
@app.get("/")
def root():
    return  {"message": "Hello World"}

# item パスにアクセスし、商品情報を表示する
@app.get("/items/{item_id}")
def read_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}