from fastapi import FastAPI

from reademployeedb.dbconnections import (
    get_employees_by_id,
    get_employees,
    add_employee,
    update_employee,
    delete_employee,
)
from reademployeedb.employee import Employee

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee API!"}


@app.get("/employees")
def get_all_employees():
    employees = get_employees()
    return employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    employee = get_employees_by_id(employee_id)
    if not employee:
        return {"error": "Employee not found"}
    return employee


@app.post("/employees/new")
def create_employee(employee: dict):
    created_employee = Employee(**employee)
    add_employee(created_employee)
    return {"message": "Employee added successfully"}


@app.put("/employees/update")
def update_employee_details(employee: dict):
    updated_employee = Employee(**employee)
    update_employee(updated_employee)
    return {"message": "Employee details updated successfully"}


@app.delete("/employees/delete/{employee_id}")
def delete_employee_record(employee_id: int):
    delete_employee(employee_id)
    return {"message": "Employee record deleted successfully"}
