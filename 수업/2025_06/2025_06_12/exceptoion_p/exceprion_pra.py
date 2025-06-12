# 숫자 입력만 받기
def value_except():
  try:
      user_input = input("숫자를 입력하세요: ")
      num = int(user_input)
      print(f"입력한 숫자: {num}")
      print("실행 종료")
  except ValueError:
      print("숫자가 아닙니다!")
      return value_except()
value_except()