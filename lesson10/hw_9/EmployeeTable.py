import allure
import requests
from sqlalchemy import create_engine
from sqlalchemy.sql import text
 
class EmployeeTable: 
    __scripts = {
        "select": text("select * from employee where company_id = :id_company"),
        "insert": text("""
        INSERT INTO employee (company_id, first_name,last_name,middle_name, email,avatar_url , phone, birthdate, is_active)
        VALUES (:id_company, 'Anna', 'Generozova', 'Dmitrievna', '"test@mail.ru"', 'https://t.me/gener_anna','89218963258','1999-04-11', True)
        RETURNING id
                       """),
        "select by id": text("select * from employee where id =:select_id "),
        "delete company": text("delete from company where id =:id_to_delete"),
        "delete employee": text("delete from employee where id =:id_employee"),
        "edit":text ("""
        UPDATE employee SET last_name = 'Sokolova',
        phone = '89218308966', email = 'test123@mail.ru', avatar_url = 'https://instagram.com/_anna.roze'
        WHERE id = :employee_id
        RETURNING id, first_name, last_name, middle_name, email, avatar_url, phone, birthdate, is_active
        """)
    }
    
    # Инициализация 
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
    
    @allure.step("БД. Запросить список сотрудников компании")
    def get_employees(self,id):
        return self.db.execute(self.__scripts["select"],id_company=id).fetchall()    
    
    @allure.step("БД. Создать сотрудника с уникальным {id}")
    def create_employee(self,id):
        return self.db.execute(self.__scripts["insert"],id_company=id).fetchone()
    
    @allure.step("БД.Получение сотрудника по {id}")
    #получение сотрудника по id
    def get_employee_id(self, id):
        return self.db.execute(self.__scripts["select by id"], select_id = id).fetchone()
    
    @allure.step("БД. Удалить организацию по {id}")
    def delete(self, id):
        self.db.execute(self.__scripts["delete company"], id_to_delete = id)
    
    @allure.step("БД. Удалить сотрудника по {id}")
    def delete_emp(self, id):
        self.db.execute(self.__scripts["delete employee"], id_employee = id)
    
    @allure.step("БД. Редактирование сотрудника по {id}")
    def edit_employee(self, id):
        return self.db.execute(self.__scripts["edit"], employee_id = id).fetchone()

