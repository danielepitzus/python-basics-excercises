phrase = input("Enter a phrase: ")

new_phrase = ""
for i in range(len(phrase)):
    if i % 2 ==  0:
        new_phrase += phrase[i].upper()
    else:
        new_phrase += phrase[i]

print(new_phrase)

