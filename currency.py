import requests
import json
import argparse

def input(to, fromCurrency, amount):

    return f"https://api.apilayer.com/fixer/convert?to={to}&from={fromCurrency}&amount={amount}"


payload = {}
headers = {
    "apikey": "5nm48Mhn2kKxwSk71Cpce0Pbr7i5tM7v"
}

parser = argparse.ArgumentParser()

parser.add_argument('--to', type=str)
parser.add_argument('--fromCurrency', type=str)
parser.add_argument('--amount', type=str)

args = parser.parse_args()
print(args)
args = vars(args)

print(args)
url = input(args['to'], args['fromCurrency'], args['amount'])
response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)
