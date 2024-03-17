import requests
import sys
import json

argv = sys.argv

def main():
    # verify argv
    coins = verify_argv()

    # get USD rate
    # acess API, read json file and extract key
    rate = get_rate()

    # calculate and print (argv x bitcoin price)
    print(f"${(rate * coins):,.4f}")

def get_rate():
    try:
        rate = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        rate = rate.json()
        rate = float(rate["bpi"]['USD']['rate_float'])
        return rate
    except requests.RequestException:
        pass

def verify_argv():
    if len(argv) < 2:
        print("Missing command-line argument")
        sys.exit
    elif len(argv) > 2:
        print("Too many command-line arguments")
        sys.exit
    else:
        try:
            argv_one = argv[1]
            return float(argv_one)
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit

main()
