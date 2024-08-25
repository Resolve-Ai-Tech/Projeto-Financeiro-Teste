import requests

class brApi():
    def __init__(self) -> None:
        self.token = "pQY5mAcVsqbXRAbQGC99LP"
        self.urlStock = "https://brapi.dev/api/available?search=TR&token=%d"
        self.urlAcao = "" # 2 variaveis dentro (acao e token)
        
    def get_request_stock(self) -> dict:
        response = requests.get(self.urlStock, params=self.token)
        
        return response
    
if __name__ == "__main__":
    pass