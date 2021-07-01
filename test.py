import urllib.request as req
from bs4 import BeautifulSoup

header = req.Request("http://www.cgv.co.kr/movies/", headers={"User-Agent": "Mozilla/5.0"})
code = req.urlopen(header)
soup = BeautifulSoup(code, "html.parser")
title = soup.select("strong.title")

token = ""
id = ""
bot = telepot.Bot(token)

for i in title:
    print(i.text)
    bot.sendMessage(chat_id=id, text=i.text)