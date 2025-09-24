import mysql.connector as m

mydb=m.connect(
    host= "localhost",
    user="root",
    password="2007",
    database="hps"
)
mycursor= mydb.cursor()

def add_pharmacy_bill():
    P_Id = int(input("Enter Patient ID:"))
    Receipt_Number = int(input("Enter Receipt Number:"))
    Medicines = input("Enter Medicines:")
    Precribed_by = input("Enter Prescribed by (Doctor's Name):")
    Med_charges = float(input("Enter Medicine Charges:"))
    query_new_pharmacy = '''INSERT INTO pharmacy(
    P_Id,
    Receipt_Number,
    Medicines,
    Precribed_by,
    Med_charges
    )
    VALUE(%s,%s,%s,%s,%s)
    '''
    val_pharmacy_insert = (P_Id, Receipt_Number, Medicines, Precribed_by, Med_charges)
    mycursor.execute(query_new_pharmacy, val_pharmacy_insert)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("New Pharmacy Bill Added Successfully")
    print("Bill No:",mycursor.lastrowid)
    print("-----------------------------------------------------------------")

def update_pharmacy_bill():
    Bill_No = int(input("Enter Bill Number to update:"))
    P_Id = int(input("Enter Patient ID:"))
    Receipt_Number = int(input("Enter Receipt Number:"))
    Medicines = input("Enter Medicines:")
    Precribed_by = input("Enter Prescribed by (Doctor's Name):")
    Med_charges = float(input("Enter Medicine Charges:"))
    query_update_pharmacy = '''Update pharmacy SET
    P_Id=%s,
    Receipt_Number=%s,
    Medicines=%s,
    Precribed_by=%s,
    Med_charges=%s
    where Bill_No=%s'''
    val_pharmacy_update = (P_Id, Receipt_Number, Medicines, Precribed_by, Med_charges, Bill_No)
    mycursor.execute(query_update_pharmacy, val_pharmacy_update)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Pharmacy Bill details updated")
    print("-----------------------------------------------------------------")

def search_by_bill_no():
    Bill_No = int(input("Enter Bill Number:"))
    query_pharmacy_fetch = '''SELECT * FROM pharmacy WHERE Bill_No = %s'''
    val_fetch = (Bill_No,)
    mycursor.execute(query_pharmacy_fetch, val_fetch)
    record_fetchone = mycursor.fetchone()
    if record_fetchone:
        print("-----------------------------------------------------------------")
        print("Pharmacy Bill Record")
        print("Bill Number:", record_fetchone[0])
        print("Patient ID:", record_fetchone[1])
        print("Receipt Number:", record_fetchone[2])
        print("Medicines:", record_fetchone[3])
        print("Prescribed By:", record_fetchone[4])
        print("Medicine Charges:", record_fetchone[5])
        print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No pharmacy bill found with that Bill Number.")
        print("-----------------------------------------------------------------")

def search_pharmacy_by_pid():
    P_Id = int(input("Enter Patient ID:"))
    query_pharmacy_fetch_pid = '''SELECT * FROM pharmacy WHERE P_Id = %s'''
    val_fetch = (P_Id,)
    mycursor.execute(query_pharmacy_fetch_pid, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Pharmacy Bills for Patient ID:", P_Id)
        for row in record_fetchall:
            print("Bill Number:", row[0])
            print("Patient ID:", row[1])
            print("Receipt Number:", row[2])
            print("Medicines:", row[3])
            print("Prescribed By:", row[4])
            print("Medicine Charges:", row[5])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No pharmacy bills found for that Patient ID.")
        print("-----------------------------------------------------------------")

def search_pharmacy_by_receipt():
    Receipt_Number = int(input("Enter Receipt Number:"))
    query_pharmacy_fetch = '''SELECT * FROM pharmacy WHERE Receipt_Number = %s'''
    val_fetch = (Receipt_Number,)
    mycursor.execute(query_pharmacy_fetch, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Pharmacy Records found for Receipt Number:", Receipt_Number)
        for row in record_fetchall:
            print("Bill Number:", row[0])
            print("Patient ID:", row[1])
            print("Receipt Number:", row[2])
            print("Medicines:", row[3])
            print("Prescribed By:", row[4])
            print("Medicine Charges:", row[5])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No pharmacy records found for that Receipt Number.")
        print("-----------------------------------------------------------------")

def all_pharmacy_records():
    query_pharmacy_fetch_all = '''SELECT * FROM pharmacy'''
    mycursor.execute(query_pharmacy_fetch_all)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("All Pharmacy Records")
        for row in record_fetchall:
            print("Bill Number:", row[0])
            print("Patient ID:", row[1])
            print("Receipt Number:", row[2])
            print("Medicines:", row[3])
            print("Prescribed By:", row[4])
            print("Medicine Charges:", row[5])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No pharmacy records found.")
        print("-----------------------------------------------------------------")

def clear_pharmacy_record():
    Bill_No = int(input("Enter Bill Number to delete:"))
    query_pharmacy_delete_one = '''DELETE FROM pharmacy WHERE Bill_No = %s'''
    val_pharmacy_deleteone = (Bill_No,)
    mycursor.execute(query_pharmacy_delete_one, val_pharmacy_deleteone)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Pharmacy Bill Deleted Successfully")
    print("-----------------------------------------------------------------")

def clear_all_pharmacy_records():
    query_pharmacy_deleteall = '''DELETE FROM pharmacy'''
    mycursor.execute(query_pharmacy_deleteall)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("All pharmacy data cleared")
    print("-----------------------------------------------------------------")
