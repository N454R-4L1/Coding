def x_and_o(st):
    c_x = 0
    c_o = 0
    x = 'x'
    o = 'o'
    flag = 0

    if st.isalpha():
        for i in st:
            if i != x and i != o:
                flag = 0

            elif i == x:

                c_x += 1
            elif i == o:

                c_o += 1

    if c_x == c_o and c_x != 0:
        flag = 1

    if flag == 0:
        return False

    else:
        return True


if __name__ == '__main__':
    print("String Please : ")
    string = input()
    print(x_and_o(string))
