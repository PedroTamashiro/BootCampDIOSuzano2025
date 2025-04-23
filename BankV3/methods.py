from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import pytz
import re
from abc import ABC, abstractmethod

REGEX_ADRESS = '^[A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ\s]+-\s\d+\s-\s\d{5}-\d{3}\s-\s[A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ\s]+\/[A-Za-z]{2}$'

# ======================== ABSTRACT TRANSACTION ============================
class Transaction(ABC):
    @abstractmethod
    def register(self, account):
        pass

    @abstractmethod
    def verify_number(self):
        pass

# ======================== HISTORIC ============================
class Historic:
    def __init__(self):
        self._register = []

    def add_transaction(self, transaction):
        timestamp = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
        self._register.append(f'{transaction.__class__.__name__} -> {timestamp} - R$ {transaction._value:.2f}')

    def show_historic(self):
        print('REGISTER:')
        for reg in self._register:
            print(reg)

# ======================== ACCOUNT ============================
class Account:
    def __init__(self, accounts_list, client=None):
        self._balance = 0
        self._agency = '0001'
        self._number = self.verify_agency_number(accounts_list)
        self._client = client
        self._historic = Historic()
        
    def verify_agency_number(self, accounts_list):
        return len(accounts_list) + 1
    
    def balance(self):
        return f'Balance: R$ {self._balance:.2f}'

    def new_account(self, account_list):
        if not self._client:
            print('Account without Client')
        else:
            new_account = Account(account_list, self._client)
            return new_account
        
    def loot(self, value):
        self._balance -= value

    def deposit(self, value):
        self._balance += value

# ======================== DEPOSIT ============================
class Deposit(Transaction):
    def __init__(self):
        self._value = self.verify_number()

    def verify_number(self):
        try:
            value = float(input('Send value to deposit: '))
            if value <= 0:
                raise ValueError
            return value
        except:
            print('Invalid value')
            return self.verify_number()

    def register(self, account):
        account._historic.add_transaction(self)
        account.deposit(self._value)
        print('Deposit successful')

# ======================== WITHDRAW ============================
class Withdraw(Transaction):
    def __init__(self):
        self._value = self.verify_number()

    def verify_number(self):
        try:
            value = float(input('Send value to withdraw: '))
            if value <= 0:
                raise ValueError
            return value
        except:
            print('Invalid value')
            return self.verify_number()

    def register(self, account):
        if account._balance >= self._value:
            account._historic.add_transaction(self)
            account.loot(self._value)
            print('Withdraw successful')
        else:
            print("You don't have sufficient balance.")

# ======================== CLIENT ============================
class Client:
    def __init__(self):
        self._address = self.get_address()
        self._accounts = []

    def get_address(self):
        while True:
            address = input('Input your address (address - number - CEP - City/UF): ')
            if re.match(REGEX_ADRESS, address):
                return address
            print("Invalid format. Example: Rua das Flores - 123 - 12345-678 - São Paulo/SP")

    def realize_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self._accounts.append(account)

# ======================== CURRENT ACCOUNT ============================
class CurrentAccount(Account):
    def __init__(self, accounts_list, client):
        super().__init__(accounts_list, client)
        self._limit = 500
        self._loot_limit = 3

# ======================== FISIC PERSON ============================
class FisicPerson(Client):
    def __init__(self):
        super().__init__()
        self._cpf = self.get_cpf()
        self._name = self.get_name()
        self._born_date = self.get_born_date()

    def get_name(self):
        while True:
            name = input('Enter your full name: ')
            if all(x.isalpha() or x.isspace() for x in name) and name.strip():
                return name
            print("Invalid name. Use only letters and spaces.")

    def get_born_date(self):
        while True:
            date_str = input('Enter birth date (dd/mm/yyyy): ')
            try:
                date = datetime.strptime(date_str, "%d/%m/%Y")
                if date > datetime.now():
                    print("Date cannot be in the future.")
                else:
                    return date_str
            except ValueError:
                print("Invalid format. Use dd/mm/yyyy.")

    def get_cpf(self):
        while True:
            cpf = input('Enter CPF (only numbers): ').replace('.', '').replace('-', '')
            if cpf.isdigit() and len(cpf) == 11:
                return cpf
            print("Invalid CPF. It must have 11 digits.")