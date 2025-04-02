from methods import User, Account
import datetime

menu = """

[1] Deposit
[2] Loot
[3] extract
[4] Create User
[5] Create Account
[6] Logout
[7] Exit

=>"""

LOOT_LIMIT = 500
MAX_LOOT_NUMBER = 3
users = []
Accounts = []
selected = None

while True:
    if users == []:
        print('\nAny user in located, please create at least one')
        login = User(len(Accounts) + 1)
        users.append(login)
        Accounts.append(login.Accounts[-1])

    if selected == None:
        print('Please select one user:')
        for n in range(len(users)):
            print(f'[{n}] {users[n].name}')
        while selected == None:
            try:
                number = input()
                selected = users[int(number)]
            except:
                print('please input one digit')
                
    option = input(menu)

    if option == '1':
        if selected.transactionNumber < 10:
            balance, extract = selected.deposit()
            print(f'Atual balance: {balance}')
        else:
            print('You reached the limit of day')

    elif option == '2':
        if selected.transactionNumber < 10:
            balance, extract = selected.loot(LOOT_LIMIT, MAX_LOOT_NUMBER)
            print(f'Atual balance: {balance}')
        else:
            print('You reached the limit of day')

    elif option == '3':
        selected.lookExtract()

    elif option == '4':
        problem = True
        while problem == True:
            problem = False
            login = User(len(Accounts) + 1)
            for n in range(len(users)):
                if users[n].cpf == login.cpf:
                    problem = True
                    print('CPF already registered')
                    break
            
        users.append(login)

    elif option == '5':
        login = Account(len(Accounts) + 1, selected)
        Accounts.append(Account)

    elif option == '6':
        selected = None
        
    elif option == '7':
        break

    else:
        print('Invalid Operation')