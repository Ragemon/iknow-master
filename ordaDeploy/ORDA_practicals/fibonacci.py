def fib(num):
    a,b = 0,1
    result = []

    for i in range(num):
        a,b = b,a+b
        result.append(a)
    print(result)





if __name__ == '__main__':
    import timeit

    ask = int(input('Enter a value: '))
    #timeit.repeat(lambda: fib(ask))

    timeit.repeat(lambda : fib(ask))


