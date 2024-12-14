import requests

def get_exchange_rate(source_currency: str, target_currency: str) -> float:
    """Function that gets real-time exchange rates from the API."""
    # API key and URL
    api_key = '1523f0bb8a0b9c9f8de061e4'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{source_currency}'

    try:
        # GET request
        response = requests.get(url)
        data = response.json()

        # API success check
        if response.status_code == 200 and data.get('result') == 'success':
            conversion_rates = data.get('conversion_rates')
            if target_currency in conversion_rates:
                exchange_rate = conversion_rates[target_currency]
                exchange_rate = round(exchange_rate, 2)
                return exchange_rate
            else:
                print(f"Currency {target_currency} not found in the API response.")
                return 1.0  # Default exchange rate of 1 if currency not found
        else:
            print("Failed to retrieve exchange rates from the API.")
            return 1.0  # Default exchange rate of 1

    except Exception as e:
        # Handle exceptions, connection errors, API errors, etc.
        print(f"An error occurred: {e}")
        return 1.0  # Default exchange rate of 1
