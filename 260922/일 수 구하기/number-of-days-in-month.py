n = int(input())

if (n %2 !=0 and n <=7) or (n%2 ==0 and n>=8):
    print("31")
elif (n %2 !=0 and n >=9) or (n%2 ==0 and n>=4):
    print("30")
else:
    print("28")



