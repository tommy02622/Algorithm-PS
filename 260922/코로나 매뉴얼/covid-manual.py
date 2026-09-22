a_cold , a_tem = input().split()
a_tem = int(a_tem)
b_cold , b_tem = input().split()
b_tem = int(b_tem)
c_cold , c_tem = input().split()
c_tem = int(c_tem)
count =0

if a_cold  == "Y":
    if a_tem >=37:
        count+=1
if b_cold  == "Y":
    if b_tem >=37:
        count+=1
if c_cold  == "Y":
    if c_tem >=37:
        count+=1
if count >= 2:
    print("E")
else:
    print("N")