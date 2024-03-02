from random import *

elements = elements = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
length = int(input("intruduzca la longitud de su contraseña "))



password = ""



for i in range (length):
    password += choice(elements)


print(password)
