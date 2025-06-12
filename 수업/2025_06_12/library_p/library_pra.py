# 오늘 날짜와 무작위 추천 과일 출력
import datetime, random
from collections import Counter, defaultdict

fruits = ['사과', '바나나', '포도', '딸기', '딸기', '바나나']
print("오늘 날짜:", datetime.date.today())
print("오늘의 추천 과일:", random.choice(fruits))

d = defaultdict(int)
d['나'] += 1
print(d)