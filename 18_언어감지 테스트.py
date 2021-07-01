import pickle

#Load from file
with open("./language_model.pkl", 'rb') as file:
    model = pickle.load(file)

def Normalize(i):
    return i / total

# test.txt의 알파벳 출현 빈도수 카운트
# 텍스트 추출하기
with open("./language/test.txt", encoding="utf-8") as f:
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

result = model.predict([cnt_norm])
print(result)


