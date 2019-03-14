
import sys
import os


def welcome():
    clear_screen()
    print('''
    =========================================
    FLEETING HAPPY HOUR
    =========================================

    Version 3 by
    Transitional Intelligence Group

    >>> Welcome to your checkbook!
    ''')

def display_menu():
    print(''' 
    What would you like to do?

    1) View current balance
    2) Record a debit (withdraw)
    3) Record a credit (deposit)
    4) View last 5 transactions
    5) Exit
    ''')

    user_input = input('Enter choice: ')
    
    if user_input == '1':
        view_balance()
    elif user_input =='2':
        withdraw()
    elif user_input == '3':
        deposit()
    elif user_input == '4':
        view_history()
    elif user_input == '5':
        exit_program()
    else:
        clear_screen()
        print('ERROR. Invalid input; try again.')
        print()
        display_menu()


def view_balance():
    clear_screen()

    clean_credits = 0
    clean_debits = 0

    with open('project_data.txt') as f:
        transactions = f.read().split('\n')
        for item in transactions:
            if item.startswith('+'):
                clean_credits += float(item.strip('+'))
            elif item.startswith('-'):
                clean_debits += float(item.strip('-'))

    current_balance = clean_credits - clean_debits

    formatted_balance = '${:,.2f}'.format(current_balance)
    print('>>> Your current balance is:', formatted_balance)
    print()
    display_menu()


def withdraw():
    clear_screen()
    try:
        withdraw_amount = input('>>> How much would you like to withdraw? ')
    except:
        print()
        print('What you entered was not a valid number. Try again.')
        print()
        display_menu()
    try:
        withdrawal = float(withdraw_amount.strip('$').replace(',', ''))
    except:
        print()
        print('What you entered was not a valid number. Try again.')
        print()
        display_menu()
    with open('project_data.txt', 'a+') as f:
        f.write('-'+str(withdrawal)+'\n')
    print()
    print('Transaction recorded.')
    display_menu()


def deposit():
    clear_screen()
    try:
        deposit_amount = input('>>> How much would you like to deposit? ')
    except:
        print()
        print('What you entered was not a valid number. Try again.')
        print()
        display_menu()
    try:
        deposit = float(deposit_amount.strip('$').replace(',', ''))
    except:
        print()
        print('What you entered was not a valid number. Try again.')
        print()
        display_menu()
    with open('project_data.txt', 'a+') as f:
        f.write('+'+str(deposit)+'\n')
    print()
    print('Transaction recorded.')
    display_menu()


def view_history():
    clear_screen()
    with open('project_data.txt') as f:
        transactions = f.read().split('\n')
        print()
        for i in range(1,6):
            print(f'#{i} \t ' + transactions[-(i+1)])
    print()
    display_menu()


def exit_program():
    clear_screen()
    print('>>> Exiting. Thank you, goodbye!')
    print()
    print('Programmers: K. Salts & E.C. De Dios \n')
    sys.exit()


def clear_screen():
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X


welcome()
display_menu()