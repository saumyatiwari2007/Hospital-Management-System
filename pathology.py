import mysql.connector as m

mydb=m.connect(
    host= "localhost",
    user="root",
    password="2007",
    database="hps"
)
mycursor= mydb.cursor()
def add_pathology_record():
    P_Id = int(input("Enter Patient ID:"))
    Receipt_Number = int(input("Enter Receipt Number:"))
    Test_name = input("Enter Test Name:")
    Test_charges = float(input("Enter Test Charges:"))
    Report_Status = input("Enter Report Status (e.g., Pending, Completed):")
    Equiments = input("Enter Equipment Used:")
    Units = int(input("Enter Units:"))
    Price = int(input("Enter Price:"))
    query_new_pathology = '''INSERT INTO pathology(
    P_Id,
    Receipt_Number,
    Test_name,
    Test_charges,
    Report_Status,
    Equiments,
    Units,
    Price
    )
    VALUE%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    val_pathology_insert = (P_Id, Receipt_Number, Test_name, Test_charges, Report_Status, Equiments, Units, Price)
    mycursor.execute(query_new_pathology, val_pathology_insert)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("New Pathology Record Added Successfully")
    print("Lab ID:",mycursor.lastrowid)
    print("-----------------------------------------------------------------")

def update_pathology_record():
    Lb_Id = int(input("Enter Lab ID to update:"))
    P_Id = int(input("Enter Patient ID:"))
    Receipt_Number = int(input("Enter Receipt Number:"))
    Test_name = input("Enter Test Name:")
    Test_charges = float(input("Enter Test Charges:"))
    Report_Status = input("Enter Report Status (e.g., Pending, Completed):")
    Equiments = input("Enter Equipment Used:")
    Units = int(input("Enter Units:"))
    Price = int(input("Enter Price:"))
    query_update_pathology = '''Update pathology SET
    P_Id=%s,
    Receipt_Number=%s,
    Test_name=%s,
    Test_charges=%s,
    Report_Status=%s,
    Equiments=%s,
    Units=%s,
    Price=%s
    where Lb_Id=%s'''
    val_pathology_update = (P_Id, Receipt_Number, Test_name, Test_charges, Report_Status, Equiments, Units, Price, Lb_Id)
    mycursor.execute(query_update_pathology, val_pathology_update)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Pathology Record details updated")
    print("-----------------------------------------------------------------")

def search_by_lab_id():
    Lb_Id = int(input("Enter Lab ID:"))
    query_pathology_fetch = '''SELECT * FROM pathology WHERE Lb_Id = %s'''
    val_fetch = (Lb_Id,)
    mycursor.execute(query_pathology_fetch, val_fetch)
    record_fetchone = mycursor.fetchone()
    if record_fetchone:
        print("-----------------------------------------------------------------")
        print("Pathology Record")
        print("Lab ID:", record_fetchone[0])
        print("Patient ID:", record_fetchone[1])
        print("Receipt Number:", record_fetchone[2])
        print("Test Name:", record_fetchone[3])
        print("Test Charges:", record_fetchone[4])
        print("Report Status:", record_fetchone[5])
        print("Equipment Used:", record_fetchone[6])
        print("Units:", record_fetchone[7])
        print("Price:", record_fetchone[8])
        print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No pathology record found with that Lab ID.")
        print("-----------------------------------------------------------------")

def search_pathology_by_pid():
    P_Id = int(input("Enter Patient ID:"))
    query_pathology_fetch_pid = '''SELECT * FROM pathology WHERE P_Id = %s'''
    val_fetch = (P_Id,)
    mycursor.execute(query_pathology_fetch_pid, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Pathology Records for Patient ID:", P_Id)
        for row in record_fetchall:
            print("Lab ID:", row[0])
            print("Patient ID:", row[1])
            print("Receipt Number:", row[2])
            print("Test Name:", row[3])
            print("Test Charges:", row[4])
            print("Report Status:", row[5])
            print("Equipment Used:", row[6])
            print("Units:", row[7])
            print("Price:", row[8])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No pathology records found for that Patient ID.")
        print("-----------------------------------------------------------------")

def search_pathology_by_receipt():
    Receipt_Number = int(input("Enter Receipt Number:"))
    query_pathology_fetch = '''SELECT * FROM pathology WHERE Receipt_Number = %s'''
    val_fetch = (Receipt_Number,)
    mycursor.execute(query_pathology_fetch, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Pathology Records found for Receipt Number:", Receipt_Number)
        for row in record_fetchall:
            print("Lab ID:", row[0])
            print("Patient ID:", row[1])
            print("Receipt Number:", row[2])
            print("Test Name:", row[3])
            print("Test Charges:", row[4])
            print("Report Status:", row[5])
            print("Equipment Used:", row[6])
            print("Units:", row[7])
            print("Price:", row[8])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No pathology records found for that Receipt Number.")
        print("-----------------------------------------------------------------")

def search_by_test_name():
    Test_name = input("Enter Test Name:")
    query_pathology_fetch_test = '''SELECT * FROM pathology WHERE Test_name LIKE %s'''
    val_fetch = (f'%{Test_name}%',)
    mycursor.execute(query_pathology_fetch_test, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Pathology Records for Test Name:", Test_name)
        for row in record_fetchall:
            print("Lab ID:", row[0])
            print("Patient ID:", row[1])
            print("Receipt Number:", row[2])
            print("Test Name:", row[3])
            print("Test Charges:", row[4])
            print("Report Status:", row[5])
            print("Equipment Used:", row[6])
            print("Units:", row[7])
            print("Price:", row[8])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No pathology records found for that test name.")
        print("-----------------------------------------------------------------")

def all_pathology_records():
    query_pathology_fetch_all = '''SELECT * FROM pathology'''
    mycursor.execute(query_pathology_fetch_all)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("All Pathology Records")
        for row in record_fetchall:
            print("Lab ID:", row[0])
            print("Patient ID:", row[1])
            print("Receipt Number:", row[2])
            print("Test Name:", row[3])
            print("Test Charges:", row[4])
            print("Report Status:", row[5])
            print("Equipment Used:", row[6])
            print("Units:", row[7])
            print("Price:", row[8])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No pathology records found.")
        print("-----------------------------------------------------------------")

def clear_pathology_record():
    Lb_Id = int(input("Enter Lab ID to delete:"))
    query_pathology_delete_one = '''DELETE FROM pathology WHERE Lb_Id = %s'''
    val_pathology_deleteone = (Lb_Id,)
    mycursor.execute(query_pathology_delete_one, val_pathology_deleteone)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Pathology Record Deleted Successfully")
    print("-----------------------------------------------------------------")

def clear_all_pathology_records():
    query_pathology_deleteall = '''DELETE FROM pathology'''
    mycursor.execute(query_pathology_deleteall)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("All pathology data cleared")
    print("-----------------------------------------------------------------")