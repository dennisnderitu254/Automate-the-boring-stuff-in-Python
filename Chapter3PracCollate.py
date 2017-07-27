# The Collatz Sequence

"""

Write a function named collatz() that has one parameter named number . If
number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1 .
Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1 .
(Amazingly enough, this sequence actually works for any integer—sooner
or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t
sure why. Your program is exploring what’s called the Collatz sequence, some-
times called “the simplest impossible math problem.”)
Remember to convert the return value from input() to an integer with
the int() function; otherwise, it will be a string value.
Hint: An integer number is even if number % 2 == 0 , and it’s odd if
number % 2 == 1 .

"""

def collatz(number):
    global result
    if number % 2 == 0:
        print(str(number // 2))
        result = number // 2
        return result
    elif number % 2 == 1:
        print(str(3 * number + 1))
        result = 3 * number + 1
        return result

print('Enter number:')
while True:
    try:
        number = int(input())
    except ValueError:
        print('The value must be an integer!')
        continue
    collatz(number)
    if result == 1:
        break
