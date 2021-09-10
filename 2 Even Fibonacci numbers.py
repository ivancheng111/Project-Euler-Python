""" Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Start: Sep/09/2021 12:50pm
Finished: Sep/09/2021 6:30pm
"""

def compute(max):
    # initalize first 2 fibonnaci numbers 1,1
    x = y = 1
    sum = 0
    while x < max:
        # check if x is even, add to sum
        if x % 2 == 0:
            sum += x
        # generate next fibonnaci number
        x, y = y, x+y
    yield sum

# 4e6 is 4mil in index notation
for i in compute(4e6): print(f"Sum of All Even Fibonacci Numbers Less Than 4 Million Is: {i}")