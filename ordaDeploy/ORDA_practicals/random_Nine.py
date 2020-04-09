import random, time, tqdm, turtle




def turtler(choice):
    if choice == 1:
        spiral = turtle.Turtle()
        for i in range(20):
            spiral.forward(i*10)
            spiral.right(144)
        turtle.done
    if choice == 2:
        painter = turtle.Turtle()
        painter.pencolor('blue')
        for i in range(50):
            painter.forward(200)
            painter.left(492)
        painter.pencolor('red')
        for i in range(50):
            painter.forward(50)
            painter.left(123)
        painter.pencolor('yellow')
        for i in range(50):
            painter.forward(50)
            painter.left(123)
    if choice == 3:
                  
        ninja = turtle.Turtle()
        ninja.pencolor('blue')
        ninja.speed(1000000000)
        for i in range(180):
            ninja.forward(100)
            ninja.right(30)
            ninja.forward(20)
            ninja.left(60)
            ninja.forward(50)
            ninja.right(30)

            ninja.penup()
            ninja.setposition(0,0)
            ninja.pendown()

            ninja.right(2)
        turtle.done()
                  

                  
                  
#turtler(2)

def randomInt():
    false_record = int
    record = int
    print('#_#'*13+' THE ADVENTURE OF RANDOMNESS ' + '#_#'*13)
    time.sleep(1)

    for i in tqdm.tqdm(range(4)):
        time.sleep(1.2)

    #('Press any key to start our adventure... ')
    print('Welcome')


    while True:
        promptu = int(input('Guess the special number: '))
        if promptu > 9 and promptu < 0:
            print('Remaian in the range of 1 - 9!')


        else:
            try:
                rightChoice = random.randint(1,9)
                if promptu == rightChoice:
                    repr=+1

                    for i in range(3):
                        print('Hurraaaay             \n')
                        sleep(0.001)
                        turtler(random.randint(1,3))
                        print('\n YOU GUESSED RIGHT MY CHILD ')



                else:
                    false_record =+ 1
                    print('BOOOOOOOOOOOOOW WROOOONG!\n')
                    if promptu > rightChoice:
                        print('...Number is bigger than what I was looking for!')
                    else:
                        print('...Number is less than what I was looking for!\nTry again.')





                tryAgain = input('Press any key to restart or E to exit ').lower()
                if tryAgain == 'e':
                    print('You won {} times and lost {} times.'.format(record, false_record))
                    break

            except:
                pass


randomInt()