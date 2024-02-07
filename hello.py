def hello(to="world"):
    print("Hello,", to)


hello()
# Ask user for name, Remove whitespace from str and capitalize users name
name = input("What's your name?").strip().title()
hello(name)
