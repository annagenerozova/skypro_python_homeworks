import requests
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeeTable: 
    __scripts = {
        "select": text("select * from employee where company_id = :id_company")
    }
    # Инициализация 
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
        
    
    #список сотрудников компании
    def get_employees(self):
        return self.db.execute(self.__scripts["select"]).fetchall()
          
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