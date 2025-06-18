'''
Q1. 다음 중 xticks() 함수의 주된 용도는 무엇인가요?
답: B
A. 데이터프레임의 인덱스를 바꾸는 함수
B. x축 눈금의 위치나 라벨을 조정하는 함수
C. 막대의 높이를 자동 조정하는 함수
D. 그래프에 범례를 추가하는 함수

Q2. 다음 중 plt.grid(True, linestyle='--')의 효과로 옳은 것은?
답:B
A. y축 눈금을 회색으로 만든다
B. 플롯에 점선을 배경으로 추가한다
C. 그래프의 테두리를 제거한다
D. 그래프의 배경색을 노란색으로 바꾼다

Q3. 다음 중 plt.legend(loc='upper right')에 대한 설명으로 옳지 않은 것은?
답: C
A. 범례를 오른쪽 위에 표시한다
B. `loc`은 범례의 위치를 지정하는 인자이다
C. 이 함수는 scatter plot에서만 사용된다
D. `legend()`는 plot의 범주 이름을 보여준다

'''
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import pandas as pd

'''
컬럼 명
'survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
'alive', 'alone'
'''  
titanic = sns.load_dataset('titanic')
sex_count = titanic['sex'].value_counts()

def get_gender_colors(labels):
  color_map = {'female': 'pink', 'male': 'blue'}
  return [color_map.get(label, 'gray') for label in labels]

def get_gender_names(labels, name_map=None):
  if name_map is None:
    name_map = {'female': '여자', 'male': '남자'}
  return [name_map.get(label, label) for label in labels]
# 문제 1
colors = get_gender_colors(sex_count.index)
names = get_gender_names(sex_count.index)
plt.bar(sex_count.index, sex_count.values, color=colors, label=names)
plt.xticks(ticks=range(len(names)), labels=names)
plt.title('성별 기준 인원 수')
plt.legend()
plt.xlabel('성별')
plt.ylabel('Count')
# plt.show()
# 문제2
plt.clf() # 초기화
arrive_p = titanic.groupby('pclass')['survived'].sum()
plt.plot(arrive_p.index, arrive_p.values, marker='o', label='생존자 수')
plt.title('객실별 생존자 수')
plt.xlabel('객실 등급')
plt.ylabel('생존자 수')
plt.legend(loc='upper right')
# plt.show()
# 문제3
plt.clf()
plt.scatter(titanic['age'], titanic['fare'], alpha=0.3)
plt.title('나이 별 요금 그래프')
plt.grid(color='gray', linestyle='--')
# plt.show()
# 문제4
plt.clf()
# 정렬버전
# embarked_p = titanic['embarked'].value_counts().sort_values()
# 기본버전
embarked_p = titanic['embarked'].value_counts()
plt.barh(embarked_p.index, embarked_p.values)
# plt.show()
# 문제5 평균 나이와 평균 요금
mean_age_fare = titanic.groupby('pclass')[["age","fare"]].mean()

plt.clf()

fig, ax = plt.subplots(figsize=(8,5))
ax.patch.set_facecolor('#a5e6b6')

ax.plot(mean_age_fare.index, mean_age_fare["age"], marker="^", label="평균 나이")
ax.plot(mean_age_fare.index, mean_age_fare["fare"], marker="o", label="평균 요금")
ax.set_title("객실 등급별 평균 나이와 평균 요금")
ax.set_xlabel("객실 등급 (pclass)")
ax.set_ylabel("값")
ax.legend()
plt.tight_layout()
plt.show()
