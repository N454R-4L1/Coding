print("N :")
n = int(input())

print("1 - True \n0 - False")
b = int(input())
flag = False

if b==1 : flag = True
else : flag = False

if (flag == True):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")
elif (flag== False) :
    for i in range(n, 0, -1):
        for j in range(0,i):
            print("*", end=" ")
        print("\r")

