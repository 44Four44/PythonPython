"""
Disadvantages of recursion:
- Very very slow compared to for loops and other iterations
- Max recursion depth error
"""

import time
def is_palindrome(word):
    # Catches error
    if len(word) == 0:
        return -1
    # Base case
    if len(word) < 2:
        return True
    # Checks if ends are equal
    return word[0:1].upper() == word[len(word)-1:len(word)].upper() and is_palindrome(word[1:-1])


# Execution timer
start_time = time.time()
print(is_palindrome('racecar'))
print("Execution time: %s seconds" % (time.time() - start_time))