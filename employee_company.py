import psycopg2
connection = psycopg2.connect(database="test_db")

cursor = connection.cursor()
# cursor.execute("SELECT * FROM companies")
# print (cursor.fetchall())

cursor.execute("SELECT * FROM employees")
print (cursor.fetchall())

# Inserting data into companies table
id_input = input("Enter company id: ") #user inputs id
name_input = input("Enter company name: ")

cursor.execute("INSERT INTO companies (id, name) VALUES (%s, %s)", [id_input, name_input])
print("Company id is: " + id_input)
print("Company name is: " + name_input)
connection.commit()

# Reading data from employees table
which_id = input("Enter company id to see company: ")

cursor.execute("SELECT * FROM companies WHERE id = %s", [which_id])
print(cursor.fetchall())
connection.commit()

# Deleting data from companies table
# delete_id = input("Enter company id to delete company: ")
# cursor.execute("DELETE FROM companies WHERE id = %s", [delete_id])
# print(cursor.fetchall())
# connection.commit()


# Updating data in companies table
# which_company_id = input("Enter company id to update company: ")
# update_id = input("Enter new company id: ")
# update_name = input("Enter new company name: ")
# cursor.execute("UPDATE companies SET id = %s, name = %s WHERE id = %s", [update_id, update_name, which_company_id])
# connection.commit()


# Creating employees in table
emp_id = input("Enter employee id: ")
employee_name = input("Enter employee name: ")
employee_company_id = input("Enter company id: ")
employee_email = input("Enter employee email: ")

cursor.execute("INSERT INTO employees (employee_id, name, comp_id, email) VALUES (%s, %s, %s, %s)", [emp_id, employee_name, employee_company_id, employee_email])
connection.commit()

# Reading data from employees table
# which_emp_id = input("Enter employee id to see employee: ")
# cursor.execute("SELECT * FROM employees WHERE employee_id = %s", [which_emp_id])
# print(cursor.fetchall())
# connection.commit()

# Deleting data from employees table
# delete_emp_id = input("Enter employee id to delete employee: ")
# cursor.execute("DELETE FROM employees WHERE employee_id = %s", [delete_emp_id])
# connection.commit()

# Updating data in employees table
which_emp_id = input("Enter employee id to update employee: ")
update_emp_name = input("Enter new employee name: ")
update_emp_comp_id = input("Enter new company id: ")
update_emp_id = input("Enter new employee id: ")
update_emp_email = input("Enter new employee email: ")

cursor.execute("UPDATE employees SET name = %s, comp_id = %s, employee_id = %s, email = %s WHERE employee_id = %s", [update_emp_name, update_emp_comp_id, update_emp_id, update_emp_email, which_emp_id])
connection.commit()


cursor.close()
connection.close()