import pandas as pd

df = pd.DataFrame({"날짜": ["2023-01-01", "2023/02/02", "20241224"]})
# errors="coerce": 변환 불가능한 값은 NaT처리
df["날짜"] = pd.to_datetime(df["날짜"], format="mixed", errors="coerce")
# print(df)

from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date, type(formatted_date))  # 2025-02-02 18:45:12

date_str = "2025-02-01"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
# print(date_obj, type(date_obj))  # datetime.datetime(2025, 2, 2, 0, 0)

df2 = pd.DataFrame({"date": ["2025-02-01", "2025-03-15", "2025-06-20"]})
df2["date"] = pd.to_datetime(df2["date"])  # datetime 타입 변환
df2["year"] = df2["date"].dt.year
df2["month"] = df2["date"].dt.month
df2["day"] = df2["date"].dt.day
df2["day_week"]=df2["date"].dt.day_of_week
# print(df2)

''' 
정렬
- ascending= True: 오름차순 정렬
- ascending=False: 내림차순 정렬
 '''
df3 = pd.DataFrame({
  "이름": ["철수", "영희", "민수", "수진"],
  "국어": [85, 90, 75, 95],
  "영어": [80, 70, 95, 85]
})


# 국어 점수 기준으로 오름차순 정렬
df3_sorted = df3.sort_values(by="국어")
# print(df3)
# print(df3_sorted)

# 인덱스 기준으로 정렬
df4 = df3.set_index("이름")
# 인덱스(이름) 기준 오름차순 정렬
df4_sorted = df3.sort_index()
# print(df4_sorted)
# 인덱스(이름) 기준 내림차순 정렬
df4_sorted_desc = df3.sort_index(ascending=False)
# print(df4_sorted_desc)
