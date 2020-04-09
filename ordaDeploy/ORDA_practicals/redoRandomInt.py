import random

generated =  random.randint(1,9)
record = 0

while True:
    try:
        try:
            prompt = int(input('Guess a random number between 1 and 9: '))
            if prompt not in range(1,10) or prompt == None:
                break
        except:
            break
        else:
            print('Invalid input: Try again: ')
        if prompt > generated:
            print('Guess again your number is too bigger.')
            record += 1
        if prompt < generated:
            print("Guess again your number is too small.")
            record += 1
        if prompt == generated:
            print('Your guess is correct.')
            print('You guessed {} number of times before you had it correct.'.format(record))
            print('Press any key to quit or continue as normal...\n')

            generated = random.randint(1, 9)

    except ValueError:
        print('Your input value is invalid.')


