import sys
sys.dont_write_bytecode = True
# main.py
from utils.calc import add, multiply, substract, division
a = int(input(f"첫번째 숫자를 입력하세요: "))
b = int(input(f"두번째 숫자를 입력하세요: "))

# print(add(a,b))
# print({multiply(a,b)})
# print(substract(a,b))
# print(division(a,b))

n = add(a,b)
d = int(input("출금액을 말해주세요: "))

print(f"현재 잔고는 {substract(n,d)}₩ 입니다")