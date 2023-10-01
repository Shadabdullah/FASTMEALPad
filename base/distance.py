import requests

KEY = 'Cgqn94edOGXaCPrr76Zv9JMNNK9XLv4E'
fromLocation = 'Qortuba Block - 4 Street - 2 House - 7 Kuwait'
toLocation = 'MUBARAK AL - ABDULLAH BLOCK-1 STREET-115 BUILDING-1 UNIT-33 KUWAIT'

url = f'https://www.mapquestapi.com/directions/v2/route?key={KEY}&from={fromLocation}&to={toLocation}'

response = requests.get(url)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    data = response.json()
    print("Response data:")
    print(data)
else:
    print("Error:", response.status_code)
    print("Response:", response.text)