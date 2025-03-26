import methods
import datetime

menu = """

[1] Deposit
[2] Loot
[3] extract
[4] Get Out

=>"""

lastTransaction = methods.getCurrentTime(-23.5489,-46.6388) - datetime.timedelta(days=1)
balance = 0
extract = []
lootNumber = 0
contTransaction = 0
LOOT_LIMIT = 500
MAX_LOOT_NUMBER = 3

while True:
    option = input(menu)
    currentTransaction = methods.getCurrentTime(-23.5489,-46.6388)

    if lastTransaction.day == currentTransaction.day:
        lastTransaction = currentTransaction
        contTransaction = 0

    if option == '1':
        if contTransaction < 10:
            balance, extract = methods.deposit(balance, extract, currentTransaction)
            contTransaction += 1
            print(f'Atual balance: {balance}')
        else:
            print('You reached the limit of day')
        
    elif option == '2':
        if contTransaction < 10:
            balance, extract, lootNumber = methods.loot(balance, extract, LOOT_LIMIT, MAX_LOOT_NUMBER, lootNumber, currentTransaction)
            contTransaction += 1
            print(f'Atual balance: {balance}')
        else:
            print('You reached the limit of day')
        
    elif option == '3':
        methods.lookExtract(extract, balance)
        
    elif option == '4':
        break
    
    else:
        print('Invalid Operation')