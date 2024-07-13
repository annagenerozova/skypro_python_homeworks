import requests

class EmployeeApi: 
    # Инициализация 
    def __init__(self, url) -> None:
        self.url = url
    
    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    # список сотрудников компании 
    def get_staff_list(self, id):
        company = {
            'company': str(id)
        }
        resp = requests.get(self.url + '/employee' ,params=company )
        return resp.json()
    
    #добавление сотрудника 
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
    
    def get_employee(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()
    
    def edit(self, new_id, new_lname ="Sokolova", email = "test123@mail.ru", 
             url ="https://instagram.com/_anna.roze", phone ="89218308966", isActive = True):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        employee = {
            "lastName": new_lname,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": isActive
        }
        resp = requests.patch(self.url + '/employee/' + str(new_id) ,json=employee, headers=my_headers)
        return resp
    
    