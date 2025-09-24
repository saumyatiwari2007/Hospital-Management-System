import mysql.connector as m

mydb=m.connect(
    host= "localhost",
    user="root",
    password="2007",
    database="hps"
)
mycursor= mydb.cursor()

def add_admission_record():
    P_Id = int(input("Enter Patient ID:"))
    Payment_Mode = input("Enter Payment Mode:")
    Admisson_date = input("Enter Admission Date (YYYY-MM-DD):")
    Doctor = input("Enter Doctor's Name:")
    Referral_Number = input("Enter Referral Number (optional, leave blank if none):")
    query_new_admission = '''INSERT INTO admission_discharge(
    P_Id,
    Payment_Mode,
    Admisson_date,
    Doctor,
    Referral_Number
    )
    VALUE(%s,%s,%s,%s,%s)
    '''
    val_admission_insert = (P_Id, Payment_Mode, Admisson_date, Doctor, Referral_Number if Referral_Number else None)
    mycursor.execute(query_new_admission, val_admission_insert)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("New Admission Record Added Successfully")
    print("Admission No:",mycursor.lastrowid)
    print("-----------------------------------------------------------------")

def update_admission_record():
    Admission_No = int(input("Enter Admission Number to update:"))
    P_Id = int(input("Enter Patient ID:"))
    Payment_Mode = input("Enter New Payment Mode:")
    Admisson_date = input("Enter New Admission Date (YYYY-MM-DD):")
    Discharge_date = input("Enter New Discharge Date (YYYY-MM-DD, or leave blank):")
    Doctor = input("Enter Doctor's Name:")
    Referral_Number = input("Enter New Referral Number (optional, leave blank if none):")
    query_update_admission = '''Update admission_discharge SET
    P_Id=%s,
    Payment_Mode=%s,
    Admisson_date=%s,
    Discharge_date=%s,
    Doctor=%s,
    Referral_Number=%s
    where Admission_No=%s'''
    val_admission_update = (P_Id, Payment_Mode, Admisson_date, Discharge_date if Discharge_date else None, Doctor, Referral_Number if Referral_Number else None, Admission_No)
    mycursor.execute(query_update_admission, val_admission_update)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Admission Record details updated")
    print("-----------------------------------------------------------------")

def search_by_admission_no():
    Admission_No = int(input("Enter Admission Number:"))
    query_admission_fetch = '''SELECT * FROM admission_discharge WHERE Admission_No = %s'''
    val_fetch = (Admission_No,)
    mycursor.execute(query_admission_fetch, val_fetch)
    record_fetchone = mycursor.fetchone()
    if record_fetchone:
        print("-----------------------------------------------------------------")
        print("Admission Record")
        print("Patient ID:", record_fetchone[0])
        print("Admission Number:", record_fetchone[1])
        print("Payment Mode:", record_fetchone[2])
        print("Admission Date:", record_fetchone[3])
        print("Discharge Date:", record_fetchone[4])
        print("Doctor:", record_fetchone[5])
        print("Referral Number:", record_fetchone[6])
        print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No admission record found with that Admission Number.")
        print("-----------------------------------------------------------------")

def search_admissions_by_pid():
    P_Id = int(input("Enter Patient ID:"))
    query_admission_fetch_pid = '''SELECT * FROM admission_discharge WHERE P_Id = %s'''
    val_fetch = (P_Id,)
    mycursor.execute(query_admission_fetch_pid, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Admission Records for Patient ID:", P_Id)
        for row in record_fetchall:
            print("Patient ID:", row[0])
            print("Admission Number:", row[1])
            print("Payment Mode:", row[2])
            print("Admission Date:", row[3])
            print("Discharge Date:", row[4])
            print("Doctor:", row[5])
            print("Referral Number:", row[6])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No admission records found for that Patient ID.")
        print("-----------------------------------------------------------------")

def search_admissions_by_doctor():
    Doctor = input("Enter Doctor's Name:")
    query_admission_fetch_doctor = '''SELECT * FROM admission_discharge WHERE Doctor LIKE %s'''
    val_fetch = (f'%{Doctor}%',)
    mycursor.execute(query_admission_fetch_doctor, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Admission Records for Doctor:", Doctor)
        for row in record_fetchall:
            print("Patient ID:", row[0])
            print("Admission Number:", row[1])
            print("Payment Mode:", row[2])
            print("Admission Date:", row[3])
            print("Discharge Date:", row[4])
            print("Doctor:", row[5])
            print("Referral Number:", row[6])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No admission records found for that Doctor.")
        print("-----------------------------------------------------------------")

def all_admission_records():
    query_admission_fetch_all = '''SELECT * FROM admission_discharge'''
    mycursor.execute(query_admission_fetch_all)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("All Admission and Discharge Records")
        for row in record_fetchall:
            print("Patient ID:", row[0])
            print("Admission Number:", row[1])
            print("Payment Mode:", row[2])
            print("Admission Date:", row[3])
            print("Discharge Date:", row[4])
            print("Doctor:", row[5])
            print("Referral Number:", row[6])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No admission records found.")
        print("-----------------------------------------------------------------")

def clear_admission_record():
    Admission_No = int(input("Enter Admission Number to delete:"))
    query_admission_delete_one = '''DELETE FROM admission_discharge WHERE Admission_No = %s'''
    val_admission_deleteone = (Admission_No,)
    mycursor.execute(query_admission_delete_one, val_admission_deleteone)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Admission Record Deleted Successfully")
    print("-----------------------------------------------------------------")

def clear_all_admission_records():
    query_admission_deleteall = '''DELETE FROM admission_discharge'''
    mycursor.execute(query_admission_deleteall)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("All admission and discharge data cleared")
    print("-----------------------------------------------------------------")
