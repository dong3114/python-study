import warnings
warnings.filterwarnings('ignore')

'''
### [객관식] Q1. 날짜 포맷 코드 (필수 포함 문제)

다음 중 **월의 전체 이름 (예: March)** 을 의미하는 `strftime()` 포맷 코드는?
답: A

A. `%m`

B. `%M`

C. `%B`

D. `%b`

📌 *힌트: [strftime 포맷 코드 검색](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)*

---

### [객관식] Q2. `pd.to_datetime()`의 옵션 이해

`errors='coerce'`를 설정할 경우 어떤 일이 발생하는가?
답: A

A. 변환 가능한 형식은 유지되고, 불가능한 값은 NaT로 바뀐다

B. 문자열이 datetime 형식이 아니면 오류가 발생한다

C. NaN 값은 자동으로 제거된다

D. 변환이 불가능한 값은 삭제된다

---

### [객관식] Q3. groupby() + transform의 특징

다음 중 `.transform()` 함수의 설명으로 알맞은 것은?
답: C

A. 그룹별로 하나의 요약값을 반환한다

B. 원본과 다른 크기의 시리즈를 반환한다

C. 그룹 내 개별 값을 기준으로 변환하며 원본과 같은 크기의 시리즈를 반환한다

D. 평균, 합계만 적용 가능하다

---

### [객관식] Q4. concat()과 merge() 비교

다음 중 `pd.concat()`과 `pd.merge()`의 차이에 대한 설명으로 적절한 것은?
답: C

A. 둘 다 기본적으로 인덱스를 기준으로 병합한다

B. concat은 key 컬럼 기준 병합이며 merge는 axis 기준 결합이다

C. concat은 단순 연결, merge는 공통 컬럼 기준 병합이다

D. concat은 SQL의 JOIN, merge는 UNION ALL과 같다

'''
# Q5.strftime()을 활용하여 현재 시간을 "YYYY-MM-DD HH:MM" 형식 문자열로 출력하세요.
from datetime import datetime
import pandas as pd

now = datetime.now()
format_date = now.strftime("%Y-%m-%d %H:%M")
# print(format_date, type(format_date))

# Q6. 다음 DataFrame에서 "2023/01/01"을 datetime으로 변환하고, 연도(year) 만 추출하는 코드를 작성하세요
df = pd.DataFrame({"date": ["2023/01/01"]})
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
# print(df)

# Q7. 아래 DataFrame에서 국어 점수 기준으로 내림차순 정렬된 결과를 반환하는 코드를 작성하세요.

# Q8. 아래 데이터를 이용해 부서별 평균 연봉을 계산하고 새로운 컬럼 "부서평균"으로 원본에 추가하세요.

# Q9. 아래 두 DataFrame을 직원ID 기준으로 내부 조인(inner join) 하여 병합하는 코드를 작성하세요.

df1 = pd.DataFrame({
    "직원ID": ["E1", "E2", "E3"],
    "이름": ["홍길동", "김철수", "이영희"]
})

df2 = pd.DataFrame({
    "직원ID": ["E2", "E3", "E4"],
    "부서": ["회계팀", "영업팀", "개발팀"]
})

df_inner = pd.merge(df1, df2, on="직원ID", how="inner")
# print(df_inner)

# 빅분기 기출 문제 
'''
Q1.
학교 세부유형이 일반중학교인 학교들 중
일반중학교 숫자가 2번째로 많은 시도의 일반중학교 데이터만
필터하여 해당 시도의 교원 한명 당 맡은
학생수가 가장 많은 학교를 찾아서 해당 학교의 교원수를 출력하라
'''
df3 = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e6_p1_2.csv')
# sprint(df3.head(5))

# step1 세부유형 일반중학교 중 숫자가 2번째로 많은 시도 필터
filter = df3[df3['학교세부유형'] == '일반중학교']
df3_count = filter['시도'].value_counts()
second_sido = df3_count.index[1]
# print(second_sido) # 시도 확인
step1_result = filter[filter['시도'] == second_sido]
# print(step1_result.head(5))

# step2 필터된 데이터프레임에서 교원 한명 당 맡은 학생수가 가장 많은 학교의 교원수 필터링
step1_result['교원당_학생'] = step1_result['일반학급_학생수_계'] / step1_result['교원수_총계_계']
# print(step1_result.head(5))
st2_sorted = step1_result.sort_values(by="교원당_학생", ascending=False)
# print(st2_sorted.head(3))
step2_result = st2_sorted.iloc[0]['교원수_총계_계']
# print(step2_result)

'''
Q2.
5대 범죄(절도, 사기, 배임, 방화, 폭행)의 월별 총 발생건수를
총범죄수라고 표현하자. 18,19년의 각각 분기별 총범죄수의
월평균 값을 구했을때 최대값을 가지는 년도와 분기를 구하고
해당 분기의 최댓값의 사기가 발생한 월의 사기 발생건수를
출력하라
(1분기:1,2,3월 / 2분기 : 4,5,6월 /
 3분기 7,8,9월 / 4분기 10,11,12월 ,
 1분기 월평균 : 1,2,3월의 총범죄수 평균)
'''
# step1 총범죄수 컬럼 추가 후 18,19년도 각각 분기별 총범죄수 월평균 값
df2 = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e6_p1_3.csv')
# 더할 열 지정하기
columns_sum = ['절도', '사기', '배임', '방화', '폭행']
# 행 별로 총합 '총범죄수' 컬럼 추가
df2['총범죄수'] = df2[columns_sum].sum(axis=1)
# print(df2.head(3))
df2[['년도', '월']] = df2['범죄분류'].str.split('_', expand=True)

# 숫자 변환
df2['년도'] = df2['년도'].str.replace('년', '').astype(int)
df2['월'] = df2['월'].str.replace('월', '').astype(int)

# 분기를 나누는 함수 생성
def get_quarter(month):
  if month in [1,2,3]:
    return '1분기'
  elif month in [4, 5, 6]:
    return '2분기'
  elif month in [7, 8, 9]:
    return '3분기'
  else:
    return '4분기'

df['분기'] = df2['월'].apply(get_quarter)

s = "사과,배,포도,귤"
result = s.split(',', maxsplit=3)
print(result)