# return과 print
def sum_a_b(a,b):
      result = a + b
      return result

def sum_a_b2(a, b):
      result = a + b
      print(result)
      	
x=sum_a_b(2,2)
print(x)

y=sum_a_b2(3,3)
print(y)


## args`
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4)) # 10

## *kwargs 
def print_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_profile(s="남성", hp="100", job="none", city="Busan")

# 여러개의 값 리턴
# 반환값이 여러개일 경우, 반환하는 결과형은 Tuple(튜플)이다.
def sum_a_b3(a,b):
  result=a+b
  return result, result**2
print(sum_a_b3(1,2))

# 변수의 유효 범위
global_var = "전역 변수"
def print_var():
    local_var = "지역 변수"
    print(global_var)
    print(local_var)
print_var()
# print(local_var) → 오류 발생

# list 내부의 데이터를 제곱해서 재가공
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
# 함수를 넣어서 사용할 수도 있음
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # [1, 4, 9, 16, 25]

# 람다함수
numbers = [1,2,3]
x = 2
y = 10
# n은 numbers의 각 원소
lam = list(map(lambda n: n + x + y, numbers))
print(lam)

# 문제 풀이
# 자연수 n이 매개변수로 주어집니다. 
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수
# x를 return 하도록 solution 함수를 완성해주세요.
# 답이 항상 존재함은 증명될 수 있습니다.

def solution(n):
    answer = 0
    new_n = n-1
    for i in range(2, n):
        if new_n % i == 0:
            answer = i
            break
    return answer
print(solution(3))

def solutuion2(n):
    return min([i for i in range(2,n) if n % i ==1])
print(f"컴프리헨션 {solutuion2(3)}")

'''
소시지 생산 공장에서 모든 제품은 HACCP 테스트를 받아야 하며,
각 제품은 규격에 따라 중량 기준을 만족해야 합니다.
HACCP 검사를 받지 못했거나, 중량이 기준에 미달하는 제품은
빠르게 식별되어야 합니다. 또한, 공장에서 검사 또는 재처리가 필요한
품목의 비율을 계산하여 전반적인 품질 관리 상태를 확인하는 것이 중요합니다.
'''
# 목표
# 테스트 받지 못한 품목 리스트 반환함수
# or 조건 인지
# HACCP 미완료 품목 중 중량 미달에 해당하는 품목 갯수를 반환함수

# 데이터
# HACCP 테스트 데이터: 검사된 품목 리스트로 제공
# 전체 품목 데이터: 딕셔너리 형태로 제공, 각 품목의 이름과 중량 정보 포함
# 중량 기준: 각 품목의 중량이 100g 이상

# 전체 품목 데이터 (품목명: 중량(g))
factory_products = {
    "Sausage_A": 90,
    "Sausage_B": 120,
    "Sausage_C": 110,
    "Sausage_D": 115,
    "Sausage_E": 98,
    "Sausage_F": 70,
    "Sausage_G": 101
}

# HACCP 검사를 받은 품목 리스트
haccp_tested = ["Sausage_A", "Sausage_B", "Sausage_D"]

# 중량 기준 (g)
weight_standard = 100

# HACCP 미검사 품목 리스트
def untested(factory_products,haccp_tested):
    hac_te = ""
    for i in range(len(haccp_tested)):
        hac_te = haccp_tested[i]
        for j in range(len(factory_products)):
            if hac_te in factory_products.keys():
                factory_products.pop(hac_te, None)
    return factory_products
print("미검사 실행")
print(untested(factory_products,haccp_tested))

# untested 항목 중 중량미달에 해당하는 품목의 갯수 
def underweight(factory_products, haccp_tested, weight_standard):
    new_pro = untested(factory_products,haccp_tested)
    count = 0
    for i in new_pro.values():
        if i < weight_standard:
            count += 1
    return count
print("중량검사")
print(underweight(factory_products, haccp_tested, weight_standard))

# 300제 문제
# 1번
blank = "------"
n = 30
for i in range(10, n+1, 10):
    print(i)
    print(blank)

# 2번
food = ["김밥", "라면", "튀김"]
today_menu = []
for i in range(len(food)):
     today_menu.append(f"오늘의 메뉴: {food[i]}")
     print(today_menu[i])

# 3번
animals = ['dog', 'cat', 'parrot']
fir = []
for i in range(len(animals)):
    word = animals[i]
    fir.append(word[0])
print(fir)

# 4번
numbers = [1, 2, 3]
for i in range(len(numbers)):
    print(f"{numbers[2]} * {numbers[i]} = {numbers[2]*numbers[i]}")

# 5번
lit = ["A", "b", "c", "D"]
for i in range(len(lit)):
    if lit[i].isupper():
          print(lit[i])

# 6번
# 스플릿을 사용해서 자른 후 특정 요소만 가져오고 싶으면
# 해당 요소 인덱스 번호 입력
file_list = ['hello.py', 'ex01.py', 'intro.hwp']
for i in range(len(file_list)):
    print(file_list[i].split(".")[0])

# 7번 
# enumerate 사용x
price_list = [32100, 32150, 32000, 32500]
lit2 = []
for i in range(len(price_list)):
    index_num = i
    lit2.append(f"{i} {price_list[i]}")
    print(lit2[i])
# enumerate 사용o
for idx, price in enumerate(price_list):
     print(f"enumerate사용 {idx}, {price}")

# 문제 1: 짝수와 홀수
# 정수 num 이 짝수 일때 "even" 홀수일때"odd"반환
def number_classification(n):
     answer = ""
     if n % 2 == 0:
          answer = "Evem"
     else:
          answer = "Odd"
     return answer
print(number_classification(15))

# 문제 2: 문자열 뒤집기
def rever(s):
  w = ""
  s_list = []
  for item in range(len(s)):
      print(s[item])
      s_list.append(s[item])
  s_list.reverse()
  for word in range(len(s_list)):
      w += s_list[word]
  return w
print(rever("hello"))

# 문제 3: 리스트 평균 구하기
numbers = [1, 2, 3]
def numbers_average(numbers):
    return int(sum(numbers) / len(numbers))
print(numbers_average(numbers))

# 문제 4: 소문자 → 대문자 변환
strings = ["a", "b"]
def list_upper(strings):
    return [i.upper() for i in strings]
print(list_upper(strings))

# 문제 5: 리스트에서 2와 3의 배수만 추출
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def multiple_num(a,b, numbers2):
    mul = (a * b) / gcd(a,b)
    mul_list = []
    for i in numbers2:
        if i % mul == 0:
          mul_list.append(i)
    return mul_list

numbers2 = [1, 2, 3, 4, 6, 12, 15, 30]
print(multiple_num(2,3,numbers2))

# 문제 6: 문자 개수 세기
def text_count(s, target):
    count = 0
    i = 0
    while True:
        if s[i] == target:
            count += 1
        i += 1
        if i == len(s):
            break
    return count
s = "banana"
target = "a"
print(text_count(s, target))
