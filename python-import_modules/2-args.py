#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    count = len(argv) - 1

    if count == 0:
        print("{:d} arguments.".format(count))
    elif count == 1:
        print("{:d} argument:".format(count))
        print("{:d}: {}".format(1, argv[1]))
    else:
        print("{:d} arguments:".format(count))
        for i in range(1, count + 1):
            print("{:d}: {}".format(i, argv[i]))
