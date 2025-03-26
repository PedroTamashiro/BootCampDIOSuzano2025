from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

def getCurrentTime(lat: float, lng: float):
    timeZoneStr = TimezoneFinder().timezone_at(lat=-23.5489, lng=-46.6388)
    if timeZoneStr:
            timezone = pytz.timezone(timeZoneStr)
            return datetime.now(timezone)
    
def deposit (balance: float, extract: list, currentTransaction: datetime):
    deposit = float(input('Input value: '))
    if deposit > 0:
        balance += deposit
        extractText = f'deposited: R${deposit:.2f} - {currentTransaction}'
        extract.append(extractText)
    else:
        print('Invalid Input')
    return balance, extract

def loot (balance: float, extract: list, limitLootValue: int, limitLoot: int, lootNumber: int, currentTransaction: datetime):
    loot = float(input('Input value: '))
    if loot <= limitLootValue and loot > 0:
        if lootNumber < limitLoot:
            balance -= loot
            if balance > 0:
                extractText = f'Looted: R${loot:.2f} - {currentTransaction}'
                lootNumber += 1
                extract.append(extractText)
            else:
                balance += loot
                print("You haven't sufficient balance")
        else:
            print('Loot Number limit hit')
    else:
        print('Loot Value invalid')
        
    return balance, extract, lootNumber

def lookExtract (extract: list, balance):
    print(f'You have {len(extract)} itens in extract:')
    if len(extract) > 0:
        for n in range(len(extract)):
            print(f'-> {extract[n]}')
    else:
        print('Any move registred')
    print(f'\nAtual balance: R${balance:.2f}')