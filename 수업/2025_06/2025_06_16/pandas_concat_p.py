import pandas as pd

df1 = pd.DataFrame({"A": ["A0", "A1"], "B": ["B0", "B1"]})
df2 = pd.DataFrame({"A": ["A2", "A3"], "B": ["B2", "B3"]})

# 행 기준 연결 (axis=0, 기본값)
df_concat0 = pd.concat([df1, df2], ignore_index=True) # ignore_index=True 기존 인덱스 무시
# print(df_concat0)

# 열 기준 연결 (axis=1)
df_concat1 = pd.concat([df1, df2], axis=1)
# print(df_concat1)

