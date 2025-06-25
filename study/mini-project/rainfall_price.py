import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# df_main: 각 상품 가격 및 연도 별 평균온도가 포함된 데이터 셋
# df_rain: 연도별 강수량
import matplotlib.pyplot as plt
import pandas as pd

def plot_rainfall_price(df_main, df_rain):
    df = pd.merge(df_main, df_rain, on=['연도', '월'], how='inner')

    # 날짜형 컬럼 생성 및 정렬
    df['년월'] = pd.to_datetime(df['연도'].astype(str) + '-' + df['월'].astype(str).str.zfill(2))
    df = df.sort_values('년월')

    fig, ax1 = plt.subplots(figsize=(14, 6))

    # 배추 가격: bar → datetime에선 width 조정이 중요
    ax1.bar(df['년월'], df['배추'], width=20, color='seagreen', label='배추 가격')  # width 조정
    ax1.set_ylabel("배추 가격 (원)", color='seagreen')
    ax1.tick_params(axis='y', labelcolor='seagreen')

    # x축 설정: datetime 축 + 레이블 포맷
    ax1.set_xticks(df['년월'][::4])
    ax1.set_xticklabels(df['년월'].dt.strftime('%Y-%m')[::4], rotation=45)

    # 강수량: line
    ax2 = ax1.twinx()
    ax2.plot(df['년월'], df['월강수량합(mm)'], color='dodgerblue', marker='o', label='강수량')
    ax2.set_ylabel("강수량 (mm)", color='dodgerblue')
    ax2.tick_params(axis='y', labelcolor='dodgerblue')

    # 범례 통합
    lines, labels = [], []
    for ax in [ax1, ax2]:
        line_, label_ = ax.get_legend_handles_labels()
        lines += line_
        labels += label_
    ax1.legend(lines, labels, loc='upper right')

    plt.title("2010~2020 월별 배추 가격과 강수량 (무등산)")
    fig.tight_layout()
    plt.grid(True)
    plt.show()
    # 📉 상관계수 계산 및 출력
    r, p = pearsonr(df['배추'], df['월강수량합(mm)'])
    print(f"📉 피어슨 상관계수 (배추 vs 강수량): r = {r:.4f}, p-value = {p:.4f}")


def plot_typhoon_vs_cabbage(df):
    """
    배추 가격과 태풍 발생 수를 년월 기준으로 이중축 시각화하고
    피어슨 상관계수를 출력합니다.

    :param df: '연도', '월', '배추', '태풍발생수' 포함된 DataFrame
    """
    # 년월 문자열 생성
    df = df.copy()
    df['년월'] = df['연도'].astype(str) + '-' + df['월'].astype(str).str.zfill(2)
    df = df.sort_values(by=['연도', '월'])

    # 시각화 시작
    fig, ax1 = plt.subplots(figsize=(14, 6))

    # 배추 가격: 막대그래프
    ax1.bar(df['년월'], df['배추'], color='mediumseagreen', label='배추 가격')
    ax1.set_ylabel("배추 가격 (원)", color='mediumseagreen')
    ax1.tick_params(axis='y', labelcolor='mediumseagreen')
    ax1.set_xticks(df['년월'][::4])
    ax1.set_xticklabels(df['년월'][::4], rotation=45)

    # 태풍 발생 수: 선그래프
    ax2 = ax1.twinx()
    ax2.plot(df['년월'], df['태풍발생수'], color='royalblue', marker='o', linewidth=2, label='태풍 횟수')
    ax2.set_ylabel("태풍 발생 수", color='royalblue')
    ax2.tick_params(axis='y', labelcolor='royalblue')

    # 제목 및 출력
    plt.title("2010~2020 월별 배추 가격과 태풍 발생 수")
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 상관계수
    r, p = pearsonr(df['배추'], df['태풍발생수'])
    print(f"📉 피어슨 상관계수 (배추 vs 태풍발생수): r = {r:.4f}, p-value = {p:.4f}")