長期コースのFastAPIパートの内容を実際に実装して、デプロイしたものです。

- FastAPI 基礎:https://www.kikagaku.ai/learning/learn/longterm3/api-basic/fastapi-basic/
- FastAPI 実践:https://www.kikagaku.ai/learning/learn/longterm3/api-basic/fastapi-iris/

# 使用手順
1. venv 等で、仮想環境を構築
なくてもよい。ただし、仮想環境を構築することを推奨
2. requirements.txtの中のライブラリをインストール
```
pip install -r requirements.txt
```
3. サーバーを起動
```
uvicorn src.main:app --reload 
```

# ディレクトリ構成
```
/
├── models
|  └──model_iris models.py で作成した分類モデル
|       
├── src/
|  └──_main.py 「FastAPI 基礎」で扱う内容
|  └──main.py 「FastAPI 実践」で扱う内容
|  └──model.py アヤメの花から分類モデルを作成するコードを記載
├── .gitignore .gitで管理しないファイルを記載
├── iris.csv アヤメの花のデータ
├── request_script.ps1
├── requirements.txt 必要なライブラリを記載
├── test_fastapi.ipynb 作成したAPIをテストするコードを記載
```