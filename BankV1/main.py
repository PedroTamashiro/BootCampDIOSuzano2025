import methods

menu = """

[1] Deposit
[2] Loot
[3] extract
[4] Get Out

=>"""

balance = 0
extract = []
lootNumber = 0
LOOT_LIMIT = 500
MAX_LOOT_NUMBER = 3

while True:
    option = input(menu)
    
    if option == '1':
        balance, extract = methods.deposit(balance, extract)
        print(f'Atual balance: {balance}')
        
    elif option == '2':
        balance, extract, lootNumber = methods.loot(balance, extract, LOOT_LIMIT, MAX_LOOT_NUMBER, lootNumber)
        print(f'Atual balance: {balance}')
        
    elif option == '3':
        methods.lookExtract(extract, balance)
        
    elif option == '4':
        break
    
    else:
        print('Invalid Operation')