import allure
import requests


class EmployeeApi: 
    # Инициализация 
    def __init__(self, url) -> None:
        self.url = url
    
    @allure.step("api. Получить токен авторизации для пользователя {user}:{password}")
    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    @allure.step("api.получаем список сотрудников компании по {id}")
    def get_staff_list(self, id):
        company = {
            'company': str(id)
        }
        resp = requests.get(self.url + '/employee' ,params=company )
        return resp.json()
    
    @allure.step("api. добавляем сотрудника в компанию {companyId} {firstName} {lastName} {middleName} {email} {url}{phone}{birthdate}{isActive}") 
    def create_employee(self, companyId, firstName ="Anna", lastName ="Generozova" , middleName= "Dmitrievna", 
                        email = "test@mail.ru", url ='https://t.me/gener_anna', phone ="89218305722", 
                        birthdate ='1999-04-11', isActive = True):
        employee = {
                "id": 0,
                "firstName": firstName,
                "lastName": lastName,
                "middleName": middleName,
                "companyId": companyId,
                "email": email,
                "url": url,
                "phone": phone,
                "birthdate": birthdate,
                "isActive": isActive
            }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee',json=employee, headers=my_headers)
        return resp
    
    @allure.step("api. Получить сотрудника по {id}")
    def get_employee(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()
    
    @allure.step("api. Редактировать сотрудника {id} {new_lname}{email}{url}{phone}{phone}{isActive}")
    def edit(self, id, new_lname ="Sokolova", email = "test123@mail.ru", 
             url ="https://instagram.com/_anna.roze", phone ="89218308966", isActive = True):
        employee = {
            "lastName": new_lname,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": isActive
            }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/employee/' + str(id) ,json=employee, headers=my_headers)
        return resp()