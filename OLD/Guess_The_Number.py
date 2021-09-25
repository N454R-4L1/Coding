print("      <========WELCOME TO GUESS THE NUMBER========>")
print("Type 777 for HINT Before Your 7th Guess ")
print("HINT will reduced your chances to 2")
n = 18

t = 9
print("GUESS THIS Number : XX")
flag = 0
while (t != 0) :
    print(t, " guess :")
    g = int(input())

    if(g==n) :
        print("\nCongratualtions,you've guessed the right number !!!!")
        print("Number of Guesses you took :",(9-t)+1)
        flag = 1
        break
    elif g == 777 and t > 7:
        t = 2
        print("NOW..\nYou've taken the so Guess left :", t)
        print("HINT : RUN THROUGH THE TABLE OF 9")
    elif g<n :
        print(g,"is lesser than the number")
        t -= 1
        print("                                       Guess Left :",t)
    elif g>n :
         print(g,"is greater than the number" )
         t -= 1
         print("                                       Guess Left :", t)

if flag == 0 and t==0:
    print("GAME OVER....\tBETTER LUCK NEXT TIME")