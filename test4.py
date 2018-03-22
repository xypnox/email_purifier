#!/usr/bin/python

import sys


def main(argv):
    for args in argv:
        print(args)
    print(argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])
