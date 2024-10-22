import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

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
unit_time_num = 12
t = unit_time_num * unit_time  # 대기 시간을 t로 고정, 이벤트 발생 횟수 x를 논의

# 푸아송 이벤트 발생 횟수 x의 시뮬레이션
n = 10000 # 시뮬레이션 횟수
x_list = [] # 매회 시뮬레이션에서 이벤트 발생 횟수 x들을 기록할 공간

for _ in range(n): # 주어진 시뮬레이션 횟수만큼 반복
    x = sum(rs.rand(t) < p) # 주어진 t시간 동안 이벤트 발생 횟수를 한번에 계산
    x_list.append(x) # 매회 시뮬레이션에서 이벤트 발생 횟수 기록

# 시뮬레이션 시각화(막대)
x, x_freq = np.unique(x_list, return_counts=True) # x의 유니크한 값으로 가로축 구성
pmf = x_freq / len(x_list) # x의 상대빈도로 세로축 구성
plt.bar(x, pmf, label="시뮬레이션", alpha=0.5, width=0.3)

# 이론 시각화(점선)
plt.plot(x, poisson.pmf(x, lb * unit_time_num), label="이론", marker="o", linestyle="--")

# 최종 설정 및 이미지 출력
title = ("1년({}개월)에 이탈하는 고객의 수: 이론과 시뮬레이션의 비교"
         "\n이론: 평균 {}명, 시뮬레이션: 평균 {}명").format(unit_time_num, lb * unit_time_num, np.mean(x_list))
plt.title(title)
plt.xlabel("시뮬레이션에서 기록된 이벤트 발생 횟수")
# plt.xticks(x) # x의 유니크한 값을 가로축에 표시 -> 너무 많은 종류의 값들이 있어 안하는 것이 좋음
plt.xlim(min(x), max(x) + 1) # 시뮬레이션에서 얻은 x의 범위만큼 설정
plt.ylabel("시뮬레이션에서 기록된 확률(상대빈도)")
plt.legend()
plt.grid()
plt.savefig(r"Images\3_연속 시간_발생 횟수")
