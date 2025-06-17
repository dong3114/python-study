import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  # numpy 추가 (np.sin, np.cos 사용)

# 그래프 생성 (6x3 크기의 figure와 ax 설정, aspect='equal'로 원형 유지)
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# 재료 목록 (파이 조각별 레이블)
recipe = ["225 g flour",
          "90 g sugar",
          "1 egg",
          "60 g butter",
          "100 ml milk",
          "1/2 package of yeast"]

# 각 재료의 양 (파이 차트 비율 설정)
data = [225, 90, 50, 60, 100, 5]

# 도넛형 차트 생성 (wedgeprops로 내부 빈 원형 조정, startangle로 회전)
wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

# 주석 스타일 설정 (사각형 박스 스타일 및 화살표 속성)
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

# 각 조각에 라벨(재료) 추가
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1  # 각 조각의 중심각 계산
    y = np.sin(np.deg2rad(ang))  # y 좌표 변환 (각도를 라디안으로 변환 후 sin 적용)
    x = np.cos(np.deg2rad(ang))  # x 좌표 변환 (cos 적용)
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]  # 텍스트 정렬 방향 결정
    connectionstyle = f"angle,angleA=0,angleB={ang}"  # 화살표 스타일 적용
    kw["arrowprops"].update({"connectionstyle": connectionstyle})  # 화살표 스타일 업데이트
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)  # 주석 추가

# 그래프 제목 추가
ax.set_title("Matplotlib bakery: A donut")

# 그래프 출력
plt.show()