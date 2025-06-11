score = 85
if score >= 70:
  print("합격입니다.")
else:
  print("불합격입니다.")

# 1번 문제
print(10 // 3)  
# 2번 문제
print(10 % 4)  
# 3번 문제
print(3 ** 2)

n = 4
if n % 2 == 0:
	print('짝수입니다')
else:
	print('홀수입니다')

# 초기 리스트
tests = [13, (23, 14), {"a": 1, "b": 13}, 'happy', 5]

# 조건문
if tests[0] == 1:
    tests.pop()
# 13, (23, 14), {"a": 1, "b": 13}, 'happy', 5
    
elif tests[2] == len(tests):
    tests.append("balanced")
# 13, (23, 14), {"a": 1, "b": 13}, 'happy', 5
    
elif "happy" in tests:
    index = tests.index("happy") # 'happy'의 인덱스값 3
    tests[index] = tests[index].replace("happy", "excited") 
# 13, (23, 14), {"a": 1, "b": 13}, 'excited', 5    

elif type(tests[2])==dict:
	tests[-2]= sum(tests[2].values())
# 조건이 참이지만 이전 흐름에서 참이었기때문에 pass
else:
    pass
print("변경된 리스트:", tests[-3:])
# [{"a": 1, "b": 13}, 'excited', 5]

# 반복문
total = 0
for i in range(1, 11):
     total += i
print("총합", total)


for i in range(1,8):
    if i == 2:
          pass
    if i == 3:
         print("continue!")
         continue
    if i == 6:
         print("break!")
         break
    print(i)

# While 반복문
monster_hp = 10
while monster_hp >= 0:
     if monster_hp %2 == 1:
          print("몬스터가 너무 강합니다.")
          break
     elif monster_hp % 2 == 0:
          print(f"몬스터 체력: {monster_hp}")
          monster_hp -= 2
          print("용사가 몬스터를 공격합니다! (체력 -2)")
          if monster_hp == 0:
            print("몬스터가 쓰러졌습니다.")
            break
          continue
  
# for 문
user_num = []
user_input = int(input("정수를 입력해주세요: "))
for i in range(user_input + 1):
    if i%3 == 0: 
         continue
    user_num.append(i)
print(user_num)
print(" ".join(map(str, user_num)))

# while문
user_num = []
user_input = int(input("정수를 입력해주세요: "))
count = 1
while count <= user_input:
     if count % 3 != 0:
          user_num.append(count)
     count += 1
print(user_num)
print(" ".join(map(str, user_num)))

# 마무리 퀴즈
# 1. `range(3, 8)`의 출력 결과는? 3,4,5,6,7
# 2. `if not True:` 는 실행될까? 조건이 false임 실행 x
# 3. `while`문에서 빠져나오기 위한 키워드는? break
# 4. 아래 코드는 총 몇 번 실행될까? 6번

# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 
# return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

