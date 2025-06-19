'''
C, A, A, B, C, D, C, C
'''

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

titanic = sns.load_dataset(('titanic'))

# 이시각화를통해서 알아낼수있는 인사이트를 통계적 관점에서 서술하라.
# sns.violinplot(x="survived", y="age", data=titanic)
'''
답: 
전체적으로 생존자 그룹의 나이 분포가 사망자 그룹보다 상대적으로 젊은 연령대에 밀집해 있으며,
분포의 폭도 더 좁은 경향을 보입니다. 특히 생존자의 바이올린플롯은 저연령에서 밀도가 높아
어릴수록 생존 가능성이 높았음을 유추할 수 있습니다.
따라서 해당 구조 과정에서 어린이 우선 원칙이 일부 반영되었을 가능성이 있습니다.
'''
# a = sns.histplot(data=titanic, x="age", bins=20, hue="sex", multiple="stack")

from sklearn.preprocessing import MinMaxScaler, StandardScaler
# fear 칼럼 정규화하고 히스토그램 시각화 kde plot출력
titanic["fare"] = titanic["fare"].astype(int)

titanic["fare_minmax"] = (titanic["fare"] - titanic["fare"].min()) / (titanic["fare"].max() - titanic["fare"].min())

sns.kdeplot(data=titanic, x="fare_minmax", fill=True)
plt.title("정규화된 fare 변수의 밀도 분포")
plt.xlabel("정규화된 fare 값")
plt.ylabel("밀도")
# plt.show()

# fear 칼럼 표준화 하고 시각화
plt.clf()

std_scaler = StandardScaler()
std_data = std_scaler.fit_transform(titanic[["fare"]])
# 결과는 numpy array → 다시 컬럼으로 저장
titanic["fare_zscore"] = std_data

sns.kdeplot(data=titanic, x="fare_zscore", fill=True)
plt.title("Z-score로 표준화된 fear 분포")
plt.xlabel("표준화된 fare")
plt.ylabel("밀도")
plt.show()

