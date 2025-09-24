import mysql.connector as m

mydb=m.connect(
    host= "localhost",
    user="root",
    password="2007",
    database="hps"
)
mycursor= mydb.cursor()
def add_patient():
    Patient_Name = input("Enter Patient Name:")
    Age = int(input("Enter Patient Age:"))
    Gender = input("Enter Patient Gender (M/F):")
    Adress = input("Enter Patient Address (50ch):")
    Contact = input("Enter Patient Contact(+91):")
    query_new_patient = '''INSERT INTO patient(
    Patient_Name,
    Age,
    Gender,
    Adress,
    Contact
    )
    VALUE(%s,%s,%s,%s,%s)
    '''
    val_patient_insert = (Patient_Name, Age, Gender, Adress, Contact)
    mycursor.execute(query_new_patient, val_patient_insert)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("New Patient Record Added Successfully"," Patient ID:",mycursor.lastrowid)
    print("-----------------------------------------------------------------")

def update_patient_details():
    P_Id = int(input("Enter Patient ID to update:"))
    Patient_Name = input("Enter New Patient Name:")
    Age = int(input("Enter New Patient Age:"))
    Gender = input("Enter New Patient Gender (M/F):")
    Adress = input("Enter New Patient Address (50ch):")
    Contact = input("Enter New Patient Contact(+91):")
    query_update_patient = '''UPDATE patient SET
    Patient_Name=%s,
    Age=%s,
    Gender=%s,
    Adress=%s,
    Contact=%s
    where P_Id=%s'''
    val_patient_update = (Patient_Name, Age, Gender, Adress, Contact, P_Id)
    mycursor.execute(query_update_patient, val_patient_update)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Patient details updated")
    print("-----------------------------------------------------------------")

def search_by_p_id():
    P_Id = int(input("Enter Patient ID:"))
    query_patient_fetch = '''SELECT * FROM patient WHERE P_Id = %s'''
    val_fetch = (P_Id,)
    mycursor.execute(query_patient_fetch, val_fetch)
    record_fetchone = mycursor.fetchone()
    if record_fetchone:
        print("-----------------------------------------------------------------")
        print("Patient Record")
        print("Patient ID:", record_fetchone[0])
        print("Patient Name:", record_fetchone[1])
        print("Age:", record_fetchone[2])
        print("Gender:", record_fetchone[3])
        print("Address:", record_fetchone[4])
        print("Contact:", record_fetchone[5])
        print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No patient record found with that Patient ID.")
        print("-----------------------------------------------------------------")

def search_by_name_patient():
    Patient_Name = input("Enter Patient name:")
    query_patient_fetchname = '''SELECT * FROM patient WHERE Patient_Name LIKE %s'''
    val_fetch = (f'%{Patient_Name}%',)
    mycursor.execute(query_patient_fetchname, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Patient Records for:", Patient_Name)
        for row in record_fetchall:
            print("Patient ID:", row[0])
            print("Patient Name:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("Address:", row[4])
            print("Contact:", row[5])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No patient records found with that name.")
        print("-----------------------------------------------------------------")

def all_patient_records():
    query_patient_fetch_all = '''SELECT * FROM patient'''
    mycursor.execute(query_patient_fetch_all)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("All Patient Records")
        for row in record_fetchall:
            print("Patient ID:", row[0])
            print("Patient Name:", row[1])
            print("Age:", row[2])
            print("Gender:", row[3])
            print("Address:", row[4])
            print("Contact:", row[5])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No patient records found.")
        print("-----------------------------------------------------------------")

def clear_patient_record():
    P_Id = int(input("Enter Patient ID to delete:"))
    query_patient_delete_one = '''DELETE FROM patient WHERE P_Id = %s'''
    val_patient_deleteone = (P_Id,)
    mycursor.execute(query_patient_delete_one, val_patient_deleteone)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Patient record Deleted Successfully")
    print("-----------------------------------------------------------------")


def clear_all_patient_records():
    query_patient_deleteall = '''DELETE FROM patient'''
    mycursor.execute(query_patient_deleteall)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("All patient data cleared")
    print("-----------------------------------------------------------------")