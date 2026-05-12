"""
If you don't feel like running this, just paste this into your browser's address bar to test:
https://cs361-calculator-microservice.onrender.com/calculate?m1=5&m2=10&d1=4&d2=2
Format the output of your monolith to mirror the structure of the url above.
You must have either:
-- m1 and m2 (for multiplication)
-- d1 and d2 (for division)
-- m1, d1, and d2 (for combined)
Any other combination of parameters will return an error message.
You can also test division by zero by setting d2 to 0, which should also return an error message.
"""

import requests
URL = "https://cs361-calculator-microservice.onrender.com/calculate"

def test_calculator():
    print("testing multiplication...")
    response = requests.get(URL, params={'m1': 5, 'm2': 10})
    handle_response(response)

    print("\ntesting division...")
    response = requests.get(URL, params={'d1': 20, 'd2': 4})
    handle_response(response)

    print("\ntesting combined...")
    response = requests.get(URL, params={'m1': 5, 'd1': 20, 'd2': 4})
    handle_response(response)

    print("\nTesting Division by Zero...")
    response = requests.get(URL, params={'d1': 20, 'd2': 0})
    handle_response(response)

def handle_response(response):
    if response.status_code == 200:
        data = response.json()
        print(f"result: {data.get('result')}")
    else:
        try:
            data = response.json()
            print(f"Error ({response.status_code}): {data.get('error')}")
        except ValueError:
            print(f"Server returned a non-JSON error. Status Code: {response.status_code}")

if __name__ == "__main__":
    test_calculator()