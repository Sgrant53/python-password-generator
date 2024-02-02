import random

capital_let ="QWERTYUIPASDFGHJKLZXCVBNM"
small_let = "qwertyuipasdfgjlzxcvbnm"
numbers = "1234567890"
special_char = "?,.<>!%$]{&^)#@"

upper,lower,digits,odd, = True, True, True, True

finalpass = ""

if upper:
    finalpass += capital_let
if lower:
    finalpass += small_let
if digits:
    finalpass += numbers
if odd:
    finalpass += special_char

lenght = 15 
howmuch = 10

for x in range(howmuch):
    password = "".join(random.sample(finalpass,lenght))
    print(password)
