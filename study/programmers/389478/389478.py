import numpy as np

def solution(n, w, num):
    answer = 0
    if n % w == 0: l = n // w
    else: l = (n // w) + 1
    box = np.zeros((l,w), dtype=int)
    i = 1
    input_num = 1
    while (input_num <= n):
      if (i-1) % 2 == 0: 
        for k in range(len(box[-i])):
          if input_num > n: break
          box[-i][k] = input_num
          input_num += 1
      else:
         for k in range(len(box[-i])):
            if input_num > n: break
            box[-i][-(k+1)] = input_num
            input_num += 1
      i += 1
    indexes = [j for j, k in enumerate(box[0]) if k == 0]
    rows, cols = np.where(box == num)
    row, col = rows[0], cols[0]
    if col in indexes: answer = row
    else: answer = row+1
    print(box)
    return answer 
    
lll = solution(13,3,6)

print(lll)