import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# 한글 폰트 깨지지 않게 설정
# plt.rc("font", family="Nanum Gothic") # Mac이나 리눅스에서 사용할 수 있음
plt.rc("font", family="Malgun Gothic")  # Windows에서 사용

# 베르누이 이벤트 설정
p = 0.01  # 아이템을 얻을 확률

# 문제 설정
trials = 1000  # 시도 횟수

# 베르누이 이벤트 발생 시뮬레이션
num_simulations = 10000 # 시뮬레이션 횟수
occur_counts = [] # 매회 시뮬레이션에서 이벤트 발생 횟수들 초기화

for _ in range(num_simulations): # 주어진 시뮬레이션 횟수만큼 반복
    occur_count = sum(np.random.rand(trials) < p)  # 이벤트 발생 횟수 계산
    occur_counts.append(occur_count) # 이벤트 발생 횟수 기록

# 시뮬레이션 시각화(막대)
occur_counts_unique, counts = np.unique(occur_counts, return_counts=True)  # 유일한 이벤트 발생 횟수 및 카운트
t_sim = occur_counts_unique
pmf_sim = counts/len(occur_counts)
plt.bar(t_sim, pmf_sim, label="시뮬레이션", alpha=0.5, width=0.3)


# 이론 시각화(선)
t = np.arange(min(occur_counts), max(occur_counts) + 1)
pmf = binom.pmf(t, trials, p) 
plt.plot(t, pmf, label="이론", marker="o", linestyle="--")

# 최종 설정 및 이미지 출력
plt.title("{}회를 시도했을 때 아이템을 얻을 횟수: 이론과 시뮬레이션의 비교\n이론: 평균 {}회, 시뮬레이션: 평균{}회"
          .format(trials, trials * p, np.mean(occur_counts)))
plt.xlabel("이벤트 발생 횟수")
plt.xticks(t_sim)
plt.xlim(min(occur_counts), max(occur_counts) + 1)
plt.ylabel("시뮬레이션에서 기록된 확률(상대빈도)")
plt.legend()
plt.grid()
plt.savefig("Images\이산시간_득템횟수.png")