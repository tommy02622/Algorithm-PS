a, b = map(int, input().split())

# Please write your code here.

def power(a,b):
    cnt = 1
    for _ in range(1,b+1):
        cnt*=a
    return cnt

print(power(a,b))