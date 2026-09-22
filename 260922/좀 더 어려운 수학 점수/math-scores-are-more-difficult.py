# 1. A와 B의 점수 입력받기
a_math, a_eng = map(int, input().split())
b_math, b_eng = map(int, input().split())

# 2. 우선순위 1: 수학 점수 비교
if a_math > b_math:
    print("A")
elif b_math > a_math:
    print("B")
    
# 3. 우선순위 2: 수학 점수가 같다면 영어 점수 비교
else:  
    if a_eng > b_eng:
        print("A")
    else:
        print("B")