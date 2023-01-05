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
    print("Please enter tournament entry fee.")
    print("Data should be a whole number and not contain commas.")
    print("Example: 1000")
    entry_fee = input("Enter your latest tournament entry fee:\n")
    return (entry_fee)

print(get_entry_fee())