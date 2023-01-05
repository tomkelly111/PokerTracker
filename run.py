import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("pokertracker")

def get_entry_fee():
    while True:
        print("Please enter tournament entry fee.")
        print("Data should be a whole number and not contain commas.")
        print("Example: 1000")
        entry_fee = input("Enter your latest tournament entry fee:\n")
        if validate_entry(entry_fee):
            print("Thank you!")
            break
        else:
            continue
    return (entry_fee)

def validate_entry(value):
    try:
        int(value)
        return True
    except ValueError as e:
        print(f"Sorry invalid entry:{e}, let's try again! \n")
        return False



print(get_entry_fee())