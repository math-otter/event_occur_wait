import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

# 한글 폰트 깨지지 않게 설정
# plt.rc("font", family="Nanum Gothic") # Mac이나 리눅스에서 사용할 수 있음
plt.rc("font", family="Malgun Gothic")  # Windows에서 사용

# 랜덤 시드 설정
rs = np.random.RandomState(42)

# 베르누이 이벤트 설정
p = 0.01  # 베르누이 이벤트의 강도

# 문제 설정
x = 5  # 목표 발생 횟수를 x로 고정, 이벤트 대기 시간 t를 논의

# 베르누이 이벤트 대기 시간 t의 시뮬레이션
n = 10000 # 시뮬레이션 횟수
t_list = [] # 매회 시뮬레이션에서 이벤트 대기 시간 t들을 기록할 공간

for _ in range(n): # 주어진 시뮬레이션 횟수만큼 반복
    t = 0 # 매회 시뮬레이션에서 이벤트 대기 시간 초기화
    count = 0 # 매회 시뮬레이션에서 이벤트 발생 횟수 초기화
    
    while count < x: # 매회 시뮬레이션에서 발생 횟수 = 목표 발생 횟수를 만족할 때까지 반복
        t += 1 # 발생 여부에 관계 없이 시간 +1
        if rs.rand() < p: # 0~1 난수가 p보다 작으면(p의 확률로)
            count += 1 # 매회 시뮬레이션에서 이벤트 발생 횟수 +1
    
    t_list.append(t) # 매회 시뮬레이션에서 이벤트 대기 시간 기록

# 시뮬레이션 시각화(막대)
t, t_freq = np.unique(t_list, return_counts=True) # t의 유니크한 값으로 가로축 구성
pmf = t_freq / len(t_list) # t의 상대빈도로 세로축 구성
plt.bar(t, pmf, label="시뮬레이션", alpha=0.5, width=0.3)

# 이론 시각화(점선) (이벤트가 발생하지 않은 횟수 t-x를 사용하게 되어있음)
plt.plot(t, nbinom.pmf(t-x, x, p), label="이론", marker="o", linestyle="--")

# 최종 설정 및 이미지 출력
title = ("아이템을 {}회 얻기 까지 대기 시간: 이론과 시뮬레이션의 비교"
         "\n이론: 평균 {}회, 시뮬레이션: 평균 {}회").format(x, x / p, np.mean(t_list))
plt.title(title)
plt.xlabel("시뮬레이션에서 기록된 이벤트 대기 시간")
# plt.xticks(t) # t의 유니크한 값을 가로축에 표시 -> 너무 많은 종류의 값들이 있어 안하는 것이 좋음
plt.xlim(min(t), max(t) + 1) # 시뮬레이션에서 얻은 t의 범위만큼 설정
plt.ylabel("시뮬레이션에서 기록된 확률(상대빈도)")
plt.legend()
plt.grid()
plt.savefig(r"Images\2_이산 시간_대기 시간")
