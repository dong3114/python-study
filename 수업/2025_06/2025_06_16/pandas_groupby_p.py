import pandas as pd

# 샘플 데이터 생성
df = pd.DataFrame({
    "부서": ["HR", "HR", "IT", "IT", "Finance", "Finance"],
    "성별": ["여", "남", "여", "남", "여", "남"],
    "연봉": [5000, 5500, 6000, 7000, 6500, 7500],
    "근속년수": [5, 7, 3, 8, 6, 10]
})

# 부서별 연봉 평균
df_gb = df.groupby("부서")["연봉"].mean() # median, sum, min 
# print(df_gb)
'''
성별 부서별 평균 연봉
groupby([컬럼1,컬럼2])["값"].(집계함수) 
'''
# print(df.groupby(["성별", "부서"])["연봉"].mean())


