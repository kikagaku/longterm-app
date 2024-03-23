長期コースのFastAPIパートの内容を実際に実装して、デプロイしたものです。

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
- models
    - model_iris
- src
    - _main.py # 「FastAPI 基礎」で扱う内容 https://www.kikagaku.ai/learning/learn/longterm3/api-basic/fastapi-basic/
    - main.py # 「FastAPI 基礎」で扱う内容 https://www.kikagaku.ai/learning/learn/longterm3/api-basic/fastapi-iris/
    - model.py # アヤメの花から分類モデルを作成するコードを記載
- requirements.txt # 必要なライブラリを記載
- test_fastapi.py # 作成したAPIをテストするコードを記載
- gitignore # gitで管理しないファイルを記載