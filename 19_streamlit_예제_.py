import streamlit as st

st.text("일반 텍스트 입니다.")
st.text("파이썬 공부 중입니다.")
st.text("안녕하세요")

st.write("---")
st.write("# 이렇게 글자 크기를 키울 수 있습니다.")
st.write("## 이렇게 글자 크기를 키울 수 있습니다.")
st.write("### 이렇게 글자 크기를 키울 수 있습니다.")
st.write("#### 이렇게 글자 크기를 키울 수 있습니다.")
st.write("##### 이렇게 글자 크기를 키울 수 있습니다.")
st.write("###### 이렇게 글자 크기를 키울 수 있습니다.")
st.write("> 이런 것도 됩니다.")
st.write(">> 이런 것도 됩니다.")
st.write(">>> 이런 것도 됩니다.")
st.write(">>>> 이런 것도 됩니다.")
st.write("---")

st.write("https://www.naver.com")

foo = {"짜장면":5000, "짬뽕":6000, "탕수육":10000}
st.write(foo)
st.write("1 + 1 = ", 2)
st.code("print('hello world')")

"""
# 매직 커맨드

---

> 매직 커맨드

|      |  수학 점수    |    국어 점수   |
|------|:-------------:|:--------------:|
| 철수 |  90           |       80       |
| 영희 |  80           |       75       |

https://www.naver.com

```python
print("Hello World")
```
"""