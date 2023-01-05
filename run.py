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

def get_entry_fee(prompt):
    while True:
        print(prompt)
        print("Data should be a whole number and not contain commas.")
        print(f"Example: 1000 \n")
        user_entry_fee = input(f"Entry fee:\n")
        if validate_entry(user_entry_fee):
            print("Thank you!")
            break
        else:
            continue
    entry_fee = []
    entry_fee.append(user_entry_fee)    
    return (entry_fee)

def validate_entry(value):
    try:
        int(value)
        return True
    except ValueError as e:
        print(f"Sorry invalid entry:{e}, let's try again! \n")
        return False

def update_database(data, worksheet):
    #from love sandwhiches
    print(f"Updating database...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"Database updated successfully\n")


def winnings_check():
    while True:
        answer = input(f"Did you win anything in this tournament? Please answer with 'y'(yes) or 'n'(no) \n")
        if answer == "y":
            print(f"Congratulations \n")
            winnings = get_entry_fee(f"Please enter how much you won \n")
            return winnings
        elif answer == "n":
            print("updating database")
            return ["0"]
        else:
            print(f"Answer not clear, you typed '{answer}' please type 'y' or 'n'")

def main():
    entry_fee = get_entry_fee(f"Please enter tournament entry fee \n")
    update_database(entry_fee, "entry_fees")
    winnings = winnings_check()
    update_database(winnings, "winnings")
    hours_played = get_entry_fee("How many hours did you play in this tournament?")
    update_database(hours_played, "hours_played")

main()