from konlpy.tag import Okt

okt = Okt()
result = okt.pos("이런 것도 되나욬ㅋㅋㅋㅋㅋㅋㅋㅋ")
print(result)
result = okt.nouns("파이썬을 공부 중입니다.")
print(result)