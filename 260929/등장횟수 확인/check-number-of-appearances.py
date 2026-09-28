# 변수 선언, 입력
cnt = 0
for _ in range(5):
    a = int(input())
    
    if a % 2 == 0:
        cnt += 1

# 출력
print(cnt)
