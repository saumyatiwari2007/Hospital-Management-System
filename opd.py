import mysql.connector as m

mydb=m.connect(
    host= "localhost",
    user="root",
    password="2007",
    database="hps"
)
mycursor= mydb.cursor()

def add_opd_record():
    P_Id = int(input("Enter Patient ID:"))
    Token_Number = int(input("Enter Token Number:"))
    OPD_Charges = float(input("Enter OPD Charges:"))
    Doctor = input("Enter Doctor's Name:")
    query_new_opd = '''INSERT INTO opd(
    P_Id,
    Token_Number,
    OPD_Charges,
    Doctor
    )
    VALUE(%s,%s,%s,%s)
    '''
    val_opd_insert = (P_Id, Token_Number, OPD_Charges, Doctor)
    mycursor.execute(query_new_opd, val_opd_insert)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("New OPD Record Added Successfully")
    print("-----------------------------------------------------------------")

def update_opd_record():
    Token_Number = int(input("Enter Token Number to update:"))
    P_Id = int(input("Enter Patient ID:"))
    OPD_Charges = float(input("Enter OPD Charges:"))
    Doctor = input("Enter Doctor's Name:")
    query_update_opd = '''Update opd SET
    P_Id=%s,
    OPD_Charges=%s,
    Doctor=%s
    where Token_Number=%s'''
    val_opd_update = (P_Id, OPD_Charges, Doctor, Token_Number)
    mycursor.execute(query_update_opd, val_opd_update)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("OPD Record details updated")
    print("-----------------------------------------------------------------")

def search_by_token_number():
    Token_Number = int(input("Enter Token Number:"))
    query_opd_fetch = '''SELECT * FROM opd WHERE Token_Number = %s'''
    val_fetch = (Token_Number,)
    mycursor.execute(query_opd_fetch, val_fetch)
    record_fetchone = mycursor.fetchone()
    if record_fetchone:
        print("-----------------------------------------------------------------")
        print("OPD Record")
        print("Patient ID:", record_fetchone[0])
        print("Token Number:", record_fetchone[1])
        print("OPD Charges:", record_fetchone[2])
        print("Doctor:", record_fetchone[3])
        print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No OPD record found with that Token Number.")
        print("-----------------------------------------------------------------")

def search_opd_by_pid():
    P_Id = int(input("Enter Patient ID:"))
    query_opd_fetch_pid = '''SELECT * FROM opd WHERE P_Id = %s'''
    val_fetch = (P_Id,)
    mycursor.execute(query_opd_fetch_pid, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("OPD Records for Patient ID:", P_Id)
        for row in record_fetchall:
            print("Patient ID:", row[0])
            print("Token Number:", row[1])
            print("OPD Charges:", row[2])
            print("Doctor:", row[3])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No OPD records found for that Patient ID.")
        print("-----------------------------------------------------------------")

def search_opd_by_doctor():
    Doctor = input("Enter Doctor's Name:")
    query_opd_fetch_doctor = '''SELECT * FROM opd WHERE Doctor LIKE %s'''
    val_fetch = (f'%{Doctor}%',)
    mycursor.execute(query_opd_fetch_doctor, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("OPD Records for Doctor:", Doctor)
        for row in record_fetchall:
            print("Patient ID:", row[0])
            print("Token Number:", row[1])
            print("OPD Charges:", row[2])
            print("Doctor:", row[3])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No OPD records found for that Doctor.")
        print("-----------------------------------------------------------------")

def all_opd_records():
    query_opd_fetch_all = '''SELECT * FROM opd'''
    mycursor.execute(query_opd_fetch_all)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("All OPD Records")
        for row in record_fetchall:
            print("Patient ID:", row[0])
            print("Token Number:", row[1])
            print("OPD Charges:", row[2])
            print("Doctor:", row[3])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No OPD records found.")
        print("-----------------------------------------------------------------")

def clear_opd_record():
    Token_Number = int(input("Enter Token Number to delete:"))
    query_opd_delete_one = '''DELETE FROM opd WHERE Token_Number = %s'''
    val_opd_deleteone = (Token_Number,)
    mycursor.execute(query_opd_delete_one, val_opd_deleteone)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("OPD Record Deleted Successfully")
    print("-----------------------------------------------------------------")

def clear_all_opd_records():
    query_opd_deleteall = '''DELETE FROM opd'''
    mycursor.execute(query_opd_deleteall)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("All OPD data cleared")
    print("-----------------------------------------------------------------")