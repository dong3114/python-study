import pandas as pd
# 직원 데이터
df_employees = pd.DataFrame({
    "직원ID": ["E001", "E002", "E003", "E004"],
    "이름": ["김철수", "이영희", "박지성", "손흥민"],
    "직급": ["사원", "대리", "과장", "부장"]
})
# 부서 데이터
df_departments = pd.DataFrame({
    "직원ID": ["E001", "E002", "E004", "E005"],
    "부서": ["영업팀", "마케팅팀", "개발팀", "재무팀"]
})

# ✅ Inner Join (공통 직원ID 기준)
df_inner = pd.merge(df_employees, df_departments, on="직원ID", how="inner")
# print(df_inner) 

# ✅ Left Join (모든 직원 포함)
df_left = pd.merge(df_employees, df_departments, on="직원ID", how="left")
print(df_left)