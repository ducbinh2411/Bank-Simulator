import json
from datetime import datetime
from banking_functions import staff
def login():
    print(f"Enter Details.")
    username = input("Please enter your username: ")
    password = input(f'Please enter your password: ')
    with open('staff.txt') as json_file:
        data = json.load(json_file)
        while (username != (data['Staff 1']['Username']) or password != (data['Staff 1']['Password'])) and (
                username != (data['Staff 2']['Username']) or password != (data['Staff 2']['Password'])):
            print('Username or password not found!!!')
            login()
        else:
            print(f'Welcome {username}')
            login = datetime.now()
            login = login.strftime("%d:%m:%Y %H:%M:%S")
            session_data = {
                'Present User': username,
                'Login Time': login,
            }
            with open('user_session.txt', 'w') as file_object:
                json.dump(session_data, file_object)
            staff()

#function to exit
def exit():
    file = open('customer.txt', 'r+')
    file.truncate()
    file.close()
    print("Thank you for using our banking system!")


def welcome():
    print("=====================================")
    print("     ----Welcome to Bank of America----       ")
    print("*************************************")
    print("=<< 1. Staff Login                >>=")
    print("=<< 2. Close App                  >>=")
    print("*************************************")
    choice = input(f'Select your choice number from the above menu :')
    if choice == "1":
        login()
    elif choice == "2":
        exit()
    else:
        print('Wrong input')
        welcome()
