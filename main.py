import random
symbolvar = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

genpass = ""
length = int(input("Какая длина вашего пароля от 4 - 16 "))
if length >= 4 :
    for i in range(length):
        genpass += random.choice(symbolvar)

else:
    print("я не буду работать")
print(genpass)