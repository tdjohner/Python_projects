#-------------------------------------------------------------------------

#                   Lab1TJ.py

#-------------------------------------------------------------------------

#                Teagan Johner

#                  Program name:  Percentage of Odd Integers
#-------------------------------------------------------------------------

#   count_odd() goes through each number in a given list and counts how many of them are odd

#   syntax: count_odd([list of numbers here])
#       ex.
#            count_odd([1, 2, 3, 4])

#   arguments: listOfNumbers

#   returns: the total of odd numbers in listOfNumbers

def count_odd(listOfNumbers):
    tally = 0
    for i in range(len(listOfNumbers)):
        if listOfNumbers[i] % 2 == 1:
            tally += 1
    return tally

#   percent_odd gives the percentage of numbers in a list that are odd

#   syntax: percent_odd([list of numbers here])
#       ex.
#            percent_odd([1, 2, 3, 4])

#   arguments: listOfNumbers

#   returns: the percentage of odd numbers in the list

def percent_odd(listOfNumbers):
    oddNum = count_odd(listOfNumbers)
    tally = 0
    for i in range(len(listOfNumbers)):
        tally += 1
    if oddNum != 0:
        return tally / oddNum
    else:
        return 0
    
    
    
            
        
    