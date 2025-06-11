from .random_number import RandomNumber

class AssignGroup:
  def __init__(self, members):
    self.members = members

  def assign_number(self):
    print("1. 전 인원에게 난수 부여")
    # 1. 전 인원에게 난수 부여
    ran = RandomNumber(self.members)
    r_list = ran.random_number()
    n = len(r_list)
    items = list(r_list.items())

    print("2. 점수 별로 4개 그룹으로 그룹핑")
    # 2. 점수 별로 4개 그룹으로 그룹핑
    for i in range(n):
      for j in range(n - i - 1):
        if items[j][1] > items[j+1][1]:
          items[j], items[j+1] = items[j+1], items[j]

    print("3. 새롭게 할당될 딕셔너리")
    # 3. 새롭게 할당될 딕셔너리 { "이름": x조 }
    assign_list = {}

    fir = int(n / 4)
    sec = int(n / 2)
    thi = int(n * 3 / 4)
    fou = n

    for i, (name, score) in enumerate(items):
      if i < fir:
        assign_list[name] = "1조"
      elif i < sec:
        assign_list[name] = "2조"
      elif i < thi:
        assign_list[name] = "3조"
      else:
        assign_list[name] = "4조"

    return assign_list