dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


sum = 0

while True:
    try:
        user = input("What would you like to order? ")
        if user in dict:
            sum += dict[user]
            out = format(sum, ".2f")
        print(f"Total: ${out}")
    except EOFError:
        break
