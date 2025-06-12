# 프로그래머스
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 
# return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
n = 4586216
dight_num = len(str(n))
result = 0
for i in range(dight_num):
  num = n // (10 ** (dight_num - 1 - i))
  result += num
  n = n % (10 ** (dight_num - 1 - i))
print(f"뒷자리부터 해체 한 방식 답: {result}")

# 문자열 추출 하는 방식
n = 4586216
result = 0
for i in str(n):
  result += int(i)
print(f"문자열 방식 답: {result}")

# 문제1. 3의 배수 출력
# 1부터 30까지의 숫자 중에서 3의 배수만 출력하세요
n = 30
num = []
for i in range(n + 1):
  if i == 0:
    pass
  elif i % 3 == 0:
    num.append(i)
print(f"문제1: {num}")

# 문제2. 모음 제거하기
# 문자열에서 모음(a, e, i, o, u)을 제거한 문자열을 출력하세요.
abc = ["a","e","i","o","u"]
text = "python programming"
for i in range(len(abc)):
  text = text.replace(abc[i], "")
print(text)


# 문제3. 수 크기 비교하기
# 두 개의 숫자를 입력받아 큰 수와 작은 수를 차례대로 출력하세요.
# (input()함수 활용) )

num = []
first_num = int(input("첫번째 숫자: "))
if type(first_num) == int:
  num.append(first_num)
second_num = int(input("두번째 숫자: "))
if type(second_num) == int:
  num.append(second_num)
num.sort()
print(f"오름차순 정렬: {num}")
num.sort(reverse=True)
print(f"내림차순 정렬: {num}")

# 문제4. 문자열 길이 반환하기
# sentence 문자열을 입력받아 길이를 출력하되, 
# 빈 문자열일 경우 "문자열이 비어 있습니다."를 출력하세요.

number = 0
user_input = input("문자열을 입력하세요")
if user_input == "":
  print("문자열이 비어 있습니다.")
else:
  number = len(str(user_input))
  print(number)
