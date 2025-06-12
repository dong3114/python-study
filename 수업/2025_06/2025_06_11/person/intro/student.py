from .person import Person

class Student(Person):
  def __init__(self, name, number):
    # super().__init__() 와 같음
    Person.__init__(self, name)
    self.number = number

  def stu(self):
    print(f"저는 {self.name}이고, {self.number}학년 입니다.")