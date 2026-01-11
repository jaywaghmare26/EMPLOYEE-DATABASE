import sqlite3


conn = sqlite3.connect('employee.db')
c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            dept TEXT,
            position TEXT,
            salary REAL,
            email TEXT
            )""")
conn.commit()

def add_emp():
    name = input("Name: ")
    dept = input("Department: ")
    pos = input("Position: ")
    sal = input("Salary: ")
    email = input("Email: ")
    
    c.execute("INSERT INTO employee (name, dept, position, salary, email) VALUES (?, ?, ?, ?, ?)",
              (name, dept, pos, sal, email))
    conn.commit()
    print("Employee added!")

def view_emp():
    c.execute("SELECT * FROM employee")
    data = c.fetchall()
    
    if len(data) == 0:
        print("No records found")
    else:
        for row in data:
            print(row)

def search_emp():
    id = input("Enter ID: ")
    c.execute("SELECT * FROM employee WHERE id=?", (id,))
    data = c.fetchone()
    
    if data:
        print(data)
    else:
        print("Not found")

def update_emp():
    id = input("Enter ID to update: ")
    print("1. Update Name")
    print("2. Update Department")
    print("3. Update Salary")
    ch = input("Choice: ")
    
    if ch == '1':
        new_name = input("New Name: ")
        c.execute("UPDATE employee SET name=? WHERE id=?", (new_name, id))
    elif ch == '2':
        new_dept = input("New Department: ")
        c.execute("UPDATE employee SET dept=? WHERE id=?", (new_dept, id))
    elif ch == '3':
        new_sal = input("New Salary: ")
        c.execute("UPDATE employee SET salary=? WHERE id=?", (new_sal, id))
    
    conn.commit()
    print("Updated!")

def delete_emp():
    id = input("Enter ID to delete: ")
    c.execute("DELETE FROM employee WHERE id=?", (id,))
    conn.commit()
    print("Deleted!")


while True:
    print("\n--- Employee Database ---")
    print("1. Add Employee")
    print("2. View All")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_emp()
    elif choice == '2':
        view_emp()
    elif choice == '3':
        search_emp()
    elif choice == '4':
        update_emp()
    elif choice == '5':
        delete_emp()
    elif choice == '6':
        break
    else:
        print("Invalid choice")

conn.close()
print("Database closed")

