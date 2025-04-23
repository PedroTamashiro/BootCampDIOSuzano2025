import methods
import datetime

def menu():
    return input("""

[1] Deposit
[2] Withdraw
[3] Extract
[4] Create Person
[5] Create Account
[6] Chance Account
[7] Login
[8] Logout
[9] Exit

=> """)

# ========== LISTA GLOBAL DE CONTAS E CLIENTES ==========
clients = []
accounts = []
current_client = None
current_account = -1

# ===================== LOOP PRINCIPAL =====================
def find_client_by_cpf(cpf: int):
    for client in clients:
        if isinstance(client, methods.FisicPerson) and client._cpf == cpf:
            return client
    return None

def create_client():
    print('Create User...')
    client = methods.FisicPerson()
    clients.append(client)
    print(f"User {client._name} created successfully.")

def create_account():
    global current_client, current_account
    if not current_client:
        print('You must be logged in to create an account')
        return
    
    account = methods.Account(accounts, current_client)
    current_client.add_account(account)
    accounts.append(account)
    current_account += 1
    print('Account created successfully')

def login():
    global current_client
    cpf = input("Enter your CPF to login: ").replace(".", "").replace("-", "")
    client = find_client_by_cpf(cpf)
    if client:
        current_client = client
        print(f"Welcome, {client._name}!")
    else:
        print("CPF not found. Please create an user first.")

def logout():
    global current_client
    if current_client:
        print(f"Goodbye, {current_client._name}")
    current_client = None

def get_user_account():
    if not current_client or not current_client._accounts:
        print("No user or account found.")
        return None
    return current_client._accounts[current_account]

def deposit():
    acc = get_user_account()
    if acc:
        dep = methods.Deposit()
        current_client.realize_transaction(acc, dep)

def withdraw():
    acc = get_user_account()
    if acc:
        loot = methods.Withdraw()
        current_client.realize_transaction(acc, loot)

def extract():
    acc = get_user_account()
    if acc:
        acc._historic.show_historic()
        acc.balance()

def change_account():
    global current_account
    acc = get_user_account()
    if acc:
        for index, account in enumerate(accounts):
            balance = account.balance()
            print(f'[{index}] - {balance}')
        current_account = int(input('Choice an account: '))

while True:
    option = menu()

    if option == "1":
        deposit()
    elif option == "2":
        withdraw()
    elif option == "3":
        extract()
    elif option == "4":
        create_client()
    elif option == "5":
        create_account()
    elif option == "6":
        change_account()
    elif option == "7":
        login()
    elif option == "8":
        logout()
    elif option == "9":
        print("Exiting... Bye!")
        break
    else:
        print("Invalid option, try again.")