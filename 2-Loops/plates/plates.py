def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    found_letter = False
    for char in s:
        if char.isalpha():
            found_letter = True
        elif char.isdigit():
            if char == "0":
                return False  # If the first digit is '0', the plate is invalid
            elif found_letter:
                return True
    return False
    return (
        2 <= len(s) <= 6
        and s.isalnum()  # Check if all characters are alphanumeric
        and s[:2].isalpha()  # Check if the first two characters are letters
        and s[-1].isdigit()  # Check if the last character is a digit
        and not s.startswith("0")  # Check if the plate doesn't start with '0'
        and [0] != "0"
    )


main()
