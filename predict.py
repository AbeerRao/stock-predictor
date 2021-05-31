from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

dataset = pd.read_json("data.json")
dataset = dataset.set_index(pd.DatetimeIndex(dataset['date'].values))
dataset.index.name = 'date'

dataset['price_up'] = np.where(dataset['close'].shift(-1) > dataset['close'], 1, 0)
dataset = dataset.drop(columns=['date'])

x = dataset.iloc[:, :dataset.shape[1]-1].values
y = dataset.iloc[:, dataset.shape[1]-1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

classifer = RandomForestClassifier(max_depth=10, random_state=0)
classifer.fit(x_train, y_train)

y_pred = classifer.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))