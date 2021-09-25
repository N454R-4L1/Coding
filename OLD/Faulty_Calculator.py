print("THE FAULTY CALCULATOR")

print("1-start"
      "\n0-exit")
x = int(input("ENTER CHOICE !!! : "))
while x == 1:
    var1 = int(input("FIRST NUMBER : "))
    var2 = int(input("SECOND NUMBER : "))

    print("Enter Operation Type : ")
    ch = input()
    op = { "Addition" : var1+var2, "Subtraction" : var1-var2, "Multiplication" : var1*var2,
           "Division" : var1/var2}

    if ((var1==45)and(var2==3)and(ch=="Multiplication")):
       print(555)
    elif ((var1==56)and(var2==9)and(ch=="Addition")):
        print(77)
    elif ((var1==56)and(var2==6)and(ch=="Division")):
        print(4)
    else:
        print(op[ch])

    print("Want to Continue ??")

    x = x = int(input("ENTER CHOICE !!! : "))



