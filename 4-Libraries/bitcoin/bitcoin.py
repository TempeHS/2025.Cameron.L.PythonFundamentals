import sys
import requests

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    request = r.json()
    bitcoin = 
except requests.RequestException:
    sys.exit
    print("Missing command-line argument")
except ValueError:
    sys.exit
    print("Command-line argument is not a number")
