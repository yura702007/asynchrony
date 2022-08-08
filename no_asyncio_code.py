import time


def fun_1(x):
    print(x ** 2)
    time.sleep(3)
    print('fun_1 the end\n')


def fun_2(x):
    print(x ** .5)
    time.sleep(3)
    print('fun_2 the end\n')


def main():
    fun_1(4)
    fun_2(4)


print(time.strftime('%X'))
main()
print(time.strftime('%X'))
