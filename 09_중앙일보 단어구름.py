from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

keyword = input("키워드 입력 >> ")
encoded = par.quote(keyword)  # 한글 -> 특수한 문자

page_num = 1
output_total = ""
while True:
    url = "https://news.joins.com/Search/JoongangNews?page={}&Keyword={}&SortType=New&SearchCategoryType=JoongangNews".format(
        page_num, encoded)
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("h2.headline.mg > a")
    if len(title) == 0:  # 끝 페이지까지 크롤링 완료했으면?
        break
    for i in title:
        print("제목 :", i.text)
        print("링크 :", i.attrs["href"])
        print()
        code_news = req.urlopen(i.attrs["href"])
        soup_news = BeautifulSoup(code_news, "html.parser")
        content = soup_news.select_one("div#article_body")
        result = content.text.strip().replace("     ", " ").replace("   ", "")
        output_total += result
        print(result)

    if page_num == 1:
        break
    page_num += 1

print("형태소 분석 중입니다...")
# 형태소 분석 후 명사만 추출
from konlpy.tag import Okt
okt = Okt()
nouns_list = okt.nouns(output_total)
print(nouns_list)

print("불용어를 제거합니다...")
# 불용어 걸러주기
nouns_without_stopwords = []
for i in nouns_list:
    if len(i) != 1:
        nouns_without_stopwords.append(i)

print("명사들의 출현 빈도수를 카운트합니다...")
# 명사 빈도수 카운트
from collections import Counter
count_result = Counter(nouns_without_stopwords)
print(count_result)

# 이미지 가져오기
import numpy as np
from PIL import Image
image_array = np.array(Image.open("./image.jpg"))

# 이미지 색 뽑아오기
from wordcloud import ImageColorGenerator
image_color = ImageColorGenerator(image_array)

# 단어구름 만들기
from wordcloud import WordCloud
wc = WordCloud(font_path="./NanumMyeongjoBold.ttf", background_color="white", mask=image_array).generate_from_frequencies(count_result)

# 단어구름 띄우기
import matplotlib.pyplot as plt
plt.figure()
plt.imshow(wc.recolor(color_func=image_color), interpolation="bilinear")
plt.axis("off")
plt.show()