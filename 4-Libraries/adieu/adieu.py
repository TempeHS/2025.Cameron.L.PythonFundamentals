import inflect

p = inflect.engine()
array_1 = []
while True:
    try:
        user = input("Enter names")
        name = array_1.append(user)
        print(f"Adieu, adieu, to {p.join(name)}")
    except EOFError:
        break
