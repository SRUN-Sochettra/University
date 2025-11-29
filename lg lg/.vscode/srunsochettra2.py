import requests

def get_exchange_rate(base, target):
    api_key = ""
    
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get("result") == "success" and target in data.get("conversion_rates", {}):
            rate = data["conversion_rates"][target]
            print(f"1 {base} = {rate} {target}")
        else:
            error_type = data.get("error-type", "Unknown error")
            print(f"Could not get rate. Reason: {error_type}")
            
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Please check currency codes.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err} - Please check your internet connection.")
    except KeyError:
        print("Error: Could not parse the currency data.")

base = input("Enter base currency (e.g., USD, EUR, THB, AUD, VND, CNY): ")
target = input("Enter target currency (e.g., USD, EUR, THB, AUD, VND, CNY): ")

get_exchange_rate(base.upper(), target.upper())