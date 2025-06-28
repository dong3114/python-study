from datetime import time

# 출근 희망 시간 + 10분
# 1013 -> 10시 13분

# schedules: 출근희망시각담은 1차원 정수배열
# timelogs: 일주일간 출근한 시각을 담은 2차원 배열
# startday: 이벤트 시작요일 [1='월요일' ... 7='금요일']
# return: 상품을 받을 직원 수
def solution(schedules, timelogs, startday):
    answer = 0
    day_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    s_day = day_list[startday-1]
    schedules = si_bun(schedules)
    for i in range(len(timelogs)):
        timelogs[i] = si_bun(timelogs[i])
    
    

    return answer

def si_bun(lit):
    result = []
    for num in lit:
        hour = num // 100
        minute = num % 100
        result.append(time(hour, minute))
    return result

schedules = [700,800,1100]
timelogs = [[710, 2359, 1050, 700, 650, 631, 659], 
            [800, 801, 805, 800, 759, 810, 809], 
            [1105, 1001, 1002, 600, 1059, 1001, 1100]]
startday = 5
