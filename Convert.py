import requests, json, os

"""
Get an API KEY from: https://free.currconv.com.
"""

API_KEY = "CHANGE ME"

def Convert(CUR1, CUR2, AMOUNT):
    return AMOUNT * json.loads(requests.get(f'https://free.currconv.com/api/v7/convert?q={CUR1}_{CUR2}&compact=ultra&apiKey={API_KEY}').text)[f'{CUR1}_{CUR2}']

if __name__ == "__main__":
    while True:
        A = input("From: ")
        B = input("To: ")
        C = input("Amount: ")
        os.system('cls')
        print(Convert(A, B, int(C)))