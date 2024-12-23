# File Name: app.py  7/16/22
# About: Donation app that allows a user to make adonation

from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register
import re

stop = "Stop"

database = {
    "admin": "password123"
}
donations = []
authorized_user = ""

#print(f"{'$7.00':10}"
#      f"{'$10.00':10}")

print("""
  ___                _   _             
 |   \ ___ _ _  __ _| |_(_)___ _ _  ___
 | |) / _ \ ' \/ _` |  _| / _ \ ' \(_-<
 |___/\___/_||_\__,_|\__|_\___/_||_/__/\n""")



while True:
    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}")

    choice = input("Choose an option between 1-6: ")

    print()

    if choice == "1":
        if authorized_user == "":
            username = input("Username: ").lower()  # lowercase username
            password = input("Password: ")          # case sensitive password
            authorized_user = login(database, username, password)
        else:
            print(f"You are already logged in as {authorized_user}...")
        print()
        
        """
        if authorized_user == "":
            while True:
                username = input("Email/username: ")

                regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

                if re.fullmatch(regex, username) or username == 'admin':
                    password = input("Password: ")
                    authorized_user = login(database, username, password)
                    break
                else:
                    print(f"Invalid Email: {username}")
        else:
            print("You are already logged in...")"""
            
    elif choice == "2":
        if authorized_user == "":
            username = input("Username: ").lower()
            password = input("Password: ")
            authorized_user = register(database, username)
            if authorized_user != "":
                database[authorized_user] = password
                print(f"User {authorized_user} registerd.")
        else:
            print(f"You are currently logged in. Please log out to register a new account.")

        """
        if authorized_user == "":
            username = input("Enter Email: ")
            regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

            if re.fullmatch(regex, username):
                    password = input("Password: ")
                    authorized_user = register(database, username)
                    if authorized_user != "":
                        database[authorized_user] = password
            else:
                print("Invalid Email! Please try again.")
        else:
            print(f"You are currently logged in. Please log out to register a new account.")"""


    elif choice == "3":
        if authorized_user == "":
            print("You are not logged in...")
        else:
            donation_list = donate(authorized_user)
            donations.append(donation_list)

    elif choice == "4":
        show_donations(donations, authorized_user)
    
    elif choice == "5":
        exit_choice = input("Are you sure you want to exit? (Y?N): ")
        if exit_choice[0].lower() == "y":
            print("Thank you and have a nice day\n")
            exit()
        else:
            continue

    elif choice == "6":
        if authorized_user != "":
            logout_choice = input("Are you sure you want to log out? (Y?N) ")
            if logout_choice[0].lower() == "y":
                print(f"Goodbye {authorized_user}")
                authorized_user = ""
                username = ""
                password = ""
                donation_list = []                
            else:
                continue
        else:
            print("You're currently logged out.")

