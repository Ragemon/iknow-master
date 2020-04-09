
def stop(func):
    while True:
        stopFunc = input('If you want to quit type Quit: \n').capitalize()
        if stopFunc[0] == 'q':
            break
        func()


def divisor():
    try:
        testVar = int(input('Enter a number to obtain it\'s divisor: '))
        container = []
        for i in range(1,testVar+1):
            if testVar%i == 0:
                container.append(i)
        print(container)
        stop(divisor)
    except ValueError:
        print('Input must be a string.\nTry again.')
        stop(divisor)


divisor()















