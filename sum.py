import sys

def sum_values(n):
    sum = 0
    for number in range(1, n + 1):
        sum = sum + number
    return sum
if len(sys.argv) == 2:
    try:
        print("SUM: ", sum_values(int(sys.argv[1])))
    except ValueError:
        print("I need an integer to work")
else:
    print("Not enough arguments")