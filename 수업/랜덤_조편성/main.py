import sys
sys.dont_write_bytecode = True

from utils.assign_group import AssignGroup
# 1. 조원 이름 입력 받기
# 미구현 while문으로 input을 받아서 리스트화
members = ["사람1", "사람2", "사람3", "사람4", "사람5"]

# 2. 그룹화 클래스 실행
go = AssignGroup(members)
result = go.assign_number()
print(result)