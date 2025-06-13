# 사용 할 주요 컬럼

# 승하차 시간 추적 로그 컬럼
# pickup_datetime: 승객이 탑승한 날짜와 시간
# dropoff_datetime: 승객이 하차한 날짜와 시간

# passenger_count: 승객수
# trip_distance: 운행 거리(마일 단위)

# 승하차 장소 추적 로그 컬럼
# PULocationID: 픽업 지점의 지역 코드(Location ID)
# DOLocationID: 하차 지점의 지역 코드(Location ID)

# 금액 컬럼
# fare_amount: 기본 요금
# extra: 추가 요금(예: 혼잡 요금, 야간 요금 등))
# mta_tax: MTA 세금
# tip_amount: 팁 금액
# total_amount: 총 요금 (팁 포함)
# payment_type: 결제 방식 (1: 카드, 2: 현금 등)

import pandas as pd
from pathlib import Path

# 옵션: 너무 많은 열/행 생략 방지
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

# csv 파일 불러오기
csv_path = Path(__file__).parent / "content" / "sample_with_missing.csv"

# 파일 일부분만 미리 읽기
preview_rows = 10
df = pd.read_csv(csv_path, nrows=preview_rows)

# 전체 행 수 알아보기 (헤더만 읽고 shape 확인)
total_rows = sum(1 for _ in open(csv_path)) - 1  # 첫 줄은 header니까 제외

# 출력
print(f"✅ 미리보기: 상위 {preview_rows}개 행 (전체 {total_rows}행 중 일부)\n")
print(df)
print(f"\n📊 전체 열 개수: {len(df.columns)}개")

import missingno as msno
import matplotlib.pyplot as plt

msno.matrix(df)

# 꼭 필요함!
plt.show()
