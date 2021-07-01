from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import json
import os
import streamlit as st

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

okt = Okt()
tokenizer = Tokenizer(19417, oov_token = 'OOV')
with open('wordIndex.json') as json_file:
  word_index = json.load(json_file)
  tokenizer.word_index = word_index

loaded_model = load_model('best_model.h5')
def sentiment_predict(new_sentence):
    max_len = 30
    stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
    new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
    new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
    encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
    pad_new = pad_sequences(encoded, maxlen = max_len) # 패딩
    score = float(loaded_model.predict(pad_new)) # 예측
    return score


from bs4 import BeautifulSoup
import urllib.request as req

page_num = 1
prev_review = ""
emotion_result = {"매우긍정":0, "긍정":0, "중립":0, "부정":0, "매우부정":0}
while True:
    code = req.urlopen("https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=10106&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}".format(page_num))
    soup = BeautifulSoup(code, "html.parser")
    comment = soup.select("li > div.score_reple > p > span")
    if prev_review == comment[-1].text:
        break
    prev_review = comment[-1].text
    for i in comment:
        i = i.text.strip()
        if i == "관람객":
            continue
        # print(i)
        st.write(f"###### {i}")
        score = sentiment_predict(i)
        # print(score)
        if score >= 0.5:
            # print(f"{score*100:.2f}% 확률로 긍정입니다.")
            st.write(f"###### {score*100:.2f}% 확률로 __긍정__입니다.")
        else:
            # print(f"{100 - score * 100:.2f}% 확률로 부정입니다.")
            st.write(f"###### {100 - score * 100:.2f}% 확률로 __부정__입니다.")
        print("------------------------")
        if 0.8 <= score <= 1:
            emotion_result["매우긍정"] += 1
        elif 0.6 <= score < 0.8:
            emotion_result["긍정"] += 1
        elif 0.4 <= score < 0.6:
            emotion_result["중립"] += 1
        elif 0.2 <= score < 0.4:
            emotion_result["부정"] += 1
        elif 0 <= score < 0.2:
            emotion_result["매우부정"] += 1


    page_num += 1

