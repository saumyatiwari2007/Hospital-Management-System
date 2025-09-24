from admission_discharge import *
from billing import*
from doctors import*
from employee import*
from opd import*
from pathology import*
from patients import*
from pharmacy import*
from referral import*
from tests import*

import mysql.connector as m

try:
    mydb=m.connect(
        host= "localhost",
        user="root",
        password="2007",
        database="hps"
    )
    mycursor= mydb.cursor()
    connection_respone= True
    print("connected ")

except:
    print("An error ocurred, please check your connection")

def main():
    while True:
        print("-----------------------------------------------------------------")
        print("Main Menu")
        print("-----------------------------------------------------------------")
        print("1. Patient")
        print("2. Employee")
        print("3. Doctors")
        print("4. Pharmacy")
        print("5. Pathology")
        print("6. Billing")
        print("7. Tests")
        print("8. OPD")
        print("9. Admission & Discharge")
        print("10. Referral")
        print("11. Exit")
        print("-----------------------------------------------------------------")

        try:
            user_option = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        print("-----------------------------------------------------------------")

        if user_option == 1:
            while True:
                print("-----------------------------------------------------------------")
                print("Patient Menu")
                print("-----------------------------------------------------------------")
                print("1. Add new Patient")
                print("2. Update Patient details")
                print("3. Search by P_Id")
                print("4. Search by Name")
                print("5. Show all records")
                print("6. Clear a Patient record")
                print("7. Exit to main menu")
                print("-----------------------------------------------------------------")
                try:
                    patient_option = int(input("Enter your option:"))
                    if patient_option == 1:
                        add_patient()
                    elif patient_option == 2:
                        update_patient_details()
                    elif patient_option == 3:
                        search_by_p_id()
                    elif patient_option == 4:
                        search_by_name_patient()
                    elif patient_option == 5:
                        all_patient_records()
                    elif patient_option == 6:
                        clear_patient_record()
                    elif patient_option == 7:
                        break
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif user_option == 2:
            while True:
                print("-----------------------------------------------------------------")
                print("Employee Menu")
                print("-----------------------------------------------------------------")
                print("1. Add new Employee")
                print("2. Update Employee details")
                print("3. Search by E_Id")
                print("4. Search by Name")
                print("5. Show all records")
                print("6. Clear an Employee record")
                print("7. Search by Designation")
                print("8. Exit to main menu")
                print("-----------------------------------------------------------------")
                try:
                    employee_option = int(input("Enter your option:"))
                    if employee_option == 1:
                        add_employee()
                    elif employee_option == 2:
                        update_employee_details()
                    elif employee_option == 3:
                        search_by_e_id()
                    elif employee_option == 4:
                        search_by_name_employee()
                    elif employee_option == 5:
                        all_employee_records()
                    elif employee_option == 6:
                        clear_employee_record()
                    elif employee_option == 7:
                        search_by_designation()
                    elif employee_option == 8:
                        break
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif user_option == 3:
            while True:
                print("-----------------------------------------------------------------")
                print("Doctors Menu")
                print("-----------------------------------------------------------------")
                print("1. Add new Doctor")
                print("2. Update Doctor details")
                print("3. Search by Doc_Id")
                print("4. Search by Name")
                print("5. Show all records")
                print("6. Clear a Doctor record")
                print("7. Search by OPD")
                print("8. Search Specialists")
                print("9. Search for Surgeon")
                print("10. Search for Physician")
                print("11. Exit to main menu")
                print("-----------------------------------------------------------------")
                try:
                    doctor_option = int(input("Enter your option:"))
                    if doctor_option == 11:
                        break
                    else:
                        print("Functionality not yet implemented. Please select option 11 to exit.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif user_option == 4:
             while True:
                print("-----------------------------------------------------------------")
                print("Pharmacy Menu")
                print("-----------------------------------------------------------------")
                print("1. Add new Bill record")
                print("2. Update Bill details")
                print("3. Search by Bill Number")
                print("4. Search by Patient ID")
                print("5. Show by Receipt Number")
                print("6. Show all records")
                print("7. Clear a record")
                print("8. Exit to main menu")
                print("-----------------------------------------------------------------")
                try:
                    pharmacy_option = int(input("Enter your option: "))
                    if pharmacy_option == 1:
                        add_pharmacy_bill()
                    elif pharmacy_option == 2:
                        update_pharmacy_bill()
                    elif pharmacy_option == 3:
                        search_by_bill_no()
                    elif pharmacy_option == 4:
                        search_pharmacy_by_pid()
                    elif pharmacy_option == 5:
                        search_pharmacy_by_receipt
                    elif pharmacy_option == 6:
                        all_pharmacy_records()
                    elif pharmacy_option == 7:
                        clear_pharmacy_record()
                    elif pharmacy_option == 8:
                        break
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif user_option == 5:
            while True:
                print("-----------------------------------------------------------------")
                print("Pathology Menu")
                print("-----------------------------------------------------------------")
                print("1. Add new Pathology record")
                print("2. Update Pathology details")
                print("3. Search by Lab ID")
                print("4. Search by Patient ID")
                print("5. Search by Receipt Number")
                print("6. Search by Test Name")
                print("7. Show all records")
                print("8. Clear a record")
                print("9. Exit to main menu")
                print("-----------------------------------------------------------------")
                try:
                    pathology_option = int(input("Enter your option: "))
                    if pathology_option == 1:
                        add_pathology_record()
                    elif pathology_option == 2:
                        update_pathology_record()
                    elif pathology_option == 3:
                        search_by_lab_id()
                    elif pathology_option == 4:
                        search_pathology_by_pid()
                    elif pathology_option == 5:
                        search_pathology_by_receipt()
                    elif pathology_option == 6:
                        search_by_test_name()
                    elif pathology_option == 7:
                        all_pathology_records()
                    elif pathology_option == 8:
                        clear_pathology_record()
                    elif pathology_option == 9:
                        break
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif user_option == 6:
            while True:
                print("-----------------------------------------------------------------")
                print("Billing Menu")
                print("-----------------------------------------------------------------")
                print("1. Add new Bill record")
                print("2. Update Bill details")
                print("3. Search by Receipt Number")
                print("4. Search by Patient ID")
                print("5. Show all records")
                print("6. Clear a record")
                print("7. Exit to main menu")
                print("-----------------------------------------------------------------")
                try:
                    billing_option = int(input("Enter your option: "))
                    if billing_option == 1:
                        add_billing_record()
                    elif billing_option == 2:
                        update_billing_record()()
                    elif billing_option == 3:
                        search_by_receipt_number()
                    elif billing_option == 4:
                        search_billing_by_pid()
                    elif billing_option == 5:
                        all_billing_records()
                    elif billing_option == 6:
                        clear_billing_record()
                    elif billing_option == 7:
                        break
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif user_option == 7:
            while True:
                print("-----------------------------------------------------------------")
                print("Tests Menu")
                print("-----------------------------------------------------------------")
                print("1. Add new Test record")
                print("2. Update Test details")
                print("3. Search by Test Number")
                print("4. Search by Patient ID")
                print("5. Show all records")
                print("6. Clear a record")
                print("7. Exit to main menu")
                print("-----------------------------------------------------------------")
                try:
                    test_option = int(input("Enter your option: "))
                    if test_option == 1:
                        add_test_record()
                    elif test_option == 2:
                        update_test_record()
                    elif test_option == 3:
                        search_by_test_no()
                    elif test_option == 4:
                        search_tests_by_pid()
                    elif test_option == 5:
                        all_test_records()
                    elif test_option == 6:
                        clear_test_record()
                    elif test_option == 7:
                        break
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif user_option == 8:
            while True:
                print("-----------------------------------------------------------------")
                print("OPD Menu")
                print("-----------------------------------------------------------------")
                print("1. Add new OPD record")
                print("2. Update OPD record")
                print("3. Search by Token Number")
                print("4. Search by Patient ID")
                print("5. Search by Doctor")
                print("6. Show all records")
                print("7. Clear a record")
                print("8. Clear all records")
                print("9. Exit to main menu")
                print("-----------------------------------------------------------------")
                try:
                    opd_option = int(input("Enter your option:"))
                    if opd_option == 1:
                        add_opd_record()
                    elif opd_option == 2:
                        update_opd_record()
                    elif opd_option == 3:
                        search_by_token_number()
                    elif opd_option == 4:
                        search_opd_by_pid()
                    elif opd_option == 5:
                        search_opd_by_doctor()
                    elif opd_option == 6:
                        all_opd_records()
                    elif opd_option == 7:
                        clear_opd_record()
                    elif opd_option == 8:
                        clear_all_opd_records()
                    elif opd_option == 9:
                        break
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif user_option == 9:
            while True:
                print("-----------------------------------------------------------------")
                print("Admission & Discharge Menu")
                print("-----------------------------------------------------------------")
                print("1. Add new Admission record")
                print("2. Update Admission/Discharge details")
                print("3. Search by Admission Number")
                print("4. Search by Patient ID")
                print("5. Search by Doctor")
                print("6. Show all records")
                print("7. Clear a record")
                print("8. Clear all records")
                print("9. Exit to main menu")
                print("-----------------------------------------------------------------")
                try:
                    ad_option = int(input("Enter your option:"))
                    if ad_option == 1:
                        add_admission_record()
                    elif ad_option == 2:
                        update_admission_record()
                    elif ad_option == 3:
                        search_by_admission_no()
                    elif ad_option == 4:
                        search_admissions_by_pid()
                    elif ad_option == 5:
                        search_admissions_by_doctor()
                    elif ad_option == 6:
                        all_admission_records()
                    elif ad_option == 7:
                        clear_admission_record()
                    elif ad_option == 8:
                        clear_all_admission_records()
                    elif ad_option == 9:
                        break
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        elif user_option == 10:
            while True:
                print("-----------------------------------------------------------------")
                print("Referral Menu")
                print("-----------------------------------------------------------------")
                print("1. Add new Referral record")
                print("2. Update Referral details")
                print("3. Search by Referral Number")
                print("4. Search by Patient ID")
                print("5. Search by Receipt Number")
                print("6. Show all records")
                print("7. Clear a record")
                print("8. Clear all records")
                print("9. Exit to main menu")
                print("-----------------------------------------------------------------")
                try:
                    referral_option = int(input("Enter your option:"))
                    if referral_option == 1:
                        add_referral_record()
                    elif referral_option == 2:
                        update_referral_record()
                    elif referral_option == 3:
                        search_by_referral_no()
                    elif referral_option == 4:
                        search_referrals_by_pid()
                    elif referral_option == 5:
                        search_referrals_by_receipt()
                    elif referral_option == 6:
                        all_referral_records()
                    elif referral_option == 7:
                        clear_referral_record()
                    elif referral_option == 8:
                        clear_all_referral_records()
                    elif referral_option == 9:
                        break
                    else:
                        print("Invalid option. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif user_option == 11:
            print("Exiting program. Goodbye!")
            mydb.close()
            break
        else:
            print("Invalid option. Please try again.")
print(main())