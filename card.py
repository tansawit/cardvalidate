def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

def card_valid_check(number):
    card = list(map(int, list(number)))
    odd = card[1::2]
    even = [sum_digits(digit*2) for digit in card[::2]]
    checksum = sum([x + y for x, y in zip(odd, even)])
    if checksum%2 == 0:
        return True
    else:
        return False
    
#Returns Card Issuer if Valid
def card_issuer_check(number):
    card = list(map(str, list(number)))
    if card[0] == '4':
        return "Visa"
    elif 51<=int(''.join(card[0:2]))<=55:
        return "MasterCard"
    elif ''.join(card[0:4]) == '6011' or ''.join(card[0:3]) == '644' or ''.join(card[0:2]) == '65':
        return "Discover"
    elif ''.join(card[0:2]) == '34' or ''.join(card[0:2]) == '37':
        return "Amex"


card_number = input("Enter Credit Card Number: ").replace(" ","")
issuer = card_issuer_check(card_number)
if issuer:
    print("Credit Card Issuer: {}".format(issuer))
    if card_valid_check(card_number):
        print("Credit Card Number is Valid")
    else:
        print("Invalid Credit Card Number")
else:
    print("Invalid Credit Card Number")

