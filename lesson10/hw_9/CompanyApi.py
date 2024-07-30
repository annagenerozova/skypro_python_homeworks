import allure
import requests

class CompanyApi:
    # Инициализация 
    def __init__(self, url) -> None:
        self.url = url
    
    @allure.step("api. Получить список компаний через API")  
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()
    
    @allure.step("api. Получить токен авторизации для пользователя {user}:{password}")
    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    @allure.step("api. Создать компанию {name} ({description})")
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company',
                             json=company, headers=my_headers)
        return resp.json()
    
    @allure.step("api. Получить компанию по {id}")
    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()
    
    @allure.step("api. Удалить компанию {id}")
    def get_delete(self, id):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.get(self.url + '/company/delete/' + str(id),headers=my_headers )
        return resp.json()