# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import time


def print_cube(num):
    # function to print cubes from 0 to num
    for i in range(num+1):
        print("Cube: {}".format(i * i * i))


def print_square(num):
    # function to print square from 0 to num
    for i in range(num+1):
        print("Square: {}".format(i * i))


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_square, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")
