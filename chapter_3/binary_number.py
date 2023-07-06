def find_binary(binary_num):
    power = 0
    binary = 0
    while binary_num != 0:

        right_reminder = binary_num % 10
        binary += right_reminder * (2**power)
        binary_num //= 10 
        power += 1
    print(binary)
find_binary(1101)
