#!/usr/bin/python3
if __name__ == '__main__':

    import sys

    argucnt = len(sys.argv) - 1
    # our condi that will demonstaret our program
    if argucnt == 0:
        print("0 arguments.")
    elif argucnt == 1:
        print('1 argument:')
    else:
        print('{} arguments:'.format(argucnt))
    for i in range(argucnt):
        print('{}: {}'.format(i + 1, sys.argv[i + 1]))
