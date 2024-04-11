with open("myText.txt", "r") as file:
    number = int(file.read())
    number += 1

with open("myText.txt", "w") as file:
    file.write(str(number))
