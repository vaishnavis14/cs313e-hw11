#  File: Tower.py

#  Description: The goal is to move all the rings from source to destination by only moving 1 ring at a time and at no point should a larger ring be on top of a smaller ring

#  Student's Name: Vaishnavi Sathiyamoorthy

#  Student's UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/12/2022

#  Date Last Modified: 10/14/2022

import sys
import math

# Code help was given by TA Kunaal
# If n is less than or equal to 1, it returns 1
# The recursive case is moving n-1 from source to spare 1
# work + 1 is added because the bottom plate is added
# Then we move from spare 1 to destination
def towers3(n, source, spare1, destination):
    if n <= 1:
        return 1
    else:
        work = 0
        work += towers3(n - 1, source, destination, spare1)
        work += 1
        work += towers3(n - 1, spare1, source, destination)
        return work

# we calculate k using the formula
# we move k disks from source to spare 1
# we act as if there are only 3 pegs (spare1 doesnt exist)
# we call towers 3 because we ignore spare1
# we move n - k disks from source to spare 2
# we bring spare 1 back and call towers4 again. We move from spare1 to destination
def towers4(n, source, spare1, spare2, destination):
    if n <= 1:
        return n
    else:
        work = 0
        k = n - round(math.sqrt(2 * n + 1)) + 1
        work += towers4(k, source, destination, spare2, spare1)
        work += towers3(n - k, source, destination, spare2)
        work += towers4(k, spare1, source, spare2, destination)
        return work

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
    return towers4(n, "A", "B", "C", "D")

def main():
  # read number of disks and print number of moves
  for line in sys.stdin:
    line = line.strip()
    num_disks = int (line)
    print (num_moves (num_disks))

if __name__ == "__main__":
  main()

