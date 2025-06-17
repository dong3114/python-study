import matplotlib.pyplot as plt
import koreanize_matplotlib

# x축 데이터와 y축 데이터 준비
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# 기본 플롯 생성
# plt.plot(x,y)

# 플롯 생성 및 스타일 추가
plt.plot(x, y, label='샘플 데이터', color='blue', linestyle='--', marker='o')

# 축, 제목, 레이블 추가하기
plt.xlabel('x축 이름')
plt.ylabel('y축 이름')
plt.title('플롯 제목')
plt.legend()  # 범례 추가

# x축과 y축 눈금 설정
# rotation은 보여질 글자의 기울기 설정해줌
plt.xticks([1, 2, 3, 4, 5], ['One', 'Two', 'Three', 'Four', 'five'], rotation=45)
plt.yticks([10, 20, 25, 30, 35],  ['Ten', 'Twenty', 'Twenty-Five', 'Thirty', 'Thirty-Five'])

# 플롯 표시
plt.show()
