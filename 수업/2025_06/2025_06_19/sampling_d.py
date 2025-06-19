import numpy as np
import matplotlib.pyplot as plt

# 모집단 생성 (균등분포 또는 왜도 있는 분포)
population = np.random.exponential(scale=2.0, size=10000)

# 표본 평균 시뮬레이션
def simulate_sampling_means(n_samples=30, n_iter=1000):
    sample_means = []
    for _ in range(n_iter):
        sample = np.random.choice(population, size=n_samples)
        sample_means.append(np.mean(sample))
    return sample_means

sample_means = simulate_sampling_means()

plt.hist(sample_means, bins=30, edgecolor='black')
plt.title("표본평균의 분포 (n=30)")
plt.xlabel("표본 평균")
plt.ylabel("빈도")
plt.show()