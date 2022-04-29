from replit import clear
from art import logo
print(logo)

#HINT: You can call clear() to clear the output in the console.
start = True
empty_dict = {}
while start:
  name = input('What is your name: ')
  bid = int(input('What is your bid: '))
  empty_dict[name] = bid
  ask = input('Is there any more bidders-')
  if ask == 'yes':
    clear()
    continue
  elif ask == 'no':
    start = False
    break
nam= ''
highest_bidder = 0
for bidders in empty_dict:
  if highest_bidder == 0:
    highest_bidder += empty_dict[bidders]
  if highest_bidder < empty_dict[bidders]:
    nam = bidders
    highest_bidder = empty_dict[bidders]
clear()
print(logo)
print(f'{nam} is the highest bidder with {highest_bidder}$!!!')
  
  