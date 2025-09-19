import mysql.connector as m

mydb=m.connect(
    host= "localhost",
    user="root",
    password="2007",
    database="hps"
)
mycursor= mydb.cursor()
print("connected ")

while True:
    print("-----------------------------------------------------------------")
    print("Main Menu")
    print("-----------------------------------------------------------------")
    print("1.Patient", "2.Employee", "3.Doctors", "4.Pharmacy", "5.Pathology", "6.Billing", "7.Tests", "8.OPD", "9.Admission/Discharge", "10.Referral", sep= "\n")
    print("-----------------------------------------------------------------")
    user_option = int(input("enter your option:"))
    while True:
        if user_option == 1:
            print("-----------------------------------------------------------------")
            print("Patient")
            print("-----------------------------------------------------------------")
            print("1.Add new Patient")
            print("2.Update Patient details")
            print("3.Search by P_Id")
            print("4.Search by Name")
            print("5.Show all records")
            print("6.Clear a Patient record")
            print("7.Clear all records")
            print("8.Exit to main menu")
            print("-----------------------------------------------------------------")
            user_option_patient= int(input("Enter Your option:"))
            if user_option_patient == 1:
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
                print("-----------------------------------------------------------------")
                if exe_patient_insert == True:
                    Exit_input= int(input("press 1 to go back:"))
                    continue

            if user_option_patient== 2:
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
                if exe_patient_update== True:
                   Exit_update= int(input("Press 1 to go back"))
                   continue

            if user_option_patient== 3:
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
                if exe_patient_fetch == True:
                    Exit_fetch= int(input("Press 1 to go back:"))
                    continue

                
            if user_option_patient == 4:
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
                if exe_patient_fetch == True:
                    Exit_fetch= int(input("Press 1 to go back:"))
                    continue

            if user_option_patient == 5:
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
                if exe_patient_fetch == True:
                    Exit_fetch= int(input("Press 1 to go back:"))
                    continue

            if user_option_patient== 6:
                P_Id= int(input("Enter Patient ID:"))
                query_patient_Delete_one= '''Delete from patient where P_Id= %s'''
                val_Patient_deleteone=(P_Id,)
                mycursor.execute(query_patient_Delete_one,val_Patient_deleteone)
                mydb.commit()
                print("-----------------------------------------------------------------")
                print("Patient record Deleted")
                print("-----------------------------------------------------------------")
                exe_patient_deleteone= True
                if exe_patient_deleteone == True:
                    exit_deleteone= int(input("press 1 to go back"))
                    continue

            if user_option_patient==7:
                query_patient_deleteall= '''Delete from patient'''
                mycursor.execute(query_patient_deleteall)
                mydb.commit()
                print("-----------------------------------------------------------------")
                print("All data cleared")
                print("-----------------------------------------------------------------")
                exe_patient_deleteall= True
                if exe_patient_deleteall == True:
                    exit_deleteall =int(input("press 1 to go back"))
                    continue
                
            if user_option_patient == 8:
                print("exit to main menu")
                break


    
        if user_option == 2:
            print("-----------------------------------------------------------------")
            print("Employee")
            print("-----------------------------------------------------------------")
            print("1.Add new Employee")
            print("2.Update Employee details")
            print("3.Search by E_Id")
            print("4.Search by Name")
            print("5.Show all records")
            print("6.Clear a Employee record")
            print("7.Search by Designation")
            print("8.Search by OPD")
            print("9.Search Specialists")
            print("10.Search for Surgeon")
            print("11.Search for Physician")
            print("12.Exit to main menu")
            print("-----------------------------------------------------------------")
            user_option_employee= int(input("Enter Your option:"))
            if user_option_employee == 1:
                Emp_Id=int(input("Enter Employee ID:"))
                Emp_Name=input("Enter Employee Name:")
                Emp_Age=int(input("Enter Employee Age:"))
                Emp_Gender= input("Enter Employee Gender (M/F):")
                Emp_Adress= input("Enter Employee Address (50ch):")
                Emp_Contact= input("Enter Patient Contact(+91):")
                Emp_Designation= input("Enter Employee Designation:")
                Emp_Salary = int(input("Enter Employee Salary:"))
                opd= int(input("OPD STATUS Active(1)/Inactive(0)"))
                Specialists =input("Enter Doctor Speicality:")
                surgeon = input("Enter Surgeon:")
                Physician = input("Enter Physician:")
                Active_Status = int(input("Enter Active Status Active(1)/Inactive(0)"))

                query_new_employee='''INSERT INTO Employee(
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
                val_employee_insert= (Emp_Id,Emp_Name,Emp_Age,Emp_Gender,Emp_Adress,Emp_Contact,Emp_Designation,Emp_Salary,opd,Specialists,surgeon,Physician,Active_Status)
                mycursor.execute(query_new_employee,val_employee_insert)
                mydb.commit()
                exe_employee_insert= True
                print("-----------------------------------------------------------------")
                print("New Employee Added Successfully")
                print("-----------------------------------------------------------------")
                if exe_employee_insert == True:
                    Exit_input= int(input("press 1 to go back:"))
                    continue  
            
            if user_option_employee == 2:
                Emp_Id=int(input("Enter Employee ID:"))
                Emp_Name=input("Enter Employee Name:")
                Emp_Age=int(input("Enter Employee Age:"))
                Emp_Gender= input("Enter Employee Gender (M/F):")
                Emp_Adress= input("Enter Employee Address (50ch):")
                Emp_Contact= input("Enter Patient Contact(+91):")
                Emp_Designation= input("Enter Employee Designation:")
                Emp_Salary = int(input("Enter Employee Salary:"))
                opd= int(input("OPD STATUS Active(1)/Inactive(0)"))
                Specialists =input("Enter Doctor Speicality:")
                surgeon = input("Enter Surgeon:")
                Physician = input("Enter Physician:")
                Active_Status = int(input("Enter Active Status Active(1)/Inactive(0)"))
                query_update_employee='''Update Employee Set
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
                val_employee_update= (Emp_Name,Emp_Age,Emp_Gender,Emp_Adress,Emp_Contact,Emp_Designation,Emp_Salary,opd,Specialists,surgeon,Physician,Active_Status,Emp_Id)
                mycursor.execute(query_update_employee,val_employee_update)
                mydb.commit()
                exe_employee_insert= True
                print("-----------------------------------------------------------------")
                print("Employee Details updated")
                print("-----------------------------------------------------------------")
                if exe_employee_insert == True:
                    Exit_input= int(input("press 1 to go back:"))
                    continue  

            if user_option_employee== 3:
                Emp_Id= int(input("Enter Employee ID:"))
                query_Employee_fetch= '''Select * From Employee
                where Emp_Id=%s'''
                val_fetch=(Emp_Id,)
                mycursor.execute(query_Employee_fetch,val_fetch)
                record_fetchone= mycursor.fetchone()
                print("-----------------------------------------------------------------")
                print("Employee Record")
                print("-----------------------------------------------------------------")
                print("Employee ID:",record_fetchone[0])
                print("Employee Name:", record_fetchone[1])
                print("Age:",record_fetchone[2])
                print("Gender:",record_fetchone[3])
                print("Address:",record_fetchone[4])
                print("Contact:",record_fetchone[5])
                print("-----------------------------------------------------------------")
                exe_employee_fetch= True
                if exe_employee_fetch == True:
                    Exit_fetch= int(input("Press 1 to go back:"))
                    continue

            if user_option_employee == 4:
                Emp_Name_= input("Enter Employee name:")
                query_employee_fetchname= '''Select * From Employee
                where emp_name=%s'''
                val_fetch=(Emp_Name,)
                mycursor.execute(query_employee_fetchname,val_fetch)
                record_fetchone= mycursor.fetchone()
                print("-----------------------------------------------------------------")
                print("Employee Record")
                print("-----------------------------------------------------------------")
                print("Employee ID:",record_fetchone[0])
                print("Employee Name:", record_fetchone[1])
                print("Age:",record_fetchone[2])
                print("Gender:",record_fetchone[3])
                print("Address:",record_fetchone[4])
                print("Contact:",record_fetchone[5])
                print("-----------------------------------------------------------------")
                exe_patient_fetch= True
                if exe_patient_fetch == True:
                    Exit_fetch= int(input("Press 1 to go back:"))
                    continue

            if user_option_employee == 5:
                query_employee_fetch_all = '''Select * From Employee'''
                mycursor.execute(query_employee_fetch_all)
                record_fetchall= mycursor.fetchall()
                print("-----------------------------------------------------------------")
                print("Employee Record")
                print("-----------------------------------------------------------------")
                
                for row in record_fetchall:
                        print("Employee ID:",row[0])
                        print("Employee Name:", row[1])
                        print("Age:",row[2])
                        print("Gender:",row[3])
                        print("Address:",row[4])
                        print("Contact:",row[5])
                        print("-----------------------------------------------------------------")
                exe_employee_fetch= True
                if exe_employee_fetch == True:
                    Exit_fetch= int(input("Press 1 to go back:"))
                    continue
                
            
            if user_option_employee == 6:
                Emp_Id= int(input("Enter Employee ID:"))
                query_employee_Delete_one= '''Delete from employee where Emp_Id= %s'''
                val_employee_deleteone=(Emp_Id,)
                mycursor.execute(query_employee_Delete_one,val_employee_deleteone)
                mydb.commit()
                print("-----------------------------------------------------------------")
                print("Employee record Deleted")
                print("-----------------------------------------------------------------")
                exe_employee_deleteone= True
                if exe_employee_deleteone == True:
                    exit_deleteone= int(input("press 1 to go back"))
                    continue
                
            if user_option_employee== 7:
                Emp_Designation= input("Enter Employee Designation:")
                query_employee_designation= ''' select * from employee
                where Emp_Designation = %s
                '''
                val_employee_designation=(Emp_Designation,)
                mycursor.execute(query_employee_designation,val_employee_designation)
                record_fetchall= mycursor.fetchall()
                print("-----------------------------------------------------------------")
                print("Employee Record")
                print("-----------------------------------------------------------------")
                
                for row in record_fetchall:
                        print("Employee ID:",row[0])
                        print("Employee Name:", row[1])
                        print("Age:",row[2])
                        print("Gender:",row[3])
                        print("Address:",row[4])
                        print("Contact:",row[5])
                        print("-----------------------------------------------------------------")
                exe_employee_designation= True
                if exe_employee_designation == True:
                    Exit_fetch= int(input("Press 1 to go back:"))
                    continue
                
            
            if user_option_employee == 8:
                print("exit to main menu")
                break
        
        
        if user_option == 3:
            print("-----------------------------------------------------------------")
            print("Doctors")
            print("-----------------------------------------------------------------")
            print("1.Add new Doctor")
            print("2.Update Doctor details")
            print("3.Search by Doc_Id")
            print("4.Search by Name")
            print("5.Show all records")
            print("6.Clear a Doctor record")
            print("7.Search by OPD")
            print("8.Search Specialists")
            print("9.Search for Surgeon")
            print("10.Search for Physician")
            print("11.Exit to main menu") 
            
            print("-----------------------------------------------------------------")

            print("Doctos")
        elif user_option == 4:
            print("Pharmacy")
        elif user_option == 5:
            print("Pathology")
        elif user_option == 6:
            print("Billing")
        elif user_option == 7:
            print("tests")
        elif user_option == 8:
            print("OPD")
        elif user_option == 9:
            print("Admission/Discharge")
        elif user_option == 10:
            print("Referral")
        else:
            print("invalid option")