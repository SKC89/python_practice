def celsius_to_fahrenheit(c):
    return c*9 / 5 + 32
def hottest(new):
    highest=new[0]
    for x in new:
        if x>highest:
            highest=x
    return highest
new=[]
for x in range (4):
    try:
        a=float(input('Type temperature: '))
        b=celsius_to_fahrenheit(a)
        new.append(b)
    except ValueError:
        print("Skipped, not a number")
if len(new)==0:
    print("No temperatures entered.")
else:
    print(new)
    print(hottest(new))

