class Car:
  # 생성자 생성
  def __init__(self, model, year):
    self.model = model
    self.year = year

  # 출발
  def start(self, person):
    print(f"{self.year}에 제작 되었습니다.")
    print(f"{self.model} 차량이 출발합니다.")
    print(f"운전자는 {person} 입니다")
  
