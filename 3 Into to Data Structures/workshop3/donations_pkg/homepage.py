import re

def show_homepage():
    print("\n       === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.   Login       | 2.   Register        |")
    print("------------------------------------------")
    print("| 3.   Donate      | 4.   Show Donations  |")
    print("------------------------------------------")
    print("| 5.   Exit        | 6.   Log Out         |")
    print("------------------------------------------")


def donate(username):
    while True:
        donation_amount = input("How much would you like to donate?: $ ")
    
        if re.match(r'\d+(?:[.]\d{2})?$', donation_amount):
            donation_amount = float(donation_amount)
            if donation_amount > 0:
                print(f"\nThank you {username} for donating: $ {donation_amount:.2f}")
                break
            elif donation_amount == 0:
                break
            else:
                print("You did not enter a valid amount.")
        else:
            print("You did not enter a valid amount.")    
    
    donation_list = [username, donation_amount]
    return donation_list


def show_donations(donations, username):
    if username == "admin":
        print("  ---  All Donations  ---  ")
        if len(donations) == 0:
            print("  Currently, there are no donations.\n")
        else:
            total_users = 0
            total_donation_amt = 0
            for donation in donations:
                print(f"  {donation[0]} donated: $ {donation[1]:.2f}")
                total_donation_amt += donation[1]
                total_users += 1

            print()
            print(f"  Total = $ {total_donation_amt:.2f}")
            
            average_donated = total_donation_amt / total_users
            print(f"  Avg.  = $ {average_donated:.2f}")
        print("  -----------------------  ")

    else:
        print("Sorry, you are not admin. You cannot see the donations.")
        # print("You don't have access to view the donations.")