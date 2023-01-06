bids = {}

more_people = True
max_bid = 0
winner = ''
while more_people:
    name = input("User: ")
    price = float(input("Price: $"))
    bids[name] = price

    if price > max_bid:
        max_bid = price
        winner = name

    others = input("Are there any more users who want to bid? Y/N : ").lower()
    if others == 'n':
        more_people = False

print(f'\nThe winner is {winner} with the bid of ${bids[winner]}')


