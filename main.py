
from banking_functions import random_with_N_digits, create, account, staff

from authentication_functions import welcome, login, exit

# Main entry point of the program
if __name__ == "__main__":
    welcome()

random_with_N_digits()
create()
account()
staff()
login()
exit()
