from node.node import * 
from stack.stack import *


def sort(data: stack, first: int):
    """Sorts a listof intergers from smallestto largest 
    bypassing the elements to the left of first

    Args:
        data (int): list of integers
        first (int): the list index atwhich the sort will begin 
    """    

    #Intialize loop counter variable named i 
    i = data.size() - first - 1 

    # initialize loop counter variable named j to 0 
    j = 0 

    # Initialize variable named big that will be used 
    # to store the index of the biggest value 
    big = 0 

    # initialize varibale named temp that will be used 
    # to swap list values 
    temp = 0 

    # loop trhrough list as many times as specified by 
    # len(data) and first 
    # this loop represents the blue arrow 
    while (i > 0 ):
        # set big equal to first
        big = first  

        # set j equal to first + 1 
        j = first + 1 

        # loop through list starting with element at
        # first + 1 and continue until reach first + i 
        # this loop represents the yellow arrow 
        while (j <= first + i ):
            # if the value in data[big] is less than 
            # data[j]
            if (node.listPosition(data.getHead(),big).get_data() < node.listPosition(data.getHead(),j).get_data()): 
                # set big equal to j 
                big = j 
            # Increment j by 1 
            j += 1 

        # swap the data in first + i with the data in big 
        # set temp to value in data[first + i]
        #temp = data[first+ i]

        #set data[first+i] to value in data[big]
        #data[first+i] = data[big]

        # set data[big] to value in temp
        #data[big] = temp 
    
        # decrement i by 1
        i -= 1