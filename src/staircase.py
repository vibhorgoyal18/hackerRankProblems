# Consider a staircase of n size :
#
#    #
#   ##
#  ###
# ####
# Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces.
# The last line is not preceded by any spaces.
#
# Write a program that prints a staircase of size n.

def staircase(n):
    for row in range(n):
        print((" " * (n - 1 - row)) + ("#" * (row + 1)))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
