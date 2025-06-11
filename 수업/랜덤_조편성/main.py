import sys
sys.dont_write_bytecode = True

from utils.assign_group import AssignGroup
# 리스트 예시
# members = ["사람1", "사람2", "사람3", "사람4", "사람5"]

# 1. 조원 이름 입력 받기
members = ["사람1", "사람2", "사람3", "사람4", "사람5"]

# 2. 
go = AssignGroup(members)
result = go.assign_number()
print(result)