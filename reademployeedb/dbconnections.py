from pathlib import Path
import sqlite3
from sqlite3 import Error

from reademployeedb.employee import Employee

PARENT_DIR = Path(__file__).resolve().parent
DATABASEFILE = PARENT_DIR / "db" / "employeedb.db"


def _create_connection(db_file):
    """create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database: {db_file}")
    except Error as e:
        print(e)
    return conn


def _execute_query(conn, query):
    """execute a query on the SQLite database"""
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        print("Query executed successfully")
    except Error as e:
        print(e)


def get_employees():
    conn = _create_connection(DATABASEFILE)
    query = "SELECT * FROM employees"
    c = conn.cursor()
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    return rows


def get_employees_by_department(department):
    conn = _create_connection(DATABASEFILE)
    query = f"SELECT * FROM employees WHERE department = '{department}'"
    c = conn.cursor()
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    return rows


def get_employees_by_id(id):
    conn = _create_connection(DATABASEFILE)
    query = f"SELECT * FROM employees WHERE id = {id}"
    c = conn.cursor()
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    return rows


def add_employee(employee: Employee):
    conn = _create_connection(DATABASEFILE)
    query = f"INSERT INTO employees (name, department, email, phone) VALUES ('{employee.name}', '{employee.department}', '{employee.email}', '{employee.phone}')"
    _execute_query(conn, query)
    conn.close()


def update_employee(employee: Employee):
    conn = _create_connection(DATABASEFILE)
    query = f"UPDATE employees SET name = '{employee.name}', department = '{employee.department}', email = '{employee.email}', phone = '{employee.phone}' WHERE id = {employee.id}"
    _execute_query(conn, query)
    conn.close()


def delete_employee(id):
    conn = _create_connection(DATABASEFILE)
    query = f"DELETE FROM employees WHERE id = {id}"
    _execute_query(conn, query)
    conn.close()
