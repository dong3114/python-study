import pandas as pd

# 모든 컬럼을 다 보이게 설정
pd.set_option('display.max_columns', None)

# 모든 행을 다 보이게 설정 (선택)
pd.set_option('display.max_rows', None)

# 컬럼 너비를 충분히 확보 (줄바꿈 방지)
pd.set_option('display.width', 1000)

# 컬럼 내용이 너무 길어도 자르지 않게
pd.set_option('display.max_colwidth', None)

# 데이터프레임 생성
df = pd.DataFrame({
    "A": [1, 2, 3, 4],
    "B": [10, 20, 30, 40]
})
# 행 단위로 계산
df["Sum"] = df.apply(lambda row: row["A"] + row["B"], axis=1)

population = [35000, 71000, 16000, 5000]
state = ['Ohio', 'Texas', 'Oregon', 'Utah']
debt=  [1.2, 1.5, 1.7, 1.9]

frame = pd.DataFrame({'Population': population, 'State': state, 'Debt': debt}, index=['A', 'B', 'C', 'D'])
frame['eastern'] = frame['State'] =="Ohio"

# 13 면적 데이터 추가
area_data = [50000, 70000, 45000, 30000]
frame['Area'] = area_data
print(f"13. 면적데이터 추가 \n{frame}")

# 14 인구 밀도 계산
# "Population"과 "Area"를 이용해 "Population_Density"라는 새 컬럼을 만드세요.
frame['Population_Density'] = frame["Population"] / frame['Area']
print(f"14. 인구 밀도 계산 \n{frame}")

# 15. 부채 상태에 따라 범주형 데이터 생성 (리스트 컴프리헨션 사용)
# "debt" 값을 기준으로 1.5 미만이면 "Low", 그렇지 않으면 "High"로 설정한
# 새로운 "Debt_Level" 컬럼을 리스트 컴프리헨션으로 생성하세요.
frame['Debt_Level1'] = ['Low' if debt < 1.5 else 'High' for debt in frame['Debt']]
print(f"15. 부채 상태 계산 \n{frame}")

# 15-1. 부채 상태에 따라 범주형 데이터 생성 (apply 함수 사용)
# apply를 사용하여 "Debt_Level" 컬럼을 생성하세요.
frame['Debt_Level2'] = frame["Debt"].apply(lambda debt: 'Low' if debt < 1.5 else 'High')
print(f"15-1. 부채 상태 계산 \n{frame}")

# 15-2. 특정 위치에 새 컬럼 삽입
# "Debt_Level" 컬럼을 "debt" 컬럼 뒤에 삽입하세요.
frame.insert(
    loc=3, 
    column='Debt_Level3', 
    value=frame["Debt"].apply(lambda debt: 'Low' if debt < 1.5 else 'High')
)
print(f"15-2. 부채 상태 계산 \n{frame}")
