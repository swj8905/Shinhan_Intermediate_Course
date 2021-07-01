import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score



def get_data_label(folder_name):
    def Normalize(i):
        return i / total
    files = glob.glob("./language/{}/*.txt".format(folder_name))  # 폴더 내 텍스트 파일 추출
    data = []
    label = []

    for fname in files:
        # 레이블 구하기
        basename = os.path.basename(fname)
        lang = basename.split("-")[0]

        # 텍스트 추출하기
        with open(fname, "r", encoding="utf-8") as f:
            text = f.read()
            text = text.lower()  # 소문자 변환

        # 알파벳 출현 빈도 구하기
        code_a = ord("a")
        code_z = ord("z")
        cnt = [0 for n in range(0, 26)]  # 26개의 0
        for char in text:
            code_current = ord(char)
            if code_a <= code_current <= code_z:
                cnt[code_current - code_a] += 1
        total = sum(cnt)
        cnt_norm = list(map(Normalize, cnt))
        # 리스트에 넣기
        label.append(lang)
        data.append(cnt_norm)
    return data, label


def show_me_the_graph(data, label):
    def Normalize(i):
        return i/total
    # 그래프 준비하기
    graph_dict = {}
    for i in range(0, len(data)):
        y = label[i]
        total = sum(data[i])
        x = list(map(Normalize, data[i]))
        if not (y in graph_dict):
            graph_dict[y] = x

    asclist = [[chr(n) for n in range(97, 97 + 26)]]
    df = pd.DataFrame(graph_dict, index=asclist)
    # 바그래프
    df.plot(kind='bar', subplots=True, ylim=(0, 0.15))
    plt.show()

# data, label 불러오기
train_data, train_label = get_data_label("train")
test_data, test_label = get_data_label("test")

# show_me_the_graph(train_data, train_label)

model = SVC()
model.fit(train_data, train_label)

result = model.predict(test_data)
score = accuracy_score(result, test_label)
print(score)

import pickle
f = open("./language_model.pkl", "wb")
pickle.dump(model, f)
f.close()
