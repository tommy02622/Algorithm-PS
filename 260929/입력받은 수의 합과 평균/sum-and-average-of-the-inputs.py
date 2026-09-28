# 변수 선언 및 입력
n = int(input())

# 합을 구합니다.
sum_val = 0
for _ in range(n):
    score = int(input())
    sum_val += score
    
# 평균을 구합니다.
avg = sum_val / n

print(f"{sum_val} {avg:.1f}")
