import mysql.connector as m

mydb=m.connect(
    host= "localhost",
    user="root",
    password="2007",
    database="hps"
)
mycursor= mydb.cursor()
def add_referral_record():
    Referral_Number = int(input("Enter Referral Number:"))
    Insurance_company = input("Enter Insurance Company:")
    CGHS = input("Enter CGHS status:")
    CAPF_AYUSHMAN = input("Enter CAPF AYUSHMAN status:")
    AYUSHMAN_BHARAT = input("Enter AYUSHMAN BHARAT status:")
    ECHS = input("Enter ECHS status:")
    Hospital_Name = input("Enter Hospital Name:")
    Receipt_Number = int(input("Enter Receipt Number:"))
    P_Id = int(input("Enter Patient ID:"))
    query_new_referral = '''INSERT INTO refer(
    Referral_Number,
    Insurance_company,
    CGHS,
    CAPF_AYUSHMAN,
    AYUSHMAN_BHARAT,
    ECHS,
    Hospital_Name,
    Receipt_Number,
    P_Id
    )
    VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    val_referral_insert = (Referral_Number, Insurance_company, CGHS, CAPF_AYUSHMAN, AYUSHMAN_BHARAT, ECHS, Hospital_Name, Receipt_Number, P_Id)
    mycursor.execute(query_new_referral, val_referral_insert)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("New Referral Record Added Successfully")
    print("-----------------------------------------------------------------")

def update_referral_record():
    Referral_Number = int(input("Enter Referral Number to update:"))
    Insurance_company = input("Enter New Insurance Company:")
    CGHS = input("Enter New CGHS status:")
    CAPF_AYUSHMAN = input("Enter New CAPF AYUSHMAN status:")
    AYUSHMAN_BHARAT = input("Enter New AYUSHMAN BHARAT status:")
    ECHS = input("Enter New ECHS status:")
    Hospital_Name = input("Enter New Hospital Name:")
    Receipt_Number = int(input("Enter New Receipt Number:"))
    P_Id = int(input("Enter New Patient ID:"))
    query_update_referral = '''Update refer SET
    Insurance_company=%s,
    CGHS=%s,
    CAPF_AYUSHMAN=%s,
    AYUSHMAN_BHARAT=%s,
    ECHS=%s,
    Hospital_Name=%s,
    Receipt_Number=%s,
    P_Id=%s
    where Referral_Number=%s'''
    val_referral_update = (Insurance_company, CGHS, CAPF_AYUSHMAN, AYUSHMAN_BHARAT, ECHS, Hospital_Name, Receipt_Number, P_Id, Referral_Number)
    mycursor.execute(query_update_referral, val_referral_update)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Referral Record details updated")
    print("-----------------------------------------------------------------")

def search_by_referral_no():
    Referral_Number = int(input("Enter Referral Number:"))
    query_referral_fetch = '''SELECT * FROM refer WHERE Referral_Number = %s'''
    val_fetch = (Referral_Number,)
    mycursor.execute(query_referral_fetch, val_fetch)
    record_fetchone = mycursor.fetchone()
    if record_fetchone:
        print("-----------------------------------------------------------------")
        print("Referral Record")
        print("Referral Number:", record_fetchone[0])
        print("Insurance Company:", record_fetchone[1])
        print("CGHS:", record_fetchone[2])
        print("CAPF AYUSHMAN:", record_fetchone[3])
        print("AYUSHMAN BHARAT:", record_fetchone[4])
        print("ECHS:", record_fetchone[5])
        print("Hospital Name:", record_fetchone[6])
        print("Receipt Number:", record_fetchone[7])
        print("Patient ID:", record_fetchone[8])
        print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No referral record found with that Referral Number.")
        print("-----------------------------------------------------------------")

def search_referrals_by_pid():
    P_Id = int(input("Enter Patient ID:"))
    query_referral_fetch_pid = '''SELECT * FROM refer WHERE P_Id = %s'''
    val_fetch = (P_Id,)
    mycursor.execute(query_referral_fetch_pid, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Referral Records for Patient ID:", P_Id)
        for row in record_fetchall:
            print("Referral Number:", row[0])
            print("Insurance Company:", row[1])
            print("CGHS:", row[2])
            print("CAPF AYUSHMAN:", row[3])
            print("AYUSHMAN BHARAT:", row[4])
            print("ECHS:", row[5])
            print("Hospital Name:", row[6])
            print("Receipt Number:", row[7])
            print("Patient ID:", row[8])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No referral records found for that Patient ID.")
        print("-----------------------------------------------------------------")

def search_referrals_by_receipt():
    Receipt_Number = int(input("Enter Receipt Number:"))
    query_referral_fetch = '''SELECT * FROM refer WHERE Receipt_Number = %s'''
    val_fetch = (Receipt_Number,)
    mycursor.execute(query_referral_fetch, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Referral Records found for Receipt Number:", Receipt_Number)
        for row in record_fetchall:
            print("Referral Number:", row[0])
            print("Insurance Company:", row[1])
            print("CGHS:", row[2])
            print("CAPF AYUSHMAN:", row[3])
            print("AYUSHMAN BHARAT:", row[4])
            print("ECHS:", row[5])
            print("Hospital Name:", row[6])
            print("Receipt Number:", row[7])
            print("Patient ID:", row[8])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No referral records found for that Receipt Number.")
        print("-----------------------------------------------------------------")

def all_referral_records():
    query_referral_fetch_all = '''SELECT * FROM refer'''
    mycursor.execute(query_referral_fetch_all)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("All Referral Records")
        for row in record_fetchall:
            print("Referral Number:", row[0])
            print("Insurance Company:", row[1])
            print("CGHS:", row[2])
            print("CAPF AYUSHMAN:", row[3])
            print("AYUSHMAN BHARAT:", row[4])
            print("ECHS:", row[5])
            print("Hospital Name:", row[6])
            print("Receipt Number:", row[7])
            print("Patient ID:", row[8])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No referral records found.")
        print("-----------------------------------------------------------------")

def clear_referral_record():
    Referral_Number = int(input("Enter Referral Number to delete:"))
    query_referral_delete_one = '''DELETE FROM refer WHERE Referral_Number = %s'''
    val_referral_deleteone = (Referral_Number,)
    mycursor.execute(query_referral_delete_one, val_referral_deleteone)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Referral Record Deleted Successfully")
    print("-----------------------------------------------------------------")

def clear_all_referral_records():
    query_referral_deleteall = '''DELETE FROM refer'''
    mycursor.execute(query_referral_deleteall)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("All referral data cleared")
    print("-----------------------------------------------------------------")