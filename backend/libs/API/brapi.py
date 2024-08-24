import requests

class brApi():
    def __init__(self) -> None:
        self.token = "pQY5mAcVsqbXRAbQGC99LP"
        self.url = "https://brapi.dev/api/available?search=TR&token=%d"
        
    def get_request_stock(self) -> dict:
        response = requests.get(self.url, params=self.token)
        
        return response
    
if __name__ == "__main__":
    pass