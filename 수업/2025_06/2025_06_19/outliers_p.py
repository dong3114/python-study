import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import koreanize_matplotlib

'''
정답: B
정답: B OR A
정답: D?
'''
df = pd.DataFrame({
    "process": ["A"]*6 + ["B"]*6,
    "weight": [101, 102, 100, 99, 98, 102, 120, 121, 122, 119, 118, 121]
})

# 바이올린플롯으로 공정별 분포 시각화
sns.violinplot(x="process", y="weight", data=df)  # (1)
plt.title("공정별 제품 무게 분포")
plt.show()
