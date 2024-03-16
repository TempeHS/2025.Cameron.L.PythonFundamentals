import sys
import requests


def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        request = r.json()
        bitcoin = request["bpi"]["USD"]["rate_float"]
        amount = bitcoin * value
        print(f"${amount:,.4f}")
    except requests.RequestException:
        print("Failed to get Bitcoin price")
        sys.exit(1)


if __name__ == "__main__":
    main()
