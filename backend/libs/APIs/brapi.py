import requests
 
url = "https://brapi.dev/api/v2/crypto"
params = {
    'coin': 'BTC,ETC',
    'currency': 'BRL',
    'token': 'eJGEyu8vVHctULdVdHYzQd',
}

token = "pQY5mAcVsqbXRAbQGC99LP"

class brApi():
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}")