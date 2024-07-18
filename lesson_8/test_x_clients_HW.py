import requests
from CompanyApi import CompanyApi
from EmployeeApi import EmployeeApi

api1 = CompanyApi("https://x-clients-be.onrender.com")
api2 = EmployeeApi("https://x-clients-be.onrender.com")
 # Проверка получения списка компаний
def test_get_companies():
    body = api1.get_company_list()
    assert len(body) > 0


def test_get_staff():
    #Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api1.create_company(name, descr)
    new_id = result["id"]
    #список сотрудников в компании 
    body1 = api2.get_staff_list(new_id) #x = 0
    #создание сотрудника 
    employee = api2.create_employee(new_id)
    employee_id = employee.json()['id']
    #проверка после создания 
    body2 = api2.get_staff_list(new_id)
    assert len(body1) + 1 == len(body2)
    assert employee_id > 0
    assert employee.status_code == 201

def test_get_one_emploee():
    #Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api1.create_company(name, descr)
    new_id = result["id"]
    #создание сотрудника 
    new_emploee = api2.create_employee(new_id)
    #Обращаемся к сотруднику
    id_emploee= new_emploee["id"]
    emploee = api2.get_employee(id_emploee)
    
    #Проверим id нового сотрудника:
    assert emploee["firstName"] =="Anna"
    assert emploee["lastName"] == "Generozova"

def test_edit_employee():
    #Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api1.create_company(name, descr)
    new_id = result["id"]
    #создание сотрудника 
    new_employee = api2.create_employee(new_id)

    id_employee = new_employee["id"]

    update = api2.edit(id_employee)
    assert update["id"] == id_employee
    assert update["lastName"] == "Sokolova"
    assert update["email"] == "test123@mail.ru"
    assert update["isActive"] == True






