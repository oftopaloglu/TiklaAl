import sqlite3

db = sqlite3.connect("db.sqlite3")

vt = db.cursor()

read = vt.execute("SELECT para from iyzico_payment")

sum = 0

for price in read:
    price = str(price)
    price = int(price[1:-2])
    
    sum += price

vt.close()

print(sum)