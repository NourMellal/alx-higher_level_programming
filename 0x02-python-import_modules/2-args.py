#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    len_argv = len(argv) - 1

    if len_argv == 0:
        print("0 arguments.")
    elif len_argv == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len_argv))
    for i in range(len_argv):
        print("{}: {}".format(i + 1, argv[i + 1]))
