from collections import Counter

# 문제 7
# max 메서드 사용
numbers_max = [1,7,2]

def max_number(numbers_max):
  return max(numbers_max)
print(max_number(numbers_max))

# max 메서드 미사용
def max_number2(numbers_max):
  n = len(numbers_max)
  change = True
  while change:
    change = False
  for i in range(n - 1):
    first_num = numbers_max[i]
    second_num = numbers_max[i + 1]
    first_idx = i
    second_idx = i + 1
    if first_num > second_num:
      numbers_max[first_idx], numbers_max[second_idx] = numbers_max[second_idx], numbers_max[first_idx]
  print(f"정렬 종료: {numbers_max}")
  return numbers_max[-1]
print("max 미사용")
print(max_number2(numbers_max))

# 8번
words = ["hi", "apple"]
def word_lens(words):
  word_len = []
  for i in range(len(words)):
    word_len.append(len(words[i]))
  return word_len
print(word_lens(words))

# 9번
lst = ["abc", "de"]
def reverse_str(lst):
  re = []
  for i in range(len(lst)):
    word = ''.join(reversed((lst[i])))
    re.append(word)
  return re
print(reverse_str(lst))

# 10번
numbers = [3, 10, 7, 30]
n = 20
def number_filter(numbers, n):
  return [i for i in numbers if i > n]
print(number_filter(numbers, n))

# 11번 튜플 형태 (양수 개수, 음수 개수)
numbers = [-1, 0, 2, -3, 5]
def num_tuple(numbers):
  yang = [i for i in numbers if i > 0]
  um = [i for i in numbers if i < 0]
  tu = (len(yang) , len(um))
  return tu
print(num_tuple(numbers))

# 12번 
test_text = "aaabbc"
def text_pre(test_text):
  result = ""
  count = 1
  for i in range(len(test_text) - 1):
    if test_text[i] == test_text[i+1]:
      count += 1
    else:
      result += f"{test_text[i]}{count}"
      count = 1
  # 마지막 인덱스
  result += f"{test_text[-1]}{count}"
  return result
print(text_pre(test_text))

# 13번
numbers = [3,7,1]
def min_max(numbers):
  max_num = max(numbers)
  for i in range(len(numbers)):
    if numbers[i] == max_num:
      tu = (numbers[i], i)
  return tu
print(min_max(numbers))

# 14번
words = ["hi", "apple", "banana"]
def five_word(words):
  return [i for i in words if 5 <= len(i)]
print(five_word(words))

# 15번
words = ["interview", "internet", "interval"]
def same_word(words):
  word = ""
  for i in range(len(words[0])):
    key = True
    count = 0
    while key:
      key = False
      fir = words[count]
      sec = words[count + 1]
      if fir[i] == sec[i]:
        count += 1
        key = True
    if count == len(words):
      word += words[0][i]
  return word
print(same_word(words))


  