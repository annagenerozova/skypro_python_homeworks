import requests
from CompanyApi import CompanyApi
from EmployeeTable import EmployeeTable
from EmployeeApi import EmployeeApi

api1 = CompanyApi("https://x-clients-be.onrender.com")
api2 = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

# Проверка получения списка компаний
def test_get_employee():
    #Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api1.create_company(name, descr)
    new_id = result["id"]
    #список сотрудников в компании 
    api_result= api2.get_staff_list(new_id)
    db_result = db.get_employees(new_id)
    assert len(db_result) >= 0
    assert len(api_result) == len(db_result)


def test_get_staff():
    #Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api1.create_company(name, descr)
    new_id = result["id"]
    #список сотрудников в компании 
    body1 = db.get_employee(new_id) #x = 0
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
    id_emploee= new_emploee.json()['id']
    emploee = api2.get_employee(id_emploee)
    
    #Проверим id нового сотрудника:
    assert emploee['id'] == id_emploee
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

    id_employee = new_employee.json()["id"]
    #изменение сотрудника 
    update = api2.edit(id_employee)
    assert update["id"] == id_employee
    assert update["lastName"] == "Sokolova"
    assert update["email"] == "test123@mail.ru"
    assert update["isActive"] == True






