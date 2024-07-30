import requests
from CompanyApi import CompanyApi
from EmployeeTable import EmployeeTable
from EmployeeApi import EmployeeApi

api1 = CompanyApi("https://x-clients-be.onrender.com")
api2 = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

# Проверка получения списка сотрудников
def test_get_employee():
    #Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api1.create_company(name, descr)
    new_id = result["id"]
    #список сотрудников в компании 
    api_result= api2.get_staff_list(new_id)
    db_result = db.get_employees(new_id)
    db.delete(new_id)
    assert len(db_result) >= 0
    assert len(api_result) == len(db_result)

#добавить нового сотрудника
def test_get_staff():
    #Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api1.create_company(name, descr)
    new_id = result["id"]
    #список сотрудников в компании 
    body1 = db.get_employees(new_id) #x = 0
    #создание сотрудника 
    employee = db.create_employee(new_id)
    employee_id = employee['id']
    #проверка после создания 
    body2 = db.get_employees(new_id)
    db.delete_emp(employee_id)
    db.delete(new_id)
    
    assert len(body1) + 1 == len(body2)
    assert employee_id > 0


#получить сотрудника по ID 
def test_get_one_emploee():
    #Создаем компанию
    name = "VS Code"
    descr = "IDE"
    result = api1.create_company(name, descr)
    new_id = result["id"]
    #создание сотрудника 
    new_employee = db.create_employee(new_id)
    #Обращаемся к сотруднику
    id_employee= new_employee['id']
    employee= db.get_employee_id(id_employee)
    db.delete_emp(id_employee)
    db.delete(new_id)
    #Проверим id нового сотрудника:
    assert employee['id'] == id_employee
    assert employee["first_name"] =="Anna"
    assert employee["last_name"] == "Generozova"

def test_edit_employee():
    
    name = "VS Code"
    descr = "IDE"
    result = api1.create_company(name, descr)
    new_id = result["id"]
    
    new_employee = db.create_employee(new_id)
   
    id_employee = new_employee['id']

    update = db.edit_employee(id_employee)
    
    db.delete_emp(id_employee)
    db.delete(new_id)
    assert update["id"] == id_employee
    assert update["email"] == "test123@mail.ru"
    assert update["last_name"] == "Sokolova"
