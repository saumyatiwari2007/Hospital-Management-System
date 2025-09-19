import mysql.connector as m

mydb=m.connect(
    host= "localhost",
    user="root",
    password="2007",
    database="hps"
)
mycursor= mydb.cursor()
print("connected ")

def new_pateint():
    P_Id=int(input("Enter Patient ID:"))
    Patient_Name=input("Enter Patient Name:")
    Age=int(input("Enter Patient Age:"))
    Gender= input("Enter Patient Gender (M/F):")
    Adress= input("Enter Patient Address (50ch):")
    Contact= input("Enter Patient Contact(+91):")
    query_new_patient='''INSERT INTO Patient(
    P_Id,
    Patient_Name,
    Age,
    Gender,
    Adress,
    Contact
    )
    VALUE(%s,%s,%s,%s,%s,%s)
    '''
    val_patient_insert= (P_Id,Patient_Name,Age,Gender,Adress,Contact)
    mycursor.execute(query_new_patient,val_patient_insert)
    mydb.commit()
    exe_patient_insert= True
    print("New Record Added Successfully")

def update_pateint_details():
    P_Id=int(input("Enter Patient ID:"))
    Patient_Name=input("Enter Patient Name:")
    Age=int(input("Enter Patient Age:"))
    Gender= input("Enter Patient Gender (M/F):")
    Adress= input("Enter Patient Address (50ch):")
    Contact= input("Enter Patient Contact(+91):")
    query_update_patient= ''' UPDATE Patient SET Patient_Name=%s,
    Age=%s,
    Gender=%s,
    Adress=%s,
    Contact=%s
    where P_Id= %s'''
    val_patient_update=(Patient_Name,Age,Gender,Adress,Contact,P_Id)
    mycursor.execute(query_update_patient,val_patient_update)
    mydb.commit()
    print("Data Updated")
    print("-----------------------------------------------------------------")
    exe_patient_update= True

def search_by_pdId():
    P_Id= int(input("Enter Patient ID:"))
    query_Patient_fetch= '''Select * From Patient
    where P_Id=%s'''
    val_fetch=(P_Id,)
    mycursor.execute(query_Patient_fetch,val_fetch)
    record_fetchone= mycursor.fetchone()
    print("-----------------------------------------------------------------")
    print("Patient Record")
    print("Patient ID:",record_fetchone[0])
    print("Patient Name:", record_fetchone[1])
    print("Age:",record_fetchone[2])
    print("Gender:",record_fetchone[3])
    print("Address:",record_fetchone[4])
    print("Contact:",record_fetchone[5])
    print("-----------------------------------------------------------------")
    exe_patient_fetch= True

def search_by_name_patient():
    Patient_Name= input("Enter Patient name:")
    query_Patient_fetchname= '''Select * From Patient
    where patient_name=%s'''
    val_fetch=(Patient_Name,)
    mycursor.execute(query_Patient_fetchname,val_fetch)
    record_fetchone= mycursor.fetchone()
    print("-----------------------------------------------------------------")
    print("Patient Record")
    print("Patient ID:",record_fetchone[0])
    print("Patient Name:", record_fetchone[1])
    print("Age:",record_fetchone[2])
    print("Gender:",record_fetchone[3])
    print("Address:",record_fetchone[4])
    print("Contact:",record_fetchone[5])
    print("-----------------------------------------------------------------")
    exe_patient_fetch= True

def all_pateint_records():
    query_Patient_fetch_all = '''Select * From Patient'''
    mycursor.execute(query_Patient_fetch_all)
    record_fetchall= mycursor.fetchall()
    print("-----------------------------------------------------------------")
    print("Patient Record")
    for row in record_fetchall:
            print("Patient ID:",row[0])
            print("Patient Name:", row[1])
            print("Age:",row[2])
            print("Gender:",row[3])
            print("Address:",row[4])
            print("Contact:",row[5])
            print("-----------------------------------------------------------------")
    exe_patient_fetch= True