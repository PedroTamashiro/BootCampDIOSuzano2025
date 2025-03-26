from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import pytz
import re

REGEX_ADRESS = '^[A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ\s]+-\s\d+\s-\s\d{5}-\d{3}\s-\s[A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ\s]+\/[A-Za-z]{2}$'

class user:
    def __init__(self):
        self.name = self.get_name()
        self.bornDate = self.get_born_date()
        self.cpf = self.get_cpf()
        self.adress = self.get_address()
        self.balance = 0
        self.extract = []
        self.lat = -23.5489
        self.lng = -46.6388
        self.currentTransaction = datetime.now()
        self.transactionNumber = 0
        self.lootNumber = 0
        self.lastTransaction = self.currentTransaction - timedelta(days=1)
        self.account = []
        self.account = self.get_account()

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
        
    def getCurrentTime(self):
        timeZoneStr = TimezoneFinder().timezone_at(lat=self.lat, lng=self.lng)
        if timeZoneStr:
            timezone = pytz.timezone(timeZoneStr)
            self.lastTransaction = self.currentTransaction
            self.currentTransaction = datetime.now(timezone)
            return self.currentTransaction
        
    def confLimit(self):
        if self.lastTransaction.day < self.currentTransaction.day:
            self.transactionNumber = 0
        return self
        
    def deposit(self):
        self.getCurrentTime()
        self.confLimit()
        deposit = float(input('Input value: '))
        if deposit > 0:
            self.balance += deposit
            extractText = f'deposited: R${deposit:.2f} - {self.currentTransaction}'
            self.extract.append(extractText)
            self.transactionNumber += 1
        else:
            print('Invalid Input')
        return self.balance, self.extract

    def loot(self, limitLootValue: int, limitLoot: int):
        self.getCurrentTime()
        self.confLimit()
        loot = float(input('Input value: '))
        if loot <= limitLootValue and loot > 0:
            if self.lootNumber < limitLoot:
                self.balance -= loot
                if self.balance > 0:
                    extractText = f'Looted: R${loot:.2f} - {self.currentTransaction}'
                    self.extract.append(extractText)
                    self.lootNumber += 1
                    self.transactionNumber += 1
                else:
                    self.balance += loot
                    print("You haven't sufficient balance")
            else:
                print('Loot Number limit hit')
        else:
            print('Loot Value invalid')
            
        return self.balance, self.extract

    def lookExtract(self):
        print(f'You have {len(self.extract)} itens in extract:')
        if len(self.extract) > 0:
            for n in range(len(self.extract)):
                print(f'-> {self.extract[n]}')
        else:
            print('Any move registred')
        print(f'\nAtual balance: R${self.balance:.2f}')

class account:
    def __init__(self):
        self.agency = self.get_agency()
        self.number = self.get_number()
