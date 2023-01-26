user_word = input("Ingresa la palabra")
user_word = user_word.upper()
new_word = ""
for letter in user_word:
    if letter not in ("A","E","I","O","U"):
        new_word += letter
print (new_word)

a = (10,20,12,1,2)
print(a.__str__())

