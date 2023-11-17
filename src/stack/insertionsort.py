from node.node import * 
from stack.stack import *


def sort(data: stack ,first: int):
    """Sorts a stack from smallest to largest 
    bypassing the nodes to the left of first.

    Args:
        data (int): stack to be sorted
        first (int): the node position at which 
        the sort will begin 
    """    
    # Initialize loop counter variable i to 1 
    i = 1

    # Initialize loop counter variable j to 0 
    j  = 0

    # Initialize next value to 0 
    nextVal = 0 

    # loop through list as many times as specified by the
    # length of the list and first 
    # this loop represents the blue arrow 
    while(i <= data.size() - first):
        # store a copy of the number in index position first + i 
        # in next value  
        nextVal = node.listPosition(data.getHead(),first +i).get_data() #data[first+i]

        # loop through the list starting at the same index as 
        # next value and iterate back toward first as long as 
        # the element to the left of next value is greater than 
        # next value and we're not the whole way back to first 
        j = first + i 
        while (j > first and node.listPosition(data.getHead(),j-1).get_data() > nextVal):

            # shift the element to left of next value right
            # ward one position 
            node.setDataAtPosition(data.getHead(),j,node.listPosition(data.getHead(),j-1).get_data())
            #node.listPosition(data.getHead(),j-1).get_data()
            #data[j] = data[j-1]

            # insert next value into the element that was just 
            # shifted 
            node.setDataAtPosition(data.getHead(),j-1,nextVal)
            
            #data[j-1] = nextVal 

            # decrement j by 1 
            j -= 1 

        # increment i by 1 
        i += 1 