from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import pytz
import re

REGEX_ADRESS = '^[A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ\s]+-\s\d+\s-\s\d{5}-\d{3}\s-\s[A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ\s]+\/[A-Za-z]{2}$'

class User:
    def __init__(self, number: int):
        self.name = self.get_name()
        self.borndate = self.get_born_date()
        self.cpf = self.get_cpf()
        self.adress = self.get_address()
        self.balance = 0
        self.extract = []
        self.lat = -23.5489
        self.lng = -46.6388
        self.current_transaction = datetime.now()
        self.transaction_number = 0
        self.loot_number = 0
        self.last_transaction = self.current_transaction - timedelta(days=1)
        self.Accounts = []
        self.create_account(number)

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

    def get_address(self):
        while True:
            adress = input('Please input your address in the format -> address - number - CEP - City/UF: ')
            if re.match(REGEX_ADRESS, adress):
                return adress
            else:
                print("Invalid address format. Please follow the specified format.")
        
    def get_current_time(self):
        timeZoneStr = TimezoneFinder().timezone_at(lat=self.lat, lng=self.lng)
        if timeZoneStr:
            timezone = pytz.timezone(timeZoneStr)
            self.last_transaction = self.current_transaction
            self.current_transaction = datetime.now(timezone)
            return self.current_transaction
        
    def conf_limit(self):
        if self.last_transaction.day < self.current_transaction.day:
            self.transaction_number = 0
        return self
        
    def deposit(self):
        self.getCurrentTime()
        self.confLimit()
        deposit = float(input('Input value: '))
        if deposit > 0:
            self.balance += deposit
            extract_text = f'deposited: R${deposit:.2f} - {self.current_transaction}'
            self.extract.append(extract_text)
            self.transaction_number += 1
        else:
            print('Invalid Input')
        return self.balance, self.extract

    def loot(self, limitLootValue: int, limitLoot: int):
        self.getCurrentTime()
        self.confLimit()
        loot = float(input('Input value: '))
        if loot <= limitLootValue and loot > 0:
            if self.loot_number < limitLoot:
                self.balance -= loot
                if self.balance > 0:
                    extract_text = f'Looted: R${loot:.2f} - {self.current_transaction}'
                    self.extract.append(extract_text)
                    self.loot_number += 1
                    self.transaction_number += 1
                else:
                    self.balance += loot
                    print("You haven't sufficient balance")
            else:
                print('Loot Number limit hit')
        else:
            print('Loot Value invalid')
            
        return self.balance, self.extract

    def look_extract(self):
        print(f'You have {len(self.extract)} itens in extract:')
        if len(self.extract) > 0:
            for n in range(len(self.extract)):
                print(f'-> {self.extract[n]}')
        else:
            print('Any move registred')
        print(f'\nAtual balance: R${self.balance:.2f}')

    def create_account(self, number: int):
        account = Account(number, self.cpf)
        self.Accounts.append(account)

class Account:
    def __init__(self, number: int, cpf: int):
        self.agency = '0001'
        self.number = number
        self.cpf = cpf