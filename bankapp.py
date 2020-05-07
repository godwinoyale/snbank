import random
import os
from datetime import datetime


def staff_choices():
    option1 = input("Please select one option to perform operation\n\t1 Staff Login\n\t2 Close App\n\t>>> ")
    if option1 == "1":
        username = input("Username: ")
        password = input("Password: ")

        def user_details(username, password, lines):
            for line in lines:
                if username in line and password in line:
                    session = open("session.txt", "x")
                    dateTimeObj = str(datetime.now())
                    session.write(dateTimeObj)
                    session.close()

                    def staff_login():
                        user_login = input("Please select an option by typing a number from the list\n\t1 "
                                           "Create New Bank Account\n\t2 Check Account Details\n\t3 Log Out\n\t>>>")
                        if user_login == "1":
                            cust_name = input("Enter the account name:  ")

                            def opening_balance():
                                global open_balance
                                open_balance = input("Enter your opening balance: ")

                                if open_balance.isdigit():
                                    open_balance = open_balance
                                else:
                                    print("opening balance must be numbers\n")
                                    opening_balance()
                            opening_balance()
                            type_account = input("Enter Account Type: ")
                            email_account = input("Enter Account Email: ")
                            global acctnumb
                            acctnumb = random.randrange(1000000000, 10000000000)

                            customer = open("customer.txt", "w")
                            customer.write("Account Name: %s \nOpening Balance: %s \nAccount Type: %s \nAccount Email: "
                                           "%s \nAccount Number: %d\n" % (cust_name, open_balance, type_account, email_account, acctnumb))
                            customer.close()
                            print(f"Your account number is: {acctnumb}\n")
                            staff_login()

                        elif user_login == "2":
                            def login_login():
                                check_acct_details = input("Enter Your Account Number: ")
                                if check_acct_details == str(acctnumb):
                                    customer = open("customer.txt", "r")
                                    staff_cust_details = customer.read()
                                    print(staff_cust_details)
                                    customer.close()
                                    staff_login()
                                else:
                                    print("Wrong Account Number supplied, try again! \n")
                                    login_login()

                            login_login()
                        elif user_login == "3":
                            os.remove("session.txt")
                            staff_choices()

                    staff_login()

                else:
                    print("Username or Password Incorrect.\n")
                    staff_choices()

        user_details(username, password, open('staff.txt').readlines())
    elif option1 == "2":
        exit(0)
    else:
        print("Please select an option from the given options")
        staff_choices()


staff_choices()







