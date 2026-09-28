# 변수 선언, 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
sum_val = 0

# a부터 b까지의 수를 더합니다.
for i in range(a, b + 1):
    sum_val += i

# 출력
print(sum_val)
