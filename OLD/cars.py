# import urllib3

def cars_needed(passengers):


    global no_cars
    if passengers % 5 == 0 :
        no_cars = int(passengers/5.0)
    else :
        c = int(passengers/5.0)
        temp = passengers - (c*5)
        if temp < 5:
            no_cars = c+1

    return f"{no_cars} cars are needed. "


if __name__ == '__main__':
    num = int(input("How many Passengers??\n"))
    print(cars_needed(num))
