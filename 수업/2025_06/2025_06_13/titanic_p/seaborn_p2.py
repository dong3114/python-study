import seaborn as sns
import pandas as pd
import missingno as ms
import matplotlib.pyplot as plt

sns.get_dataset_names()
df = sns.load_dataset("titanic")

# 1. df.isnull().sum()을 사용해 각 열의 결측치 개수를 출력하세요.
# print(df.isnull().sum())

# 2. missingno.matrix()를 사용해 결측치를 시각화해보세요.
# ms.matrix(df)
# plt.show

# 3. 결측치가 존재하는 행만 필터링하여 출력해보세요.
# df["age"] = df["age"].fillna(df["age"].median())
# print(df["age"])

# 4. age` 컬럼의 결측치를 중앙값(median)으로 채우고 결과를 확인하세요.
# df.age.isnull().sum()
# print(df["age"])

# 5. deck` 컬럼의 결측치를 'Unknown'으로 채우세요.
# df['deck']=df["deck"].cat.add_categories('Unknown').fillna('Unknown') #category
# print(df['deck'])

# 6. dropna()`를 사용해 결측치가 있는 행을 제거하고 결과를 확인하세요.


# 7. df.duplicated().sum()을 사용해 중복된 행의 개수를 확인하세요.


# 8. drop_duplicates()를 사용해 중복된 행을 제거하세요.


# 9. age`가 70세 이상인 승객만 필터링하여 이상치를 시각적으로 확인하세요.


# 10. boxplot을 이용해 나이의 이상치를 시각화하세요.


# 11. df['fare'].plot.box()를 이용해 요금의 이상치를 시각화하세요.


# 12. IQR을 이용한 사용자 정의 함수를 만들어 `fare`의 이상치를 제거해보세요.(apply 함수 활용)


# 13. 이상치 제거 전후의 행 개수를 비교 출력해보세요.

