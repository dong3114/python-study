'''
## Seaborn 및 matplotlib 종합 퀴즈
**문제 1.** `object` 타입의 날짜 문자열 컬럼(`df['date']`)을 시계열 분석을 위해 `datetime` 타입으로 변환하는 가장 올바른 코드는 무엇일까요?
답: 2번
① `df['date'] = df['date'].to_date()`
② `df['date'] = pd.to_datetime(df['date'])`
③ `df['date'] = pd.datetime(df['date'])`
④ `df['date'].apply(lambda x: datetime(x))`

**문제 2.** 특정 변수의 데이터 분포(어떤 값에 데이터가 몰려 있는지)를 시각적으로 확인할 때 가장 적합한 그래프 유형은 무엇일까요?
답: 3번
① `plt.plot()` (선 그래프)
② `sns.barplot()` (막대 그래프)
③ `sns.histplot()` (히스토그램)
④ `plt.pie()` (파이 차트)

**문제 3.** 데이터프레임 `df`의 모든 수치형 변수 간의 상관관계를 계산하고 이를 히트맵으로 시각화하는 코드로 가장 적절한 것은 무엇일까요?
답: 4번
① `sns.histplot(df.corr())`
② `sns.heatmap(df.groupby().corr())`
③ `plt.plot(df.corr())`
④ `sns.heatmap(df.corr(numeric_only=True), annot=True)`

**문제 4.** 요일별 평균 따릉이 대여량을 계산하는 코드로 가장 올바른 것은 무엇일까요?
답: 2번
① `df.filter(by='weekday')['rental_count'].mean()`
② `df.groupby('weekday')['rental_count'].agg('mean')`
③ `df.pivot_table(index='rental_count', columns='weekday', aggfunc='mean')`
④ `df['rental_count'].value_counts(by='weekday')`

**문제 5.** `matplotlib`으로 그래프를 그린 후, 그래프의 제목을 'Hourly Average Rentals'로 설정하는 코드는 무엇일까요?
답: 1번
① `plt.title('Hourly Average Rentals')`
② `plt.xlabel('Hourly Average Rentals')`
③ `plt.legend('Hourly Average Rentals')`
④ `plt.figure(title='Hourly Average Rentals')`

'''
import seaborn as sns
import pandas as pd
import matplotlib.pylab as plt
import koreanize_matplotlib

bike = pd.read_csv('수업/2025_06/2025_06_18/utils/bike_2412.csv', encoding='cp949')

# 문제1
# groupby() 사용해 hour 컬럼을 기준으로 그룹화, rental_count의 평균 계산 (hour_rentals)
# 1. 대여일시의 오브젝트 타입 datetime으로 변경
bike['대여일시'] = pd.to_datetime(bike['대여일시'])
# 2. hour 컬럼 생성
bike['hour'] = bike['대여일시'].dt.hour
bike['date'] = bike['대여일시'].dt.date
# 3. 날짜별 대여수 시리즈 생성
rental_counts = bike.groupby(['hour', 'date'])['이용시간(분)'].count().rename('rental_count').reset_index()
avg_duration = bike.groupby(['hour', 'date'])['이용시간(분)'].mean().rename('avg_duration').reset_index()
# 4. 시리즈 merge (pk =시간)
hour_stats = pd.merge(rental_counts, avg_duration, on=['hour', 'date'])

# 시간만으로 구분
rc = bike.groupby('hour')['이용시간(분)'].count().rename('rc').reset_index()
ad = bike.groupby('hour')['이용시간(분)'].mean().rename('ad').reset_index()
hs = pd.merge(rc, ad, on='hour')
# print(hs)
# seaborn을 사용해서 시간대별 대여량 시각화 하기
# x축: 시간 y축: 평균 대여량
sns.barplot(x='hour', y='ad', data=hs)
# 5. 제목 및 x,y축 라벨 네이밍
plt.title("Hourly Average Rentals")
plt.xlabel("Hour of Day")
plt.ylabel("Average Rentals")
plt.grid(axis='y')
plt.show()

# plt.clf # 초기화

