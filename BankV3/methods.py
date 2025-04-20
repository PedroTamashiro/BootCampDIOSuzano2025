from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import pytz
import re
from abc import ABC, abstractmethod

REGEX_ADRESS = '^[A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ\s]+-\s\d+\s-\s\d{5}-\d{3}\s-\s[A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ\s]+\/[A-Za-z]{2}$'

class Transaction(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def register(Account):
        pass
    
    @abstractmethod
    def verifyNumber():
        pass

class Historic:
    def __init__(self):
        self._register = []
    
    def add_transaction(self, transaction: Transaction):
        today = datetime.today()
        today = today.strftime('%d/%m/%Y - %H:%M:%S')
        self._register.append(f'{transaction.__class__} -> {today} - {transaction}')

    def show_historic(self):
        print('REGISTER:')
        for n in range(len(self._register)):
            print(self._register[n])

class Account:
    def __init__(self, accounts_list: list, client = None):
        self._balance = 0
        self._agency = '0001'
        self._number = self.verify_agency_number(accounts_list)
        self._client = client
        self._historic = Historic()
        
    def verify_agency_number(accounts_list: list):
        number = len(accounts_list) + 1
        return number
    
    def balance(self):
        print(self._balance)

    def new_account(self, account_list):
        if self._client == None:
            print('Account without Client')
        else:
            new_account = Account(account_list, self._client)
            return new_account
        
    def loot(self, value: float):
        self.balance -= value

    def deposit(self, value: float):
        self.balance += value

class Deposit(Transaction):
    def __init__(self):
        super().__init__()
        self._value = self.verifyNumber()
        
    def verify_number(self):
        try:
            value = float(input('Send value to deposit: '))
            if value <= 0:
                raise
            return value
        except:
            print('invalid value')
            self.verifyNumber()
            
    def register(self, account: Account):
        account._historic.add_transaction(self)
        account.deposit(self._value)
        
class Loot(Transaction):
    def __init__(self):
        super().__init__()
        self._value = self.verifyNumber()
        
    def verifyNumber(self):
        try:
            value = float(input('Send value to loot: '))
            if value <= 0:
                raise
            return value
        except:
            print('invalid value')
            self.verifyNumber()
            
    def register(self, account: Account):
        if account._balance - self._value >= 0:
            account._historic.add_transaction(self)
            account.loot(self._value)
        else:
            print("You haven't sufficient balance")

class Client:
    def __init__(self):
        self._adress = self.get_address()
        self._accounts = []
        
    def get_address(self):
        while True:
            adress = input('Please input your address in the format -> address - number - CEP - City/UF: ')
            if re.match(REGEX_ADRESS, adress):
                return adress
            else:
                print("Invalid address format. Please follow the specified format.")
    
    def realize_transaction(self, account: Account, transaction: Transaction):
        transaction.register(account)

    def add_account(self, account: Account):
        self.accounts.append(account)
        account._agency = self
        
class current_account(Account):
    def __init__(self, accounts_list: list, client: None):
        super().__init__(accounts_list, client)
        self._limit = 500
        self._loot_limit = 3

class fisic_person(Client):
    def __init__(self):
        super().__init__()
        self._cpf = self.get_Cpf()
        self._name = self.get_Name()
        self._BornDate = self.get_BornDate()

    def get_name(self):
        while True:
            name = input('Please input your complete Name: ')
            if all(x.isalpha() or x.isspace() for x in name) and name:
                return name
            else:
                print("Invalid entry. Name should contain only letters and spaces.")

    def get_born_date(self):
        while True:
            bornDate = input('Please input your born date in the format -> day/month/year: ')
            try:
                birth_date = datetime.strptime(bornDate, "%d/%m/%Y")
                if birth_date > datetime.now():
                    print("Date cannot be in the future.")
                else:
                    return bornDate
            except ValueError:
                print("Invalid date format. Please use day/month/year.")

    def get_cpf(self):
        while True:
            cpf = input('Please input your CPF number: ')
            cpf = cpf.replace('.', '').replace('-', '')
            if len(cpf) == 11 and cpf.isdigit():
                return cpf
            else:
                print("Invalid CPF. Ensure it has 11 digits without dots or hyphens.")