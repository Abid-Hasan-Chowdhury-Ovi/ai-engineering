title = 'Personal Finance Tracker'
print(f'{'_'*10}+{title}+{'_'*10}')

name =input('What is your name?')
name= name.strip().title()
description = input('What did you buy?')

price_text=input('Price of One Item: ')
unit_price=float(price_text)

quantity_text= input('How many times?')
quantity= int(quantity_text)

total = unit_price*quantity

print('Thanks', name)
print("Here is your record: ")

print(f'{'Item':<15}{'Price':>10}{'Qty':>6}{'Total':>12}')
print('-'*43)
print(f'{description:<15}{unit_price:>10}{quantity:>6}{total:>12}')
