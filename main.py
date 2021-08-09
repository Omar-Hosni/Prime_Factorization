'''
making a program
that prints all prime numbers
between start and end range
'''

start = int(input('enter the first number: '))
end = int(input('enter the end number: '))

print('we are going to find the prime numbers between ', start, ' and ', end)

for num in range(start, end + 1):
    # prime numbers that are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)
