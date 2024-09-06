import sys
#
# # print(help(sys))
#
class MyError(BaseException):
    pass

def f(a, b):
    if len(sys.argv) != 3:
        raise MyError('Arguments must be provided as command line parameters.')


    return a + b

def main():
    a = int(sys.argv[1])
    b = sys.argv[2]
    # a, b, c = map(int, sys.argv[1:])
    # a, b = [int(arg) for arg in sys.argv[1:]]
    # a, b = (int(arg) for arg in sys.argv[1:])
    try:
        res = f(a, b)
        print(res)
    except MyError:
        print('Please run code on command line.')
    except TypeError:
        print('Arguments must be integer.')
    print(sys.argv)

if __name__ == '__main__':
    main()


# raise ValueError('Value Error')