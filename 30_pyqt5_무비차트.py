from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic
import os
import urllib.request as req
from bs4 import BeautifulSoup

os.environ["QT_MAC_WANTS_LAYER"] = "1" # 맥 쓰시는 분들만!

ui_file = "./movie_chart.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)

        self.button.clicked.connect(self.crawling_movie_chart)

    def crawling_movie_chart(self):
        code = req.urlopen("http://www.cgv.co.kr/movies/")
        soup = BeautifulSoup(code, "html.parser")
        img = soup.select("span.thumb-image > img")
        title = soup.select("div.sect-movie-chart strong.title")
        for i in range(len(title)):
            # 영화제목 띄우기
            getattr(self, f"text{i+1}").setText(f"{i+1}위. {title[i].string}")
            # 포스터 이미지 띄우기
            img_url = img[i].attrs["src"]
            data = req.urlopen(img_url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            pixmap = pixmap.scaled(185, 260)
            getattr(self, f"img{i+1}").setPixmap(pixmap)



QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())