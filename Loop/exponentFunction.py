def rise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result*base_num
    return result

powered_value = rise_to_power(3,2)
print(powered_value)