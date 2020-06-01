# Author: Nguyen L.
# Date:   April 29th, 2020
# Find the median in a set of numbers

# function to find median of a list
def findMedian(my_list):

    #declaring variables
    l = len(my_list)
    index = 0

    #conditional statements to find the median
    if l == 0:
        return 0
    #even
    elif l % 2 == 0:
        index = l // 2 - 1
        return (my_list[index] + my_list[index+1]) / 2
    #odd
    else:
        index = l // 2
        return my_list[index]

first_list = [3, 5, 2, 10]
first_list.sort()
print("First list: " + str(first_list))
result = findMedian(first_list)
print("Median: " + str(result) + "\n")

second_list = [11, 4, 5, 2, 9]
second_list.sort()
print("Second list: " + str(second_list))
result = findMedian(second_list)
print("Median: " + str(result))