import mysql.connector as m

mydb=m.connect(
    host= "localhost",
    user="root",
    password="2007",
    database="hps"
)
mycursor= mydb.cursor()

def add_test_record():
    P_Id = int(input("Enter Patient ID:"))
    Xray = input("X-ray status (e.g., Done, Not Done):")
    CT_Scan = input("CT Scan status:")
    MRI = input("MRI status:")
    UltraSound = input("Ultrasound status:")
    EEG = input("EEG status:")
    ECG = input("ECG status:")
    query_new_test = '''INSERT INTO tests(
    P_Id,
    Xray,
    CT_Scan,
    MRI,
    UltraSound,
    EEG,
    ECG
    )
    VALUE%s,%s,%s,%s,%s,%s,%s)
    '''
    val_test_insert = (P_Id, Xray, CT_Scan, MRI, UltraSound, EEG, ECG)
    mycursor.execute(query_new_test, val_test_insert)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("New Test Record Added Successfully")
    print("-----------------------------------------------------------------")

def update_test_record():
    TEST_No = int(input("Enter Test Number to update:"))
    P_Id = int(input("Enter Patient ID:"))
    Xray = input("X-ray status (e.g., Done, Not Done):")
    CT_Scan = input("CT Scan status:")
    MRI = input("MRI status:")
    UltraSound = input("Ultrasound status:")
    EEG = input("EEG status:")
    ECG = input("ECG status:")
    query_update_test = '''Update tests SET
    P_Id=%s,
    Xray=%s,
    CT_Scan=%s,
    MRI=%s,
    UltraSound=%s,
    EEG=%s,
    ECG=%s
    where TEST_No=%s'''
    val_test_update = (P_Id, Xray, CT_Scan, MRI, UltraSound, EEG, ECG, TEST_No)
    mycursor.execute(query_update_test, val_test_update)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Test Record details updated")
    print("-----------------------------------------------------------------")

def search_by_test_no():
    TEST_No = int(input("Enter Test Number:"))
    query_test_fetch = '''SELECT * FROM tests WHERE TEST_No = %s'''
    val_fetch = (TEST_No,)
    mycursor.execute(query_test_fetch, val_fetch)
    record_fetchone = mycursor.fetchone()
    if record_fetchone:
        print("-----------------------------------------------------------------")
        print("Test Record")
        print("Test Number:", record_fetchone[0])
        print("Patient ID:", record_fetchone[1])
        print("X-ray:", record_fetchone[2])
        print("CT Scan:", record_fetchone[3])
        print("MRI:", record_fetchone[4])
        print("Ultrasound:", record_fetchone[5])
        print("EEG:", record_fetchone[6])
        print("ECG:", record_fetchone[7])
        print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No test record found with that Test Number.")
        print("-----------------------------------------------------------------")

def search_tests_by_pid():
    P_Id = int(input("Enter Patient ID:"))
    query_test_fetch_pid = '''SELECT * FROM tests WHERE P_Id = %s'''
    val_fetch = (P_Id,)
    mycursor.execute(query_test_fetch_pid, val_fetch)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("Test Records for Patient ID:", P_Id)
        for row in record_fetchall:
            print("Test Number:", row[0])
            print("Patient ID:", row[1])
            print("X-ray:", row[2])
            print("CT Scan:", row[3])
            print("MRI:", row[4])
            print("Ultrasound:", row[5])
            print("EEG:", row[6])
            print("ECG:", row[7])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No test records found for that Patient ID.")
        print("-----------------------------------------------------------------")
        
def all_test_records():
    query_test_fetch_all = '''SELECT * FROM tests'''
    mycursor.execute(query_test_fetch_all)
    record_fetchall = mycursor.fetchall()
    if record_fetchall:
        print("-----------------------------------------------------------------")
        print("All Test Records")
        for row in record_fetchall:
            print("Test Number:", row[0])
            print("Patient ID:", row[1])
            print("X-ray:", row[2])
            print("CT Scan:", row[3])
            print("MRI:", row[4])
            print("Ultrasound:", row[5])
            print("EEG:", row[6])
            print("ECG:", row[7])
            print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print("No test records found.")
        print("-----------------------------------------------------------------")

def clear_test_record():
    TEST_No = int(input("Enter Test Number to delete:"))
    query_test_delete_one = '''DELETE FROM tests WHERE TEST_No = %s'''
    val_test_deleteone = (TEST_No,)
    mycursor.execute(query_test_delete_one, val_test_deleteone)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("Test Record Deleted Successfully")
    print("-----------------------------------------------------------------")

def clear_all_test_records():
    query_test_deleteall = '''DELETE FROM tests'''
    mycursor.execute(query_test_deleteall)
    mydb.commit()
    print("-----------------------------------------------------------------")
    print("All test data cleared")
    print("-----------------------------------------------------------------")