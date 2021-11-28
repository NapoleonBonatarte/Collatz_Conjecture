###
# Author: Tyler Windemuth
# Description: This program is a simple program that runs through a  number of steps in a
#              Collatz conjecture, also known as the 3n+1 problem.
#              The program asks for a user inputted start number, and a step limiter.





start_number = int(input("Enter Start number: \n"))  # asking user for start value
# asks user for limit value (how many steps program is allowed to take)
limit = int(input("Please enter limit: \n"))
# establishing variables
steps = 0
odd = 0
even = 0
temp1 = start_number
# While the number is not 1, and steps are less than user set limit, run loop.
while temp1 != 1 and steps < limit:
    if (temp1 % 2) == 0:  # even number
        temp1 = temp1 / 2
        print("even", temp1)
        even += 1
        steps += 1
        if temp1 == 1:
            print("Break")
            break
    if (temp1 % 2) != 0:  # odd number
        temp1 = temp1 * 3 + 1
        print("odd", temp1)
        odd += 1
        steps += 1
        if temp1 == 1:
            print("Break")
            break
    if temp1 == start_number:  # number equals start number, which means an infinite loop
        print('Found', temp1)
        final = temp1
        break

# prints out final information
print("")
print("steps end", steps)
print("final = ", temp1)
print("even numbers = ", even)
print("odd numbers = ", odd)
