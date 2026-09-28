# 변수 선언, 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
sum_val = 0

# a부터 b까지 조건을 만족하는 수를 더합니다.
for i in range(a, b + 1):
    if i % 6 == 0 and i % 8 != 0:
        sum_val += i

# 출력
print(sum_val)
