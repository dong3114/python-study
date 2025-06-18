import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

data = [
    151, 154, 160, 160, 163, 156, 158, 156, 154, 160,
    154, 162, 156, 162, 157, 162, 162, 169, 150, 162,
    154, 152, 161, 160, 160, 153, 155, 163, 160, 159,
    164, 158, 150, 155, 157, 161, 168, 162, 153, 154,
    158, 151, 155, 155, 165, 165, 154, 148, 169, 158,
    146, 166, 161, 143, 156, 156, 149, 162, 159, 164,
    162, 167, 159, 153, 146, 156, 160, 151, 151, 157,
    151, 156, 166, 159, 157, 156, 159, 156, 156, 161
]

# pandas Series로 변환
s = pd.Series(data)

# 히스토그램 그리기
plt.figure(figsize=(5,8))
plt.hist(s, bins=10, edgecolor='black')

plt.title('키별 분산표 히스토그램')
plt.xlabel('키 (cm)')
plt.ylabel('빈도')
plt.grid(True)
# plt.show()

# 데이터 값
data = np.array([5, 10, 15, 20, 30, 40])
# 1. 평균 계산
mean_value = np.mean(data)
# 2. 편차 (Deviation)
deviations = data - mean_value

print(f"평균: {mean_value}")
print(f"편차: {deviations}")
