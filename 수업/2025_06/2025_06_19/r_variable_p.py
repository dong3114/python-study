import numpy as np
import matplotlib.pyplot as plt

# 이산형 변수: 하루 동안의 불량 개수 (예: 0~5개)
discrete = np.random.choice([0, 1, 2, 3, 4, 5], size=100, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1])

# 연속형 변수: 제품 길이 (정규분포를 따른다고 가정)
continuous = np.random.normal(loc=100, scale=5, size=100)

# print(f"이산형 변수: {discrete}, 연속형 변수: {continuous}")


# PMF 예시: 이항분포 시각화
from scipy.stats import binom
x = [0, 1, 2, 3, 4, 5]
pmf = binom.pmf(x, n=5, p=0.3)
plt.bar(x, pmf)
plt.title("PMF of Binomial Distribution (n=5, p=0.3)")
plt.show()

# PDF 예시: 정규분포 시각화
from scipy.stats import norm
x = np.linspace(90, 110, 100)
pdf = norm.pdf(x, loc=100, scale=5)
plt.plot(x, pdf)
plt.title("PDF of Normal Distribution")
plt.show()