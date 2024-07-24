# M.Awais ATM Machine (Allied Bank) Source Code
import time
print("Welcome to the Allied Bank")
time.sleep(3)
print("Set the password that you use for the card\n")
password = int(input("Set the 4-digits Password = "))
print("\n")
print("Your password is set, you can use your card\n")
Balance = 2000
print("\n")
print("When user went to the ATM Machine\n")

count = 5
while count > 0:
    pin = int(input("Please enter the pin = "))
    print("\n")
    if pin == password:
        while True:
            print("""Welcome to Allied
                1 == Balance Inquiry
                2 == Withdrwal Amount
                3 == Deposit Amount
                4 == Exit
                """)
            try:
                option = int(input("Enter your Choice = "))
            except:
                print("Please choose the given option")

            if option == 1:
                time.sleep(2)
                print(f"your current Balance is = {Balance}\n")
            if option==2:
                    time.sleep(2)
                    print("""Select the Amount you want to withdraw
                        1 == 1000 \t\t\t\t\t 2 == 2000
                        3 == 3000 \t\t\t\t\t 4 == 4000
                        5 == 5000  \t\t\t\t\t 6 == OtherAmount""")
                    try:
                        sel=int(input("Select the amount you want to withdraw = "))
                    except:
                        print("Please choose the given option")
                    if sel == 1:
                        time.sleep(2)
                        if 1000 > Balance:
                            print("you have insufficent Balance\n")
                        else:
                            Balance = Balance - 1000
                            print("1000 is detucted from your credit card\n")
                            print(f"your new balance is {Balance}")
                    if sel == 2:
                        time.sleep(2)
                        if 2000 > Balance:
                            print("you have insufficent Balance\n")
                        else:
                            Balance = Balance - 2000
                            print("2000 is detucted from your credit card\n")
                            print(f"your new balance is {Balance}")
                    if sel == 3:
                        time.sleep(2)
                        if 3000 > Balance:
                            print("you have insufficent Balance\n")
                        else:
                            Balance = Balance - 3000
                            print("3000 is detucted from your credit card\n")
                            print(f"your new balance is {Balance}")     
                    if sel == 4:
                        time.sleep(2)
                        if 4000 > Balance:
                            print("you have insufficent Balance\n")
                        else:
                            Balance = Balance - 4000
                            print("4000 is detucted from your credit card\n")
                            print(f"your new balance is {Balance}")
                    if sel == 5:
                        time.sleep(2)
                        if 5000 > Balance:
                            print("you have insufficent Balance\n")
                        else:
                            Balance = Balance - 5000
                            print("5000 is detucted from your credit card\n")
                            print(f"your new balance is {Balance}")
                    if sel == 6:
                        time.sleep(2)
                        withdraw = int(input("Enter the amount that you want to withdraw = "))
                        print("\n") 
                        if withdraw > Balance:
                            print("you have insufficent Balance\n")
                        else:
                            Balance = Balance - 1000
                            print(f"{withdraw} is detucted from your credit card\n")
                            print(f"your new balance is {Balance}")    
            if option==3:
                    time.sleep(2)
                    print("""Select the Amount you want to Deposit
                        1 == 1000 \t\t\t\t\t 2 == 2000
                        3 == 3000 \t\t\t\t\t 4 == 4000
                        5 == 5000  \t\t\t\t\t 5 == OtherAmount""")
                    try:
                        dal=int(input("Select the amount you want to Deposit = "))
                    except:
                        print("Please choose the given option")
                    if dal == 1:
                        time.sleep(2)
                        Balance = Balance + 1000
                        print("1000 is added in your account\n")
                        print(f"your new balance is {Balance}")
                    if dal == 2:
                        time.sleep(2)
                        Balance = Balance + 2000
                        print("2000 is added in your account\n")
                        print(f"your new balance is {Balance}")
                    if dal == 3:
                        time.sleep(2)
                        Balance = Balance + 3000
                        print("3000 is added in your account\n")
                        print(f"your new balance is {Balance}")     
                    if dal == 4:
                        time.sleep(2)
                        Balance = Balance + 4000
                        print("4000 is added in your account\n")
                        print(f"your new balance is {Balance}")
                    if dal == 5:
                        time.sleep(2)
                        Balance = Balance + 5000
                        print("5000 is added in your account\n")
                        print(f"your new balance is {Balance}")
                    if dal == 6:
                        time.sleep(2)     
                        Add = int(input("Enter the amount that you want to withdraw = "))
                        Balance = Balance + Add
                        print(f"{withdraw} is detucted from your credit card\n")
                        print(f"your new balance is {Balance}")
            if option == 4:
                time.sleep(2)
                print("Thanks for Using Allied Bank")
                break
        break
    else:
        count -= 1
        print("Wrong Pin! Please Try Again\n")
        print(f"You have {count} tries left\n")

if count == 0:
    print("Your card has been blocked\n")
    print("Contact to the help desk for unblocking your Card")
