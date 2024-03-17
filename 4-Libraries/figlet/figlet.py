from pyfiglet import Figlet
import sys


def main():
    figlet = Figlet()
    a_fonts = figlet.getFonts()

    if len(sys.argv) == 2:
        user_input = input("Enter text: ")
        print(figlet.renderText(user_input))

    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in a_fonts:
            figlet.setFont(font=sys.argv[2])
            user_input = input("Enter text: ")
            print(figlet.renderText(user_input))
        else:
            print("Invalid usage")
            sys.exit(1)

    else:
        print("Invalid usage")
        sys.exit(1)


if __name__ == "__main__":
    main()
