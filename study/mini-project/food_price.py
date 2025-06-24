import matplotlib.pyplot as plt
import seaborn as sns


class FoodPrice:
    def __init__(self, df):
        """
        :param df: '연도', '월', '쌀', '평균기온(℃)' 포함된 DataFrame
        """
        self.df = df

    def plot_rice_price_by_month(self):
        """
        연도별 1~12월 쌀 가격 추이 (선그래프)
        """
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=self.df, x="월", y="쌀", hue="연도", markers="o")
        plt.title("연도별 월별 쌀 가격 추이")
        plt.ylabel("쌀 가격")
        plt.xlabel("월")
        plt.xticks(range(1, 13))
        plt.grid(True)
        plt.legend(loc='upper right')
        plt.tight_layout()
        plt.show()

    def plot_temperature_by_month(self):
        """
        연도별 1~12월 평균기온 추이 (선그래프)
        """
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=self.df, x="월", y="평균기온(℃)", hue="연도", markers="o")
        plt.title("연도별 월별 평균기온 추이")
        plt.ylabel("평균 기온 (℃)")
        plt.xlabel("월")
        plt.xticks(range(1, 13))
        plt.grid(True)
        plt.legend(loc='upper right')
        plt.tight_layout()
        plt.show()