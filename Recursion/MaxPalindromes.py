import time
def max_palindromes(word):
    if len(word) == 1:
        return 1
    if len(word) == 2:
        if word == word[::-1]:
            return 1
        else:
            return 0
    return max_palindromes(word[1:]) + max_palindromes(word[:1])

# Execution timer
start_time = time.time()
print(max_palindromes('racecar'))
print("Execution time: %s seconds" % (time.time() - start_time))