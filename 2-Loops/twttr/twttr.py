def main():
    user = input("Write anything")
    user = (
        user.replace("a", "")
        .replace("e", "")
        .replace("i", "")
        .replace("o", "")
        .replace("u", "")
    )
    print("Here it is without vowels:", user)


main()
