import time
import sys


def printStar(n):
        for i in range(n):
                print('*', end='')
                # sys.stdout.flush()
                time.sleep(1)

if __name__ == '__main__':
        printStar(10)