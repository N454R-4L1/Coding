class Electronics:
    def __init__(self, company, a_type):
        self.brand = company
        self.gadget_type = a_type

    def print_details(self):
        return f"Brand : {self.brand} \nType : {self.gadget_type}"


class Pocket_gadget(Electronics):

    pass

class Phones(Pocket_gadget):

    def printit(self):
        return f"Well Done !!"


iphone = Phones("Apple", "Smartphone")
print(iphone.print_details())