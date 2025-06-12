# iloc[]: 정수형 인덱스로 접근 (행접근)
# loc[]: 인덱스 이름으로 접근 (행접근)
# isin(): 특정값이 포함되어 있는지 여부 확인
# df.drop(axis=1) 컬럼 삭제
# df.drop(axis=0) 행 삭제(default)
# df.rename(columns={'A':'B'}) 칼럼명 변경
# df.T 행과 열 전치 
import pandas as pd
population = [35000, 71000, 16000, 5000]
state = ['Ohio', 'Texas', 'Oregon', 'Utah']

# 1. 데이터프레임 생성
# 데이터프레임을 생성하고, 'Population'과 'State' 칼럼을 포함하며, 인덱스를 ['A', 'B', 'C', 'D']로 설정하세요.
frame = pd.DataFrame({'Population': population, 'State': state}, index=['A', 'B', 'C', 'D'])
print(frame)

# 2. 데이터 조회
# 'State' 컬럼만 출력하려면 어떻게 해야 할까요?
print("데이터조회")
print(frame['State'])  
print(frame.State)

# 3. 행 접근(iloc, loc)
# iloc를 사용해 두 번째 행(정수 인덱스 1)을 출력하세요.
print(frame.iloc[1])
# loc를 사용해 인덱스 이름이 'B'인 행을 출력하세요.
print(frame.loc['B'])

# 4. 특정 값 접근
# 첫 번째 행의 두 번째 열 값을 iloc와 loc로 각각 접근하세요.
print(frame.iloc[0, 1])  # iloc
print(frame.loc['A', 'State'])  # loc

# 5. 조건부 필터링
# 'State'가 ['Ohio', 'Texas'] 중 하나인 행만 필터링하세요.
print(frame[frame['State'].isin(['Ohio', 'Texas'])])

# 'Population'이 20000 이상인 행만 필터링하세요.
print(frame[frame['Population'] >= 20000])

# 6. 새로운 컬럼 추가
# 새로운 컬럼 'debt'와 'eastern'을 추가하세요.
frame[] = [1.2, 1.5, 1.7, 1.9]
frame[] = frame.State =="Ohio"
print(frame)

# 7. 새로운 행 추가
# 새로운 행을 추가하세요. 인덱스는 'E', 데이터는 [45000, 'Nevada', 1.8, True]로 설정하세요.
frame.loc[___] = [___, ___, ___, ___]
print(frame)

# 8. 특정 값 수정
# 'C' 행의 'Population' 값을 40000으로 수정하세요.
frame.loc[___, ___] = ___
print(frame)


# 9. 컬럼 삭제
# 'eastern' 컬럼을 삭제하세요. del과 drop 두 가지 방법을 사용해 보세요.
del frame[___]
frame = frame.drop(columns=___)
frame = frame.drop('eastern', axis=)

# 10. 행 삭제
# 'B' 행을 삭제하세요. inplace 옵션을 활용하세요.
frame.drop(index=___, inplace=)
print(frame_dropped_row)


# 11. 컬럼 이름 변경
# 'debt' 컬럼 이름을 'Debt'로 변경하세요.
frame._____(columns={___: ___}, inplace=True)


# 12. 데이터 전치 (Transpose)
# 데이터프레임의 행과 열을 바꾸세요.
transposed_frame = frame.___
print(transposed_frame)
