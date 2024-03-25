import sys

total_lines = 0
if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        for line in lines:
            if not line.startswith("#") and not line.strip() == "":
                total_lines += 1
except FileNotFoundError:
    print("File does not exist")

file_name = sys.argv[1]


if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif not file_name.endswith(".py"):
    print("Not a Python file")
    sys.exit(1)
else:
    print(f"There are {total_lines} lines in your code")
