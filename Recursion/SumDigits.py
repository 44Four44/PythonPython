import time
def sum_digits(number):
    if number < 0:
        return -1
    if number < 10:
        return number
    return sum_digits(int(number/10)) + number % 10

# Execution timer
start_time = time.time()
print(sum_digits(911111111111))
print("Execution time: %s seconds" % (time.time() - start_time))