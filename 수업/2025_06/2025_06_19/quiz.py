import matplotlib.pyplot as plt
import pandas as pd

# 온도 센서 측정값 12개
data = {
    "temperature": [23.4, 24.1, 22.8, 23.9, 24.5, 23.7, 100.0, 24.0, 23.8, 22.9, 23.6, 24.2]
}

df = pd.DataFrame(data)


df["z_score"] = (df["temperature"] - df["temperature"].mean()) / df["temperature"].std()

# Z-score가 절댓값 ___ 이상인 값을 이상치로 간주
outliers = df[ df["z_score"].abs() > ___ ]

# 표준화
df["temperature_std"] = (df["temperature"] - df["temperature"].____()) / df["temperature"].____()

# 정규화 (min-max)
df["temperature_minmax"] = (df["temperature"] - df["temperature"].____()) / (df["temperature"].____() - df["temperature"].____())

plt.plot(df["temperature"], label="original")
plt.plot(df["temperature_std"], label="standardized")
plt.plot(df["temperature_minmax"], label="min-max")
plt.legend()
plt.title("온도 원본 / 표준화 / 정규화 비교")
plt.show()