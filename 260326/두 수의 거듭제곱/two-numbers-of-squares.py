a, b = map(int, input().split())

# Please write your code here.

def A(a,b):
    cnt = 1
    for _ in range(1,b+1):
        cnt*=a
    return cnt

print(A(a,b))