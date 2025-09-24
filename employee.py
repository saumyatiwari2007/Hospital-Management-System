import mysql.connector as m

mydb=m.connect(
    host= "localhost",
    user="root",
    password="2007",
    database="hps"
)
mycursor= mydb.cursor()
def add_employee():
    Emp_Id = int(input("Enter Employee ID:"))
    Emp_Name = input("Enter Employee Name:")
    Emp_Age = int(input("Enter Employee Age:"))
    Emp_Gender = input("Enter Employee Gender (M/F):")
    Emp_Address = input("Enter Employee Address (50ch):")
    Emp_Contact = input("Enter Employee Contact(+91):")
    Emp_Designation = input("Enter Employee Designation:")
    Emp_Salary = int(input("Enter Employee Salary:"))
    opd = int(input("OPD STATUS Active(1)/Inactive(0)"))
    Specialists = input("Enter Doctor Speciality:")
    Surgeon = input("Enter Surgeon:")
    Physician = input("Enter Physician:")
    Active_Status = int(input("Enter Active Status Active(1)/Inactive(0)"))
    query_new_employee = '''INSERT INTO Employee(
    Emp_Id,
    Emp_Name,
    Emp_Age,
    Emp_Gender,
    Emp_Address,
    Emp_Contact,
    Emp_Designation,
    Emp_Salary,
    OPD,
    Specialists,
    Surgeon,
    Physician,
    Acitve_Status
    )
    VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    val_employee_insert = (Emp_Id, Emp_Name, Emp_Age, Emp_Gender, Emp_Address, Emp_Contact, Emp_Designation, Emp_Salary, opd, Specialists, Surgeon, Physician, Active_Status)
    mycursor.execute(query_new_employee, val_employee_insert)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("New Employee Added Successfully")
    print("-----------------------------------------------------------------")

def update_employee_details():
    Emp_Id = int(input("Enter Employee ID:"))
    Emp_Name = input("Enter Employee Name:")
    Emp_Age = int(input("Enter Employee Age:"))
    Emp_Gender = input("Enter Employee Gender (M/F):")
    Emp_Address = input("Enter Employee Address (50ch):")
    Emp_Contact = input("Enter Patient Contact(+91):")
    Emp_Designation = input("Enter Employee Designation:")
    Emp_Salary = int(input("Enter Employee Salary:"))
    opd = int(input("OPD STATUS Active(1)/Inactive(0)"))
    Specialists = input("Enter Doctor Speicality:")
    Surgeon = input("Enter Surgeon:")
    Physician = input("Enter Physician:")
    Active_Status = int(input("Enter Active Status Active(1)/Inactive(0)"))
    query_update_employee = '''Update Employee Set
    Emp_Name=%s,
    Emp_Age=%s,
    Emp_Gender=%s,
    Emp_Address=%s,
    Emp_Contact=%s,
    Emp_Designation=%s,
    Emp_Salary=%s,
    OPD=%s,
    Specialists=%s,
    Surgeon=%s,
    Physician=%s,
    Acitve_Status=%s
    where Emp_Id=%s'''
    val_employee_update = (Emp_Name, Emp_Age, Emp_Gender, Emp_Address, Emp_Contact, Emp_Designation, Emp_Salary, opd, Specialists, Surgeon, Physician, Active_Status, Emp_Id)
    mycursor.execute(query_update_employee, val_employee_update)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Employee Details updated")
    print("-----------------------------------------------------------------")

def search_by_e_id():
    Emp_Id = int(input("Enter Employee ID: "))
    query_employee_fetch = '''SELECT * FROM Employee WHERE Emp_Id = %s'''
    val_fetch = (Emp_Id,)
    mycursor.execute(query_employee_fetch, val_fetch)
    record_fetchone = mycursor.fetchone()
    if record_fetchone:
        print("-----------------------------------------------------------------")
        print("Employee Record")
        print("Employee ID:", record_fetchone[0])
        print("Employee Name:", record_fetchone[1])
        print("Age:", record_fetchone[2])
        print("Gender:", record_fetchone[3])
        print("Address:", record_fetchone[4])
        print("Contact:", record_fetchone[5])
        print("Designation:", record_fetchone[6])
        print("Salary:", record_fetchone[7])
        print("OPD Status:", "Active" if record_fetchone[8] == 1 else "Inactive")
        print("Specialists:", record_fetchone[9])
        print("Surgeon:", record_fetchone[10])
        print("Physician:", record_fetchone[11])
        print("Active Status:", "Active" if record_fetchone[12] == 1 else "Inactive")
        print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No employee found with that ID.")
        print("-----------------------------------------------------------------")

def search_by_name_employee():
    Emp_Name = input("Enter Employee Name: ")
    query_employee_fetchname = '''SELECT * FROM Employee WHERE Emp_Name LIKE %s'''
    val_fetch = (f'%{Emp_Name}%',)
    mycursor.execute(query_employee_fetchname, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Employee Records found:")
        for row in record_fetchall:
            print("Employee ID:", row[0])
            print("Employee Name:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("Address:", row[4])
            print("Contact:", row[5])
            print("Designation:", row[6])
            print("Salary:", row[7])
            print("OPD Status:", "Active" if row[8] == 1 else "Inactive")
            print("Specialists:", row[9])
            print("Surgeon:", row[10])
            print("Physician:", row[11])
            print("Active Status:", "Active" if row[12] == 1 else "Inactive")
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No employee found with that name.")
        print("-----------------------------------------------------------------")

def all_employee_records():
    query_employee_fetch_all = '''SELECT * FROM Employee'''
    mycursor.execute(query_employee_fetch_all)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("All Employee Records")
        for row in record_fetchall:
            print("Employee ID:", row[0])
            print("Employee Name:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("Address:", row[4])
            print("Contact:", row[5])
            print("Designation:", row[6])
            print("Salary:", row[7])
            print("OPD Status:", "Active" if row[8] == 1 else "Inactive")
            print("Specialists:", row[9])
            print("Surgeon:", row[10])
            print("Physician:", row[11])
            print("Active Status:", "Active" if row[12] == 1 else "Inactive")
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No employee records found.")
        print("-----------------------------------------------------------------")

def clear_employee_record():
    Emp_Id = int(input("Enter Employee ID to delete: "))
    query_employee_delete_one = '''DELETE FROM Employee WHERE Emp_Id = %s'''
    val_employee_deleteone = (Emp_Id,)
    mycursor.execute(query_employee_delete_one, val_employee_deleteone)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Employee record Deleted Successfully")
    print("-----------------------------------------------------------------")

def search_by_designation():
    Designation = input("Enter Employee Designation: ")
    query_employee_fetch = '''SELECT * FROM Employee WHERE Emp_Designation LIKE %s'''
    val_fetch = (f'%{Designation}%',)
    mycursor.execute(query_employee_fetch, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Employee Records for Designation:", Designation)
        for row in record_fetchall:
            print("Employee ID:", row[0])
            print("Employee Name:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("Address:", row[4])
            print("Contact:", row[5])
            print("Designation:", row[6])
            print("Salary:", row[7])
            print("OPD Status:", "Active" if row[8] == 1 else "Inactive")
            print("Specialists:", row[9])
            print("Surgeon:", row[10])
            print("Physician:", row[11])
            print("Active Status:", "Active" if row[12] == 1 else "Inactive")
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print(f"No employees found with the designation '{Designation}'.")
        print("-----------------------------------------------------------------")

def search_by_designation():
    Designation = input("Enter Employee Designation: ")
    query_employee_fetch = '''SELECT * FROM Employee WHERE Emp_Designation LIKE %s'''
    val_fetch = (f'%{Designation}%',)
    mycursor.execute(query_employee_fetch, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Employee Records for Designation:", Designation)
        for row in record_fetchall:
            print("Employee ID:", row[0])
            print("Employee Name:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("Address:", row[4])
            print("Contact:", row[5])
            print("Designation:", row[6])
            print("Salary:", row[7])
            print("OPD Status:", "Active" if row[8] == 1 else "Inactive")
            print("Specialists:", row[9])
            print("Surgeon:", row[10])
            print("Physician:", row[11])
            print("Active Status:", "Active" if row[12] == 1 else "Inactive")
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print(f"No employees found with the designation '{Designation}'.")
        print("-----------------------------------------------------------------")

def search_by_opd():
    opd_status = input("Enter OPD Status (Active/Inactive): ").lower()
    if opd_status == 'active':
        opd_val = 1
    elif opd_status == 'inactive':
        opd_val = 0
    else:
        print("Invalid input. Please enter 'Active' or 'Inactive'.")
        return

    query_employee_fetch = '''SELECT * FROM Employee WHERE OPD = %s'''
    val_fetch = (opd_val,)
    mycursor.execute(query_employee_fetch, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Employee Records with OPD Status:", opd_status.capitalize())
        for row in record_fetchall:
            print("Employee ID:", row[0])
            print("Employee Name:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("Address:", row[4])
            print("Contact:", row[5])
            print("Designation:", row[6])
            print("Salary:", row[7])
            print("OPD Status:", "Active" if row[8] == 1 else "Inactive")
            print("Specialists:", row[9])
            print("Surgeon:", row[10])
            print("Physician:", row[11])
            print("Active Status:", "Active" if row[12] == 1 else "Inactive")
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print(f"No employees found with '{opd_status}' OPD status.")
        print("-----------------------------------------------------------------")

def search_specialists():
    speciality = input("Enter Doctor's Speciality: ")
    query_employee_fetch = '''SELECT * FROM Employee WHERE Specialists LIKE %s'''
    val_fetch = (f'%{speciality}%',)
    mycursor.execute(query_employee_fetch, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Specialists found:")
        for row in record_fetchall:
            print("Employee ID:", row[0])
            print("Employee Name:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("Address:", row[4])
            print("Contact:", row[5])
            print("Designation:", row[6])
            print("Salary:", row[7])
            print("OPD Status:", "Active" if row[8] == 1 else "Inactive")
            print("Specialists:", row[9])
            print("Surgeon:", row[10])
            print("Physician:", row[11])
            print("Active Status:", "Active" if row[12] == 1 else "Inactive")
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No specialists found.")
        print("-----------------------------------------------------------------")

def search_surgeons():
    surgeon_name = input("Enter Surgeon's Name: ")
    query_employee_fetch = '''SELECT * FROM Employee WHERE Surgeon LIKE %s'''
    val_fetch = (f'%{surgeon_name}%',)
    mycursor.execute(query_employee_fetch, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Surgeons found:")
        for row in record_fetchall:
            print("Employee ID:", row[0])
            print("Employee Name:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("Address:", row[4])
            print("Contact:", row[5])
            print("Designation:", row[6])
            print("Salary:", row[7])
            print("OPD Status:", "Active" if row[8] == 1 else "Inactive")
            print("Specialists:", row[9])
            print("Surgeon:", row[10])
            print("Physician:", row[11])
            print("Active Status:", "Active" if row[12] == 1 else "Inactive")
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No surgeons found.")
        print("-----------------------------------------------------------------")

def search_physicians():
    physician_name = input("Enter Physician's Name: ")
    query_employee_fetch = '''SELECT * FROM Employee WHERE Physician LIKE %s'''
    val_fetch = (f'%{physician_name}%',)
    mycursor.execute(query_employee_fetch, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Physicians found:")
        for row in record_fetchall:
            print("Employee ID:", row[0])
            print("Employee Name:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("Address:", row[4])
            print("Contact:", row[5])
            print("Designation:", row[6])
            print("Salary:", row[7])
            print("OPD Status:", "Active" if row[8] == 1 else "Inactive")
            print("Specialists:", row[9])
            print("Surgeon:", row[10])
            print("Physician:", row[11])
            print("Active Status:", "Active" if row[12] == 1 else "Inactive")
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No physicians found.")
        print("-----------------------------------------------------------------")
