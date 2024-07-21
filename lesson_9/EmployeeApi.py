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
    def create_employee(self, companyId, firstName, lastName , middleName,
                        email , url, phone, 
                        birthdate, isActive ):
        employee = {
                "id": 0,
                firstName: "Anna",
                lastName: "Generozova",
                middleName: "Dmitrievna",
                companyId:"",
                email: "test@mail.ru",
                url: 'https://t.me/gener_anna',
                phone: "89218305722",
                birthdate: '1999-04-11',
                isActive: True
            }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee',json=employee, headers=my_headers)
        return resp
    
    def get_employee(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()
    
    def edit(self, id, new_lname, email, 
             url, phone , isActive ):
        employee = {
            new_lname: "Sokolova",
            email: "test123@mail.ru",
            url: "https://instagram.com/_anna.roze",
            phone: "89218308966",
            isActive: True
            }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/employee/' + str(id) ,json=employee, headers=my_headers)
        return resp()