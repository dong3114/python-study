import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import koreanize_matplotlib

class FoodPriceAnalyzer:
    def __init__(self, df: pd.DataFrame, item_name: str):
        self.df = df
        self.item = item_name

    def analyze_vs_temperatures(self, temp_cols: list):
        # 온도 vs 가격 회귀선 + 상관계수
        for temp_col in temp_cols:
            self._plot_and_corr(temp_col)

    def _plot_and_corr(self, temp_col: str):
        import matplotlib.pyplot as plt
        import seaborn as sns
        from scipy.stats import pearsonr

        plt.figure(figsize=(8, 6))
        sns.regplot(data=self.df, x=temp_col, y=self.item,
                    scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})
        plt.title(f"{self.item} 가격 vs {temp_col}")
        plt.xlabel(temp_col)
        plt.ylabel(f"{self.item} 가격 (원)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        r, p = pearsonr(self.df[temp_col], self.df[self.item])
        print(f"📊 {self.item} 가격 vs {temp_col}")
        print(f"📉 피어슨 상관계수 r = {r:.4f}, p-value = {p:.4f}\n")


