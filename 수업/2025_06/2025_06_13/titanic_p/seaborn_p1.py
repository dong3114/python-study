import seaborn as sns
import pandas as pd

sns.get_dataset_names()

# 1. 데이터 생성
df = sns.load_dataset("titanic")
# 2. 데이터의 처음 5행과 마지막 5행을 출력하여 데이터를 미리 살펴보세요.
# print(df.head())
# print(df.tail())

# 3. df.shape를 사용해 데이터의 행과 열의 수를 확인하세요.
# print(df.shape)

# 4. df.columns를 사용해 모든 열의 이름을 확인하세요.
# print(df.columns) # 열 이름 확인
# print(len(df.columns)) # 길이

# 5. df.index를 사용해 데이터의 인덱스 범위를 확인하세요.
# print(df.index())

# 6. df.info()를 사용하여 각 열의 데이터 타입과 결측치 정보를 확인하세요.
# print(df.info())

# 7. df.describe()를 통해 수치형 변수들의 요약 통계량을 확인하세요.
# print(df.describe())

# 8. df['embark_town'].unique()를 사용해 탑승 도시의 고유값 목록을 출력하세요.
# print(df['embark_town'].unique())

# 9. df['class'].nunique()를 사용해 class 변수에 몇 개의 고유값이 있는지 확인하세요.
# print(df['embark_town'].nunique())

# 10. df['who'].value_counts()를 사용해 승객 유형 분포를 확인하세요.
# print(df['who'].value_counts())