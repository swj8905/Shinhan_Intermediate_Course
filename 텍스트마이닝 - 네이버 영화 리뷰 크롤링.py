from bs4 import BeautifulSoup
import urllib.request as req

page_num = 1
prev_review = ""
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
        print(i)
    page_num += 1