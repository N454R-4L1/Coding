import pip._vendor.requests
# print("String :")
# txt = input()

# def un_cipher(s):
#     t =""

#     for item in range(len(s)):
#         char = s[item]
#         if ord(char) == 32:
#             t +=  ' '
#         else:
#             t += chr((ord(char) + 2 - 97) % 26 + 97)      


#     return t

# print(un_cipher(txt))


data = open("small.txt").read();
# frequencies = {} 
  
# for char in input_string: 
#    if char in frequencies:
#       frequencies[char] += 1
#    else: 
#       frequencies[char] = 1

# print (" frequency is :\n {}".format(str(frequencies)))


# re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))