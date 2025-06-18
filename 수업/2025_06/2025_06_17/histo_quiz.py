import numpy as np
data = [100, 105, 110, 120, 115, 700]
# 평균
data_mean = np.mean(data)
print(f"평균: {data_mean}")
# 중앙값
data_middle = np.percentile(data, 50)
print(f"중앙값: {data_middle}")
# 최빈값
data_dict = {}
def value_match(data):
    for d in data:
        if d in data_dict:
          data_dict[d] += 1
        else:
           data_dict[d] = 1
        # 등장 횟수
        max_freq = max(data_dict.values())
        modes = [i for i, j in data_dict.items() if j == max_freq]
    return modes, max_freq
modes, count = value_match(data)
print(f"최빈값: {modes}, 빈도수: {count}")

data2 = np.array([10,20,30,40,50])
# 평균
data2_mean = np.mean(data)
# 편차
data2_deviation = data2 - data2_mean
# 분산
data2_variance = np.mean(data2_deviation ** 2)
# 표준편차
data2_SD = np.sqrt(data2_variance)
# 변동계수 (백분율)
cv = data2_SD / data2_mean
print(f"평균: {data2_mean:.2f}")
print(f"분산: {data2_variance:.2f}")
print(f"표준편차: {data2_SD:.2f}")
print(f"변동계수: {cv:.2f} ({cv*100:.2f}%)")

