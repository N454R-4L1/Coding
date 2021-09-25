import time
from functools import lru_cache


def print_details():
    return f"Welcome Enjoy your stay...!!"


@lru_cache(maxsize=10)
def loader(n):
    print("Loading [", end="")
    time.sleep(n)
    print(".", end="")
    time.sleep(n)
    print(".", end="")
    time.sleep(n)
    print(".", end="")
    time.sleep(n)
    print(".", end="")
    time.sleep(n)
    print(".", end="")
    time.sleep(n)
    print(".", end="")
    time.sleep(n)
    print("....", end="")
    time.sleep(n)
    print("....", end="")
    time.sleep(n)
    print("...", end="")
    time.sleep(n)
    print("......", end="")
    time.sleep(n)
    print("......]", end="")
    time.sleep(n)
    print("\tDone!")

    return n


def user():
    __passwd = {'n454r': "p4ssw0rd", 'root': "toor"}
    usenm = input("Username : ")
    password = input("Password : ")
    lis_user = ["n454r", "root"]
    flag = 0

    for item in lis_user:
        if usenm == item:
            if password == __passwd[usenm]:
                print("<< Welcome >>")
                flag = 1
            else:
                print("<< Incorrect Username or Password >>")

    return flag


class library():

    def __init__(self, n, nb):
        self.name = n
        self.no_of_books = nb

    @classmethod
    def printjob(cls):
        print("<<<< WELCOME TO LIBRARY >>>>")
        print("1 - Fiction     \n2 - Non -Fiction ")
        choice = int(input())


    # @classmethod
    # def main(cls):
    #     pass


new_lib = library("Library", "2")

if __name__ == '__main__':
    print("Enter Seconds : ")
    ch = int(input())
    print("Plugins Updating Please Wait..!")
    loader(ch)
    f = user()
    if f == 1:
        print(print_details())
        print(library.printjob())
    print('Thanks')
