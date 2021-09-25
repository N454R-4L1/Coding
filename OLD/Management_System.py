print("||========================== Management System ==========================||")
print("               WELCOME")
print("1 - Start               2 - Exit")
k = int(input())
while k != 2 :

     def getdate():
        import datetime
        return datetime.datetime.now()

     print("1 - Appending           2 - Retrieval  ")
     x = int(input())

     if x == 2 :

         with open("Management.txt","r") as f :

             con = f.read()
             print()
             print(getdate())
             print()
             print(con)
         print()
         print("Want to Continue ?")
         k = int(input())

     elif x == 1 :

         with open("Management.txt", "a") as f:

             f.write("\n")
             f.write(input())

         print("Your Details Are Successfully Written ...!!")
         print()
         print("Want to Continue ?")
         k = int(input())

     else :
            print("Invalid Input")
            print()
            print("Want to Continue ?")
            k = int(input())

print()
print("THANK YOU ")
print("HAVE A GOOD DAY !!")