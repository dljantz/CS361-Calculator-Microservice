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