# 변수 선언 및 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
sum_val = 0
cnt = 0

# a부터 b까지의 수 중 5 또는 7의 배수인 수들을 더합니다.
for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        cnt += 1

# a부터 b까지의 수 중 5 또는 7의 배수인 수들의 평균을 구합니다.
avg = sum_val / cnt

# 출력
print(f"{sum_val} {avg:.1f}")
