import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

train = pd.read_csv("./mnist/train.csv")
test = pd.read_csv("./mnist/t10k.csv")

train_data = train.iloc[:, 1:]
train_label = train.iloc[:, 0]
test_data = test.iloc[:, 1:]
test_label = test.iloc[:, 0]

model = SVC()
model.fit(train_data, train_label)

result = model.predict(test_data)
score = accuracy_score(result, test_label)
print(score)

# 학습한 모델 저장
import pickle
f = open("./mnist_model.pkl", "wb")
pickle.dump(model, f)
f.close()