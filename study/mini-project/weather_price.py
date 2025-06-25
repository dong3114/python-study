import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from rainfall_price import plot_rainfall_price, plot_typhoon_vs_cabbage
from FoodPriceAnalyzer import FoodPriceAnalyzer
from food_price import FoodPrice
import koreanize_matplotlib

path = "C:/Users/User/Desktop/workspace/study/mini-project/utils/평균기온_식품가격_재난.csv"
rain_path = "C:/Users/User/Desktop/workspace/study/mini-project/utils/monthly_rainfall.csv"

# 1. 파일 로드 (utf-8인코딩)
df = pd.read_csv(path, encoding='utf-8')
df_rain = pd.read_csv(rain_path, encoding='utf-8')
# 날짜 컬럼 연도와 월로 나누기
df['연도'] = df['날짜'].str.extract(r'(\d{4})').astype(int)
df['월'] = df['날짜'].str.extract(r'(\d{1,2})월').astype(int)
# 태풍관련 데이터프레임으로 변환
df_typhoon = df[['연도', '월', '배추', '태풍발생수']]
# 온도별 가격 클래스 로드
visualizer = FoodPrice(df)
visualizer.plot_rice_price_by_month()
visualizer.plot_temperature_by_month()
# 태풍발생별 가격
plot_typhoon_vs_cabbage(df_typhoon)
# 강수량별 가격
plot_rainfall_price(df_typhoon, df_rain)
# 품목별 인스턴스 생성
rice_analyzer = FoodPriceAnalyzer(df, "쌀")
potato_analyzer = FoodPriceAnalyzer(df, "감자")
cabbage_analyzer = FoodPriceAnalyzer(df, "배추")
# 원하는 온도 요소와의 관계 분석
rice_analyzer.analyze_vs_temperatures(["평균기온(℃)", "평균최저기온(℃)", "평균최고기온(℃)"])
potato_analyzer.analyze_vs_temperatures(["평균기온(℃)", "평균최저기온(℃)", "평균최고기온(℃)"])
cabbage_analyzer.analyze_vs_temperatures(["평균기온(℃)", "평균최저기온(℃)", "평균최고기온(℃)"])

# 심화 다중 회귀
# 병합
df_merge = pd.merge(df, df_rain, on=['연도', '월'], how='inner')

# 🎯 여기에 연도를 입력하세요 (예시: 2018)
selected_year = 2016

# 해당 연도만 필터링
df_year = df_merge[df_merge['연도'] == selected_year]

# 실제 배추 가격
y_real = df_year['배추']

# 각 독립 변수로 단일 회귀 예측
def predict_single_variable(X_column):
    X = df_year[[X_column]]
    model = LinearRegression()
    model.fit(X, y_real)
    return model.predict(X)

y_pred_temp = predict_single_variable('평균기온(℃)')
y_pred_typhoon = predict_single_variable('태풍발생수')
y_pred_rain = predict_single_variable('월강수량합(mm)')

# 시각화
plt.figure(figsize=(12, 6))
plt.plot(df_year['날짜'], y_real, label='실제 배추 가격', color='seagreen')
plt.plot(df_year['날짜'], y_pred_temp, label='예측 (평균기온)', linestyle='--')
plt.plot(df_year['날짜'], y_pred_typhoon, label='예측 (태풍발생수)', linestyle='--')
plt.plot(df_year['날짜'], y_pred_rain, label='예측 (강수량)', linestyle='--')

plt.xticks(rotation=45)
plt.title(f"{selected_year}년도 배추 가격 vs 단일 변수 회귀 예측")
plt.xlabel("날짜")
plt.ylabel("배추 가격 (원)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
