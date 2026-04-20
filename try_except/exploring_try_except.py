try:
    number = int(input("Enter a number: "))
    print("Your inputed number is: ", number)
except ValueError as err:
    print(err)



try:
    num = 11/0
    print(num)
except ZeroDivisionError as zeroErr:
    print(zeroErr) 