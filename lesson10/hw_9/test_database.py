import allure
import requests
from CompanyApi import CompanyApi
from EmployeeTable import EmployeeTable
from EmployeeApi import EmployeeApi

@allure.epic("Сотрудники") 
@allure.severity("blocker")
class TestEmployee:

    api1 = CompanyApi("https://x-clients-be.onrender.com")
    api2 = EmployeeApi("https://x-clients-be.onrender.com")
    db = EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

    @allure.title("Получение полного списка сотрудников ")
    @allure.feature("READ")
    # Проверка получения списка сотрудников
    def test_get_employee(self):
        with allure.step("Создание компании"):
            name = "VS Code"
            descr = "IDE"
            result = self.api1.create_company(name, descr)
            new_id = result["id"]
        with allure.step("Получить список компаний из Api"):
            api_result= self.api2.get_staff_list(new_id)
        with allure.step("Получить список компаний из БД"):
            db_result = self.db.get_employees(new_id)
            self.db.delete(new_id)
        with allure.step("Сравнить размеры 2х списков"):    
            assert len(db_result) >= 0
            assert len(api_result) == len(db_result)

    @allure.title("Создание нового сотрудника ")
    @allure.feature("CREATE")
    @allure.description("Запрос новой созданной огранизации и сотрудника в ней")
    def test_get_staff(self):
        with allure.step("Создание компании"):
            name = "VS Code"
            descr = "IDE"
            result = self.api1.create_company(name, descr)
            new_id = result["id"]
        with allure.step("запрос списка сотрудникоа компании"):
            body1 = self.db.get_employees(new_id) #x = 0
        with allure.step("Создание сотрудника"):
            employee = self.db.create_employee(new_id)
            employee_id = employee['id']
        #проверка после создания 
        body2 = self.db.get_employees(new_id)
        with allure.step("Удаление сотрудника и компании"):
            self.db.delete_emp(employee_id)
            self.db.delete(new_id)
        
        with allure.step("Проверить, что список ДО меньше списка ПОСЛЕ на 1"):
            assert len(body1) + 1 == len(body2)
            assert employee_id > 0

    @allure.title("Запрос сотрудника по его id ")
    @allure.feature("CREATE") 
    def test_get_one_emploee(self):
        with allure.step("Создание компании"):
            name = "VS Code"
            descr = "IDE"
            result = self.api1.create_company(name, descr)
            new_id = result["id"]
        with allure.step("Создание сотрудника"):
            new_employee = self.db.create_employee(new_id)
        with allure.step("Получение id сотрудника"):
            id_employee= new_employee['id']
            employee= self.db.get_employee_id(id_employee)
        with allure.step("Удаление сотрудника и компании"): 
            self.db.delete_emp(id_employee)
            self.db.delete(new_id)
        with allure.step("Проверить поля нового сотрудника. Корректно заполнены"):
            assert employee['id'] == id_employee
            assert employee["first_name"] =="Anna"
            assert employee["last_name"] == "Generozova"
    
    @allure.title("Редактирование сотрудника ")
    @allure.feature("UPDATE") 
    def test_edit_employee(self):
        with allure.step("Создание компании"):
            name = "VS Code"
            descr = "IDE"
            result = self.api1.create_company(name, descr)
            new_id = result["id"]
        with allure.step("Создание сотрудника"):    
            new_employee = self.db.create_employee(new_id)
            id_employee = new_employee['id']
        with allure.step("Изменение сотрудника"):
            update = self.db.edit_employee(id_employee)
        with allure.step("Удаление сотрудника и компании"):
            self.db.delete_emp(id_employee)
            self.db.delete(new_id)
        with allure.step("Проверить поля сотрудника изменились и зполнились коректно"):
            assert update["id"] == id_employee
            assert update["email"] == "test123@mail.ru"
            assert update["last_name"] == "Sokolova"
