# calculator.py

# 덧셈
def add(x, y):
  return x + y

# 곱셈
def multiply(x, y):
  return x * y

# 뺼셀
def substract(x, y):
  return x - y

# 나눗셈
def division(x, y):
  if y == 0:
    return f"{y}은(는) 분모가 될 수 없습니다."
  return x / y