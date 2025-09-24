import mysql.connector as m

mydb=m.connect(
    host= "localhost",
    user="root",
    password="2007",
    database="hps"
)
mycursor= mydb.cursor()

def add_billing_record():
    Receipt_Date = input("Enter Receipt Date (YYYY-MM-DD):")
    Payment_Mode = input("Enter Payment Mode:")
    P_Id = int(input("Enter Patient ID:"))
    query_new_billing = '''INSERT INTO billing(
    Receipt_Date,
    Payment_Mode,
    P_Id
    )
    VALUE%s,%s,%s)
    '''
    val_billing_insert = (Receipt_Date, Payment_Mode, P_Id)
    mycursor.execute(query_new_billing, val_billing_insert)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("New Billing Record Added Successfully")
    print("Receipt Number:",mycursor.lastrowid)
    print("-----------------------------------------------------------------")

def update_billing_record():
    Receipt_Number = int(input("Enter Receipt Number to update:"))
    Receipt_Date = input("Enter New Receipt Date (YYYY-MM-DD):")
    Payment_Mode = input("Enter New Payment Mode:")
    P_Id = int(input("Enter New Patient ID:"))
    query_update_billing = '''Update billing SET
    Receipt_Date=%s,
    Payment_Mode=%s,
    P_Id=%s
    where Receipt_Number=%s'''
    val_billing_update = (Receipt_Date, Payment_Mode, P_Id, Receipt_Number)
    mycursor.execute(query_update_billing, val_billing_update)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Billing Record details updated")
    print("-----------------------------------------------------------------")

def search_by_receipt_number():
    Receipt_Number = int(input("Enter Receipt Number:"))
    query_billing_fetch = '''SELECT * FROM billing WHERE Receipt_Number = %s'''
    val_fetch = (Receipt_Number,)
    mycursor.execute(query_billing_fetch, val_fetch)
    record_fetchone = mycursor.fetchone()
    if record_fetchone:
        print("-----------------------------------------------------------------")
        print("Billing Record")
        print("Receipt Number:", record_fetchone[0])
        print("Receipt Date:", record_fetchone[1])
        print("Payment Mode:", record_fetchone[2])
        print("Patient ID:", record_fetchone[3])
        print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No billing record found with that Receipt Number.")
        print("-----------------------------------------------------------------")

def search_billing_by_pid():
    P_Id = int(input("Enter Patient ID:"))
    query_billing_fetch_pid = '''SELECT * FROM billing WHERE P_Id = %s'''
    val_fetch = (P_Id,)
    mycursor.execute(query_billing_fetch_pid, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Billing Records for Patient ID:", P_Id)
        for row in record_fetchall:
            print("Receipt Number:", row[0])
            print("Receipt Date:", row[1])
            print("Payment Mode:", row[2])
            print("Patient ID:", row[3])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No billing records found for that Patient ID.")
        print("-----------------------------------------------------------------")

def all_billing_records():
    query_billing_fetch_all = '''SELECT * FROM billing'''
    mycursor.execute(query_billing_fetch_all)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("All Billing Records")
        for row in record_fetchall:
            print("Receipt Number:", row[0])
            print("Receipt Date:", row[1])
            print("Payment Mode:", row[2])
            print("Patient ID:", row[3])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No billing records found.")
        print("-----------------------------------------------------------------")

def clear_billing_record():
    Receipt_Number = int(input("Enter Receipt Number to delete:"))
    query_billing_delete_one = '''DELETE FROM billing WHERE Receipt_Number = %s'''
    val_billing_deleteone = (Receipt_Number,)
    mycursor.execute(query_billing_delete_one, val_billing_deleteone)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Billing Record Deleted Successfully")
    print("-----------------------------------------------------------------")

def clear_all_billing_records():
    query_billing_deleteall = '''DELETE FROM billing'''
    mycursor.execute(query_billing_deleteall)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("All billing data cleared")
    print("-----------------------------------------------------------------")
