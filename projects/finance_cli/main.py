title = 'Personal Finance Tracker'
print(f'{'_'*10}+{title}+{'_'*10}')

name =input('What is your name?')
name= name.strip().title()
description = input('What did you buy?')
description=description.strip()

if description=='':
    print('Error: The description can not be empty')
    exit()

price_text=input('Price of One Item: ')
if not price_text.replace('.','',1).isdigit():
    print("Error: The price must be a number, for example: 7.5")
    exit()
unit_price=float(price_text)
if unit_price <=0:
    print('Error: The price must be greater than 0')
    exit()

quantity_text= input('How many times?')
if not quantity_text.isdigit():
    print('Error: The quantity must be a whole number, for example 3')
    exit()
quantity= int(quantity_text)
if quantity<=1:
    print('Error: The quantity must be greater than 1')
    exit()


total = unit_price*quantity

print('Thanks', name)
print("Here is your record: ")

print(f'{'Item':<15}{'Price':>10}{'Qty':>6}{'Total':>12}')
print('-'*43)
print(f'{description:<15}{unit_price:>10.2f}{quantity:>6}{total:>12.2f}')
