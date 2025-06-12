import pandas as pd
import numpy as np

# arange로 1차원 배열 생성
arr1 = np.arange(3,12,2)
# 인덱스와 함께 value 값을 반환 하는 차원 배열 구조
# 데이터 타입을 지정할 수 있다. dtype
d1 = pd.Series(arr1, dtype='float32')
print(d1)

d2 = pd.Series(['가', '나', '다', '라', '마'], dtype=object)
print(f"d2 출력합니다 \n{d2}")

# index 지정
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
sorted_obj = obj2.sort_index()
print(sorted_obj)

# 조건부 필터링
print(obj2[obj2 > 0])  #불리안 인덱스(Boolean Indexing) : True에 해당하는 행만 조회  

# 데이터 연산
print(obj2 * 2)

# 딕셔너리처럼 키 값으로 확인
print('b' in obj2)  # True
print('f' in obj2)  # False