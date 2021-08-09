'''
making a program
that prints all prime numbers
between start and end range
'''
def next_prime(start, end):

    isStart = input('do you wanna start the game? (y/n): ')
    start_boolean = False

    if isStart == 'y':
            start_boolean = True
            while start_boolean:
                response = input('do you wanna print the prime numbers? (y/n): ')
                for num in range(start, end + 1):
                    if num > 1:
                        for i in range(2, num):
                            if num % i == 0:
                                break
                        else:
                            if response == 'y':
                                print(num)
                                break
                            elif response == 'n':
                                start_boolean = False
                            else:
                                print('please enter y or n')



start_v = int(input('start value of range: '))
end_v = int(input('end value of range: '))

next_prime(start_v, end_v)
