prices = {"apple": 2.0, "banana": 0.5, "mango": 3.5}
total=0
for i in range(3):
    try:
        a=input('Item name: ')
        b=int(input('Quantity: '))
        cost=prices[a]*b
        total=total+cost     
    except KeyError:
        print("Not sold here, skipped")
    except ValueError:
        print("Quantity must be a whole number, skipped")

print(total)
