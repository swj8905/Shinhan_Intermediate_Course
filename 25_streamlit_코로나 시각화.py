import requests
import json

import streamlit as st
import pandas as pd
import pydeck as pdk
import math
from bs4 import BeautifulSoup
import urllib.request as req

def multipolygon_to_polygon(df):
    temp = pd.DataFrame()
    for idx, i in df.iterrows():
        if i[0] == "MultiPolygon":
            for polygon in i[1]:
                temp = temp.append(pd.DataFrame({"type":"MultiPolygon", "coordinates":[polygon], "CTP_KOR_NM":i[2]}))
        else:
            temp = temp.append(i)
    return temp.reset_index(drop=True)

st.title('코로나 확진자 맵')

# 코로나 정보 표시
code = req.urlopen("https://kosis.kr/covid/covid_index.do")
soup = BeautifulSoup(code, "html.parser")
text = soup.select("li > p.text")
number = soup.select("li > p.number")
increase = soup.select("li > p.increase")

f"""
|   {text[0].text}   |   {text[1].text}   |   {text[2].text}   |   {text[3].text}   |
|:--------:|:--------:|:--------:|:--------:|
|   {number[0].text}   |   {number[1].text}   |   {number[2].text}   |   {number[3].text}   |
|   {increase[0].text}   |   {increase[1].text}   |   {increase[2].text}   |   {increase[3].text}   |
"""


### 시도별 좌표값 데이터 가져오기
df = pd.read_json("./Si_Do_map_utf8.json")
df = multipolygon_to_polygon(df)

### 확진자 데이터 크롤링
send_data = {"statusGubun" : "confirm"}
data = requests.post("https://kosis.kr/covid/covid_getSidoMapData.do", data=send_data)
result = json.loads(data.text)
city_list = []
lat_list = []
lon_list = []
confirm_num_list = []
for i in result["resultSidoData"]:
    city = i["ovL1Kor"]
    if (city == "전체") or (city == "검역"):
        continue
    confirm_num = i["dtvalCo1"]
    df.loc[df["CTP_KOR_NM"]==city, "confirm_num"] = confirm_num

st.dataframe(df)
# 정규화
df["순위"] = df["confirm_num"].rank(method="dense", ascending=True)
df["정규화"] = df["순위"] / df["순위"].max()

layer = pdk.Layer(
    "PolygonLayer",
    df,
    get_polygon="coordinates",
    get_fill_color="[255*(1-정규화), 100*정규화, 255*정규화]",
    pickable=True,
    auto_highlight=True,
    get_elevation="confirm_num",
    elevation_scale=6,
    extruded=True
)

center = [36.33065076296566, 127.38850865111543]
view_state = pdk.ViewState(
    latitude=center[0],
    longitude=center[1],
    zoom=5.8,
    pitch=50
)
r = pdk.Deck(layers=[layer],
             map_style="light",
             initial_view_state=view_state,
             tooltip={"html":"도시: {CTP_KOR_NM}<br/>확진자: {confirm_num}",
                      "style":{"color":"white"}})

st.pydeck_chart(r)