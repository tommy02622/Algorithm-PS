y = int(input())

# 4의 배수이면서 100의 배수가 아니거나, 400의 배수인 경우
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("true")
else:
    print("false")