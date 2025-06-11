import random

# 리스트 예시
# members = ["사람1", "사람2", "사람3", "사람4", "사람5"]

class RandomNumber:
  def __init__(self, members):
    self.members = members

  # list에서 받은 name
  def random_number(self):
    print("1. Random메서드 시작")
    name_number = {}
    for i in self.members:
      name_number[i] = random.randint(1,100)
    print("2. Random메서드 종료")
    return name_number
    