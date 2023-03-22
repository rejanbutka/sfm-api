from typing import List
from fastapi import APIRouter

from app.models.Employee import Employee, EmployeeInUpdate

router = APIRouter()

employees_db = [
    Employee(id='1', first_name='John', last_name='Doe', roles='Administrator'),
    Employee(id='2', first_name='Sarah', last_name='Palmer', roles='Technician'),
    Employee(id='3', first_name='Dale', last_name='Cooper', roles='Finance'),
    Employee(id='4', first_name='David', last_name='Lynch', roles='Scientist')
]

@router.get('/employees/')
def read_employees():
    return employees_db

@router.get('/employees/{id}')
def read_employee_by_id(id: int):
    return list(filter(lambda employee: employee.id == id, employees_db))

@router.post('/employees/create')
def create_employee(employee: Employee):
    employees_db.append(employee)
    return employee

@router.put('/employees/update/{id}')
def update_employee_by_id(updated: EmployeeInUpdate, id: int):
    # get the existing employee
    employee = read_employee_by_id(id)

    # handle non-existing employee on update
    if employee == None:
        return "Employee not found!"

    # get the existing employee's index
    index = employees_db.index(employee)
    
    # update existing employee fields
    if updated.first_name != None:
        employee.first_name = updated.first_name
    if updated.last_name != None:
        employee.last_name = updated.last_name
    if updated.roles != None and updated.roles:
        employee.roles = updated.roles

    # store the updated employee
    employees_db[index] = employee

    # return the updated employee
    return employee

@router.delete('/employees/delete/{id}')
def delete_employee_by_id(id: int):
    # get the existing employee
    employee = read_employee_by_id(id)

     # handle non-existing employee on delete
    if employee == None:
        return "Employee not found!"
    
    # delete employee from db
    employees_db.remove(employee)

    # return the deleted employee
    return employee