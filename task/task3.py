'''
write a program that asks the user how many Fibonacci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.

'''


def fibonacci(number):
    fibonacci_list = []

    a, b = 0, 1

    for i in range(number):
        fibonacci_list.append(a)
        a, b = b, a + b

    return fibonacci_list


def main():
    user = int(input('Reqem daxil edin: '))

    if user <= 0:
        print('Yanliş reqem')

    else:
        fibonacci_numbers = fibonacci(user)

        for i in fibonacci_numbers:
            print(i)
main()