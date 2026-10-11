title = 'Personal Finance Tracker'
print(f'{'_'*10}+{title}+{'_'*10}')

name =input('What is your name?')
description = input('What did you buy?')

price_text=input('Price of One Item: ')
unit_price=float(price_text)

quantity_text= input('How many times?')
quantity= int(quantity_text)

total = unit_price*quantity

print('Thanks', name)
print("Here is your record: ")
print(description,total)