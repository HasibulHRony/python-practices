def max_num(num1, num2, numm3):
    if num1 >= num2 and num1 >= numm3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return numm3

maximum_number = max_num(70, 43, 85)
print(maximum_number)