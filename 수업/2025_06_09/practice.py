# 문자열 1줄 출력
print("Hello, world")

# 문자열 2줄 출력
print("Hello")
print("World")

# join 문법 "원하는형태".join
words = ["Hello", "List", "Python"]
result = " ".join(words)
print(result)

# replace 문법
words = ["Hello,", "List", "Python", "replace/"]
redirect = [w.replace(",", " ") for w in words]
result = " ".join(redirect)
print(result)

# list 사용
fruit = ["apple", "banana", "kiwi", "melon"]
compu = ["computer", "mouse", "keyboard"]
book = [fruit, compu]
print(book)

# 중첩 리스트 book 하나의 리스트로 풀기
flat_list = []
for sublist in book:
  for item in sublist:
    flat_list.append(item)
print(", ".join(flat_list))

# 문자열




