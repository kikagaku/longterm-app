"""
アヤメの花を分類するモデルを構築して保存
"""

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# データ準備
iris = datasets.load_iris()
features = pd.DataFrame(iris['data'], columns=iris['feature_names'])
target = iris['target']

# features と target を結合
df = pd.concat([features, pd.DataFrame(target)], axis=1, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target'])
df.to_csv('iris.csv', index=False)

# モデル構築
x_train, x_test, t_train, t_test = train_test_split(features, target, test_size=0.3, random_state=0)
model = RandomForestClassifier()
model.fit(x_train, t_train)
print(f'訓練データの accuracy: {model.score(x_train, t_train)}')
print(f'検証データの accuracy: {model.score(x_test, t_test):.2f}')

# モデルの保存
import pickle
pickle.dump(model, open('models/model_iris', 'wb'))
