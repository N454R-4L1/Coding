class Cool_class:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def print_details(self):
        return f"Name is {self.name} and age {self.age}"

    @classmethod
    def change_name(cls):
        print("Want To Change Your Name ?")
        choice = input()
        if choice == "Yes":
            newname = input()
            cls.name = newname



input1 = input("Name :")
input2 = int(input("Age :"))
person = Cool_class(input1, input2)
print(person.print_details())
print(person.change_name())
print(person.print_details())
