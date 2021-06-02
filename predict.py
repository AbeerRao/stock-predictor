from sklearn.model_selection import train_test_split
import sklearn.svm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
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
sc = StandardScaler()
x_train[:, :] = sc.fit_transform(x_train[:, :])
x_test[:, :] = sc.transform(x_test[:, :])

classifer = sklearn.svm.SVC(kernel = 'rbf', random_state = 0)
classifer.fit(x_train, y_train)

# y_pred = classifer.predict(x_test)
# print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))
y_pred = classifer.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
ac = accuracy_score(y_test, y_pred)

print("Confusion matrix(class=0):", cm[0])
print("Confusion matrix(class=1):", cm[1])
print("Accuracy:", ac)