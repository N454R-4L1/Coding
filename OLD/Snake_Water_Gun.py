import random

lis = ["Snake", "Water", "Gun"]

ch = random.choice(lis)

print("      <======== WELCOME TO SNAKE, WATER AND GUN GAME ========>")
print("1 - Start \t\t0 - Exit")
k = int(input())
pts_p = 0
pts_c = 0
chances = 5

while k != 0 and chances != 0:

    choice = input("Choice :\n")

    if choice == "Snake" and ch == "Water":
        pts_p += 1
        print(ch)
        print("                                Chances Left ", chances)
        chances -= 1

    elif choice == "Snake" and ch == "Gun":
        pts_c += 1

        print(ch)
        print("                                Chances Left ", chances)
        chances -= 1

    elif choice == "Snake" and ch == "Snake":
        print(ch)
        print("                                Chances Left ", chances)
        chances -= 1

    elif choice == "Water" and ch == "Snake":
        pts_c += 1
        print(ch)
        print("                                Chances Left ", chances)
        chances -= 1

    elif choice == "Water" and ch == "Water":
        print(ch)
        print("                                Chances Left ", chances)
        chances -= 1

    elif choice == "Water" and ch == "Gun":
        pts_p += 1
        print(ch)
        print("                                Chances Left ", chances)
        chances -= 1

    elif choice == "Gun" and ch == "Water":
        pts_c += 1
        print(ch)
        print("                                Chances Left ", chances)
        chances -= 1

    elif choice == "Gun" and ch == "Snake":
        pts_p += 1
        print(ch)
        print("                                Chances Left ", chances)
        chances -= 1

    elif choice == "Gun" and ch == "Gun":
        print(ch)
        print("                                Chances Left ", chances)
        chances -= 1
    elif chances == 0:
        if pts_p > pts_c:
            print("YOU WIN ")
        elif pts_c > pts_p:
            print("YOU LOSE ")
        elif pts_p == pts_c:
            print("IT's A TIES ")

    k = int(input("WANT TO CONTINUE ?\n"))
