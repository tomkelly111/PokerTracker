import gspread
import pyfiglet
import sys
import time
from google.oauth2.service_account import Credentials
"""
Below colorama import and code used elsewhere in
programme was taken from tutorial by Tech With Time
available here: https://www.youtube.com/watch?v=u51Zjlnui4Y
"""
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
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
    """
    Offers the user options of what they can do.
    A while loop is ran so that once a selected option is
    complete the user is returned these options again until
    the user exits the programme.
    """
    while True:
        answer = input("""
What would you like to do? Type:
'1' to add details of a tournament you played,
'2' to view your current winrate or
'x' to exit. \n""")
        if answer == "1":
            tournament_updates()
        elif answer == "2":
            print_slow("Calculating winrate...")
            winrate_update()
        elif answer == "x" or answer == "X":
            exit_system()
        else:
            print_slow(f"Answer not clear, you typed '{answer}'...")


def exit_system():
    print_slow("Thanks for using PokerTracker...\n")
    goodbye = pyfiglet.figlet_format("GOODBYE", font="slant")
    print(Fore.CYAN + Style.BRIGHT + goodbye)
    raise SystemExit


def retrieve_user_data(prompt, request, example):
    """
    Takes input from user. Input must be a whole
    number not containing any commas. A while loop runs until
    data entered is valid and then it is added to an empty list
    so data can be stored in googledocs.
    """
    while True:
        print_slow(f"\n{prompt}")
        (print_slow
         ("\nData should be a whole number and not contain any commas."))
        print_slow(f"\nExample: {example} \n")
        user_data = input(f"{request}:\n")
        if validate_entry(user_data):
            print_slow("\nThank you!")
            break
        else:
            continue
    entered_data = []
    entered_data.append(user_data)
    return (entered_data)


def validate_entry(value):
    """
    Validates data entered by user.
    Checks entry can be convereted from a string to an int and returns
    True and if not returns an False and an error message.
    """
    if value == "x" or value == "X":
        exit_system()
    try:
        int(value)
        return True
    except ValueError as e:
        print_slow(f"Your entry is not in the right format,\
you entered'{value}', \nlet's try again! \n")
        return False


def update_database(the_dict):
    """
    Takes user input and adds it to the relevant workheet in the the googledoc.
    Code for this function has been copied from the Love Sandwhiches
    walkthrough project.
    """
    print_slow("\nUpdating database...\n")
    print_slow("\n......\n")
    for key, value in the_dict.items():
        data = value
        worksheet = key
        worksheet_to_update = SHEET.worksheet(worksheet)
        worksheet_to_update.append_row(data)
    print_slow("\n..........\n")
    print_slow("\nDatabase updated successfully!\n")


def winnings_check():
    """
    Asks user whether they won anything in the tournament. If yes
    the retrieve data function runs to collect the prize data and
    entry is returned. If no prize was won a value of 0 is returned.
    A while loop runs until a valid answer is provided and if not
    an error message is displayed.
    """
    while True:
        answer = input("""
\nDid you win anything in this tournament?
Please answer with 'y'(yes) or 'n'(no) \n
""")
        if answer == "y":
            congrats = pyfiglet.figlet_format("CONGRATS!", font="slant")
            print(Fore.RED + Style.BRIGHT + congrats)
            winnings = (retrieve_user_data(
                "Please enter how much you won", "Winnings €", 3000))
            return winnings
        elif answer == "n":
            sorry = pyfiglet.figlet_format("Unlucky", font="slant")
            print(Fore.RED + Style.BRIGHT + sorry)
            print_slow("\nBetter luck next time!")
            return ["0"]
        elif answer == "x" or answer == "X":
            exit_system()
        else:
            (print_slow
             (f"\nAnswer not clear, you typed '{answer}'\
            \nplease type 'y' or 'n'\n"))


def calculate_totals(*worksheet_names):
    """
    Retrieves data from worksheet iterates through adding it to a vaiable.
    Does this for three worksheets and returns three variables -
    losses, hours and winnings.
    """
    answer = []
    for item in worksheet_names:
        lists = SHEET.worksheet(item).get_all_values()
        i = 0
        for list in lists:
            for item in list:
                item = int(item)
                i += item
        answer.append(i)
    for item in answer:
        return answer
        

    # lists = SHEET.worksheet(hours_played).get_all_values()
    # j = 0
    # for list in lists:
    #     for item in list:
    #         item = int(item)
    #         j += item
    # hours = j

    # lists = SHEET.worksheet(winnings).get_all_values()
    # k = 0
    # for list in lists:
    #     for item in list:
    #         item = int(item)
    #         k += item
    # winnings = k
    # return losses, hours, winnings


def calculate_winrate(losses, hours_played, winnings):
    """
    Takes three variables (losses, hours and winnings) and
    performs calculations to return
    profit, return on investment and hourly winrate.
    profit is calculated by subtracting losses from winnings.
    return on investment is calculated by dividing profit by costs
    and multiplying by 100.
    Hourly winrate is calculated by dividing profit by hours.
    """
    profit = winnings - losses
    return_on_investment = round((((profit) / losses) * 100), 2)
    hourly_rate = round((profit / hours_played), 2)
    print(Fore.CYAN + f"""
    ------------------  WINRATE  ------------------
    Your profit to date is: €{profit}
    Your return on investment is: {return_on_investment}%
    Your winrate is €{hourly_rate} per hour played.
    -----------------------------------------------
    """)


def tournament_updates():
    """
    Runs the functions required to gather tournament details from
    the user and update the database.
    Gathers tournament entry fee by running retrieve_user_data function,
    this is then passed to the update_database function.
    Winning_check is then ran to see if a prize was won, the value returned
    is then passed to the_update database function.
    Tetrieve_data function is then ran a final time to retrieve hours played,
    this is then also added to the database.
    """
    entry_fee = (retrieve_user_data("Please \
enter tournament entry fee.", "Entry Fee €", 120))
    winnings = winnings_check()
    hours_played = (retrieve_user_data("How many hours did you play in this \
tournament?", "Hours Played", 6))
    (update_database({"entry_fees": entry_fee, "winnings": winnings,
     "hours_played": hours_played}))


def winrate_update():
    """
    Obtains losses, hours and winnings from calculate_totals
    function and then passes these to calculate_winrate function.
    """
    losses, hours, winnings = (
        calculate_totals("entry_fees", "hours_played", "winnings"))
    calculate_winrate(losses, hours, winnings)


def main():
    """
    Prints a welcome messeage and runs user-options function.
    Code for logo is taken from:
    https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
    """
    logo = pyfiglet.figlet_format(f"     Poker", font="slant")
    print(Fore.RED + Style.BRIGHT + logo)
    logo2 = pyfiglet.figlet_format(f"   Tracker", font="slant")
    print(Fore.RED + Style.BRIGHT + logo2)
    print(Fore.CYAN + "-------The Pro's Favourite \
Poker Tracking Software-------")
    print_slow("Welcome to PokerTracker...\n\
Here you can add details of any tournaments you have played\n\
and check your current winrate!\n")
    user_options()


def print_slow(str):
    """"
    Function to make all text printed to CLI be typed out slowly.
    Function was taken from
    https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
    and provided by user Sebastian
    """
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)


main()
