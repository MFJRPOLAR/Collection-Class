from stack.stack import *
from node.node import *


def search(a: stack, first:int, size:int, target):
    """Searches for a target value in stack of nodes
    starting at first.

    Args:
        a (stack): the stack to search
        first (int): the stack position at which the search will start
        size (int): the number of nodes to search 
        target : the target value to search for

    Returns:
        int: If target appears in the stack, position of the node 
         that contains target; else -1.
    """    
    # Set and int variable i to 0 
    i = 0

    # set a boolean variable foun to false
    found = False 

    # while there are more elements to search 
    # and the target hasn't been found and
    # i plus first doesn't exceed the length of 
    # the list 
    
    while ((i<size) and (i+first < a.size()) and not found):
        # if the current element is the target
        if(node.listPosition(a.getHead(),i+first).get_data() == target):
            # set found to true
            found = True
        else:
            # increment i by 1
            i += 1
    # check if the target was found 
    if (found):
        # Return index of the target 
        return i + first 
    else:
        # Return negative 1
        return -1 