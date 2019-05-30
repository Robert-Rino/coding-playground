import random
import re
import sys

def iterate_substring_of_input():
    '''
    'abcd'
    :return:
        a
        b
        c
        d
        ab
        bc
        cd
        abc
        bcd
        abcd
        None
    '''
    input = raw_input("hi")
    for l in range(1, len(input)+1):
        for start in range(len(input)+1-l):
            print input[start:start+l]

def read_stdin():
    input = raw_input('type someting')
    for line in sys.stdin:
        print line


if __name__ == '__main__':
    # print iterate_substring_of_input()
    read_stdin()