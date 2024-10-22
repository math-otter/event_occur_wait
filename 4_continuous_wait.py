import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# 한글 폰트 깨지지 않게 설정
# plt.rc("font", family="Nanum Gothic") # Mac이나 리눅스에서 사용할 수 있음
plt.rc("font", family="Malgun Gothic")  # Windows에서 사용

# 랜덤 시드 설정
rs = np.random.RandomState(42)

# 푸아송 이벤트 설정
lb = 5  # 푸아송 이벤트의 강도 (단위 시간: 1달)
unit_time = 30 # 단위 시간의 양
p = lb / unit_time # 발생 빈도를 발생 확률로 변환

# 문제 설정
x = 1000  # 목표 발생 횟수를 x로 고정, 이벤트 대기 시간 t를 논의

# 푸아송 이벤트 대기 시간 t의 시뮬레이션
n = 10000 # 시뮬레이션 횟수
t_list = [] # 매회 시뮬레이션에서 이벤트 대기 시간 t들을 기록할 공간

for _ in range(n): # 주어진 시뮬레이션 횟수만큼 반복
    t = 0 # 매회 시뮬레이션에서 이벤트 대기 시간 초기화
    count = 0 # 매회 시뮬레이션에서 이벤트 발생 횟수 초기화
    
    while count < x: # 매회 시뮬레이션에서 발생 횟수 = 목표 발생 횟수를 만족할 때까지 반복
        t += 1 # 발생 여부에 관계 없이 시간 +1
        count_unit = sum(rs.rand(unit_time) < p) # 단위 시간 내 이벤트 발생 횟수를 한번에 계산
        count += count_unit # 매회 시뮬레이션에서 이벤트 발생 횟수가 단위시간 내 발생 횟수만큼 증가

    t_list.append(t) # 매회 시뮬레이션에서 이벤트 대기 시간 기록

# 시뮬레이션 시각화(히스토그램)
plt.hist(t_list, bins=range(0, max(t_list) + 1), density=True, label="시뮬레이션", alpha=0.5)

# 이론 시각화(곡선)
t = np.linspace(min(t_list), max(t_list), num=len(t_list))
plt.plot(t, gamma.pdf(t, x, loc=0, scale=1/lb), label="이론", linestyle="--")

# 최종 설정 및 이미지 출력
title = ("{}명의 고객 이탈까지 대기 시간: 이론과 시뮬레이션의 비교"
         "\n이론: 평균 {}개월, 시뮬레이션: 평균 {}개월").format(x, x / lb, np.mean(t_list))
plt.title(title)
plt.xlabel("시뮬레이션에서 기록된 이벤트 대기 시간")
# plt.xticks(t) # t의 유니크한 값을 가로축에 표시 -> 너무 많은 종류의 값들이 있어 안하는 것이 좋음
plt.xlim(min(t_list), max(t_list) + 1) # 시뮬레이션에서 얻은 t의 범위만큼 설정
plt.ylabel("시뮬레이션에서 기록된 확률(상대빈도)")
plt.legend()
plt.grid()
plt.savefig(r"Images\4_연속 시간_대기 시간")
