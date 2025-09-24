import mysql.connector as m

mydb=m.connect(
    host= "localhost",
    user="root",
    password="2007",
    database="hps"
)
mycursor= mydb.cursor()

def add_doctor():
    Emp_Id = int(input("Enter Doctor's ID:"))
    Emp_Name = input("Enter Doctor's Name:")
    Emp_Age = int(input("Enter Doctor's Age:"))
    Emp_Gender = input("Enter Doctor's Gender (M/F):")
    Emp_Address = input("Enter Doctor's Address (50ch):")
    Emp_Contact = input("Enter Doctor's Contact(+91):")
    Emp_Designation = "Doctor"
    Emp_Salary = int(input("Enter Doctor's Salary:"))
    opd = int(input("OPD STATUS Active(1)/Inactive(0)"))
    Specialists = input("Enter Doctor's Speciality:")
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
    print("New Doctor Added Successfully")
    print("-----------------------------------------------------------------")

def update_doctor_details():
    Emp_Id = int(input("Enter Doctor's ID:"))
    Emp_Name = input("Enter Doctor's Name:")
    Emp_Age = int(input("Enter Doctor's Age:"))
    Emp_Gender = input("Enter Doctor's Gender (M/F):")
    Emp_Address = input("Enter Doctor's Address (50ch):")
    Emp_Contact = input("Enter Doctor's Contact(+91):")
    Emp_Designation = "Doctor"
    Emp_Salary = int(input("Enter Doctor's Salary:"))
    opd = int(input("OPD STATUS Active(1)/Inactive(0)"))
    Specialists = input("Enter Doctor's Speicality:")
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
    print("Doctor's Details updated")
    print("-----------------------------------------------------------------")

def search_by_doc_id():
    Emp_Id = int(input("Enter Doctor's ID: "))
    query_doctor_fetch = '''SELECT Emp_Id, Emp_Name, Emp_Age, Emp_Gender, Emp_Contact, Emp_Designation, Specialists, Surgeon, Physician FROM Employee WHERE Emp_Id = %s AND Emp_Designation = 'Doctor' '''
    val_fetch = (Emp_Id,)
    mycursor.execute(query_doctor_fetch, val_fetch)
    record_fetchone = mycursor.fetchone()
    if record_fetchone:
        print("-----------------------------------------------------------------")
        print("Doctor's Record")
        print("Doctor's ID:", record_fetchone[0])
        print("Doctor's Name:", record_fetchone[1])
        print("Age:", record_fetchone[2])
        print("Gender:", record_fetchone[3])
        print("Contact:", record_fetchone[4])
        print("Designation:", record_fetchone[5])
        print("Specialists:", record_fetchone[6])
        print("Surgeon:", record_fetchone[7])
        print("Physician:", record_fetchone[8])
        print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No doctor found with that ID.")
        print("-----------------------------------------------------------------")

def search_by_name_doctor():
    Emp_Name = input("Enter Doctor's name: ")
    query_doctor_fetchname = '''SELECT Emp_Id, Emp_Name, Emp_Age, Emp_Gender, Emp_Contact, Emp_Designation, Specialists, Surgeon, Physician FROM Employee WHERE Emp_Name LIKE %s AND Emp_Designation = 'Doctor' '''
    val_fetch = (f'%{Emp_Name}%',)
    mycursor.execute(query_doctor_fetchname, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Doctor's Records found:")
        for row in record_fetchall:
            print("Doctor's ID:", row[0])
            print("Doctor's Name:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("Contact:", row[4])
            print("Designation:", row[5])
            print("Specialists:", row[6])
            print("Surgeon:", row[7])
            print("Physician:", row[8])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No doctor found with that name.")
        print("-----------------------------------------------------------------")

def all_doctor_records():
    query_doctor_fetch_all = '''SELECT Emp_Id, Emp_Name, Emp_Age, Emp_Gender, Emp_Contact, Emp_Designation, Specialists, Surgeon, Physician FROM Employee WHERE Emp_Designation = 'Doctor' '''
    mycursor.execute(query_doctor_fetch_all)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("All Doctors Records")
        for row in record_fetchall:
            print("Doctor's ID:", row[0])
            print("Doctor's Name:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("Contact:", row[4])
            print("Designation:", row[5])
            print("Specialists:", row[6])
            print("Surgeon:", row[7])
            print("Physician:", row[8])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No doctor records found.")
        print("-----------------------------------------------------------------")

def clear_doctor_record():
    Emp_Id = int(input("Enter Doctor's ID to delete: "))
    query_doctor_delete_one = '''DELETE FROM Employee WHERE Emp_Id = %s AND Emp_Designation = 'Doctor' '''
    val_doctor_deleteone = (Emp_Id,)
    mycursor.execute(query_doctor_delete_one, val_doctor_deleteone)
    mydb.commit()
    print("-----------------------------------------------------------------")
    if mycursor.rowcount > 0:
        print("Doctor record Deleted Successfully")
    else:
        print("No doctor found with that ID or record already deleted.")
    print("-----------------------------------------------------------------")
