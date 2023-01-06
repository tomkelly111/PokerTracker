import gspread
import sys,time
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


def user_options():
    print_slow(f"""
Welcome to PokerTracker... 
Here you can add details of any tournaments you have played 
and check your current winrate!\n
    """)
    while True:
        answer = input(f"""
What would you like to do? Type:
'1' to add tournament details,
'2' to view your current winrate or
'x' to exit. \n""")
        if answer == "1":
            tournament_updates()
        elif answer == "2":
            print_slow("Calculating winrate...")
            winrate_update()
        elif answer == "x":
            print_slow("Thanks for using PokerTracker... Goodbye!")
            raise SystemExit
        else:
            print_slow(f"Answer not clear, you typed '{answer}'...")


def retrieve_user_data(prompt, request):
    while True:
        print_slow(prompt)
        print_slow(f"\nData should be a whole number and not contain any commas.")
        print_slow(f"\nExample: 1000 \n")
        user_data = input(f"{request}:\n")
        if validate_entry(user_data):
            print_slow("Thank you!")
            break
        else:
            continue
    entered_data = []
    entered_data.append(user_data)
    return (entered_data)


def validate_entry(value):
    try:
        int(value)
        return True
    except ValueError as e:
        print_slow(f"Your entry is not in the right format, you entered'{value}',\
            \nlet's try again! \n")
        return False


def update_database(data, worksheet):
    # from love sandwhiches
    print_slow(f"\nUpdating database...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print_slow(f"\nDatabase updated successfully!\n")


def winnings_check():
    while True:
        answer = input(f"""
Did you win anything in this tournament?
Please answer with 'y'(yes) or 'n'(no) \n
""")
        if answer == "y":
            print_slow(f"\nCongratulations!!! \n")
            winnings = (retrieve_user_data(
                "Please enter how much you won", "Winnings €"))
            return winnings
        elif answer == "n":
            print_slow(f"\nBetter luck next time!")
            return ["0"]
        else:
            (print_slow
             (f"\nAnswer not clear, you typed '{answer}'\
            \nplease type 'y' or 'n'\n"))


def calculate_totals(worksheet1, worksheet2, worksheet3):
    lists = SHEET.worksheet(worksheet1).get_all_values()
    i = 0
    for list in lists:
        for item in list:
            item = int(item)
            i += item
    losses = i

    lists = SHEET.worksheet(worksheet2).get_all_values()
    j = 0
    for list in lists:
        for item in list:
            item = int(item)
            j += item
    hours = j

    lists = SHEET.worksheet(worksheet3).get_all_values()
    k = 0
    for list in lists:
        for item in list:
            item = int(item)
            k += item
    winnings = k
    return losses, hours, winnings


def calculate_winrate(data1, data2, data3):
    profit = data3 - data1
    return_on_investment = round((((data3 - data1) / data1) * 100), 2)
    hourly_rate = round((profit / data2), 2)
    print_slow(f"""
    Your profit to date is: €{profit}
    Your return on investment is: {return_on_investment}%
    Your winrate is €{hourly_rate} per hour played.
    """)


def tournament_updates():
    entry_fee = (retrieve_user_data("Please\
    enter tournament entry fee.", "Entry Fee €"))
    update_database(entry_fee, "entry_fees")
    winnings = winnings_check()
    update_database(winnings, "winnings")
    hours_played = (retrieve_user_data("How many hours did you play in this \
     tournament?", "Hours Played"))
    update_database(hours_played, "hours_played")


def winrate_update():
    losses, hours, winnings = (
        calculate_totals("entry_fees", "hours_played", "winnings"))
    calculate_winrate(losses, hours, winnings)


def main():
    user_options()

def print_slow(str):
    # Function to make all text printed to CLI be typed out.
    # Function was taken from 
    # https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
    # and provided by user Sebastian
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


main()
