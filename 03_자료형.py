# 리스트
a = [1,2,3,4,5, "hello", [1,2,3,4,5]]
print(a[0])
print(a[2])
a.append("world") # 원소 추가
print(a)
a.remove("hello") # 원소 삭제
del a[0] # 원소 삭제

# 튜플
a = (1,2,3,4, "hello", [1,2,3,4,5])
# a.append()
# a.remove()

# 딕셔너리
a = {"사과":100, "포도":200, "배":300}
print(a["사과"])
print(a["포도"])

# 불리언
a = True
a = False

# 집합형
a = set([1,2,2,2,3,3,3,3,4,4,4,4])
print(a)