from node.node import *

def main():
    # testInit()
    # testGettersAndSetters()
    testAddNodeAfter()

def testAddNodeAfter():
    print("Testing Add Node After")
    # construct a node with data equal to S and link equal to None 
    # and assign its reference to head 
    head = node('J', None) # R

    print("The head node contains data:", head.get_data())

    # declare a new node named selection and make it refer 
    # to the same node as head 
    selection = head 

    print("The head node contains data:", head.get_data())
    print("The selection node contains data:",selection.get_data())

    # add a node with data equal to O after the node selection 
    # refers to 
    selection.addNodeAfter('O') # J -> O

    # get selection's link and assign its reference back to 
    # selection 
    selection = selection.getLink() # O 

    print("The head node contains data:", head.get_data())
    print("The selection node contains data:",selection.get_data())

    # add a node with data equal to B after the node selection 
    # refers to 
    selection.addNodeAfter('B') # O -> B

    # get selection's link and assign its reference back to 
    # selection 
    selection = selection.getLink() # B

    print("The head node contains data:", head.get_data()) # J
    print("The selection node contains data:",selection.get_data()) # B

    # add a node with data equal to S after the node selection 
    # refers to 
    selection.addNodeAfter('S') # B -> S

    # get selection's link and assign its reference back to 
    # selection 
    selection = selection.getLink() # B

    print("The head node contains data:", head.get_data()) # J
    print("The selection node contains data:",selection.get_data()) # S

    # declare a new node named tail and make it refer to the same
    # node as head
    tail = head 

    # get tail's link and assign its reference to tail 
    # J -> O -> B -> S
    tail = tail.getLink() # O -> B -> S 
    tail = tail.getLink() # B -> S 
    tail = tail.getLink() # S 

    # add a new node with data equal to Z after the node tail 
    # refers to 
    tail.addNodeAfter('Z') 

    # get tail's link and assign its reference to tail 
    tail = tail.getLink() # S

    print("The head node contains data:", head.get_data()) # J
    print("The selection node contains data:",selection.get_data()) # S
    print("The tail node contains data:", tail.get_data()) # Z


def testGettersAndSetters(): 
    print("Testing Getters and Setters")

    # construct a node with data equal to S and link equal to None 
    # and assign its reference to head 
    head = node('R', None) # R

    print("The head node contains data:", head.get_data())

    head.set_data('S') # S
    print("The head node contains data:", head.get_data())

    head = node('B',head) # B -> S 
    print("The head node contains data:", head.get_data())

    head = node('O',head) # O -> B -> S 
    print("The head node contains data:", head.get_data())

    head = node('J',head) # J ->  O -> B -> S 
    print("The head node contains data:", head.get_data())

    # get head's link and assign its referece back to head 
    head = head.getLink() # O -> B -> S 
    print("The head node contains data:", head.get_data())

    # get head's link and assign its referece back to head 
    head = head.getLink() # B -> S 
    print("The head node contains data:", head.get_data())

    # get head's link and assign its referece back to head 
    head = head.getLink() # S 
    print("The head node contains data:", head.get_data())

    # get head's link and assign its referece back to head 
    """    head = head.getLink() # None
    print("The head node contains data:", head.get_data()) """

    print("The head node contains link:", head.getLink())

    # set head's link to a new code
    head.setlink(node('O',None)) # S -> O

def testInit():
    print("Testing Node Init")

    # construct a node with data equal to S and link equal to None 
    # and assign its reference to head 
    head = node('S', None) # S 

    # construct a node with data equal to B and link equal to head 
    # and assign its refernce to head 
    head = node('B', head) # B -> S 

    # construct a node with data equal to 0 and link equal to head 
    # and assign its reference to head 
    head = node('O', head) # O -> B -> S 

    # construct a node with data equal to J and link equal to head 
    # and assign its reference to head 
    head = node('J', head) # J -> O -> B -> S

    head = node(1, head) # 1 -> J -> O -> B -> S
    head = node(1.5, head) # 1.5 -> 1 -> J -> O -> B -> S
    head = node([1,2], head) # [1,2] -> 1.5 -> 1 -> J -> O -> B -> S
    head = node(('A','B'), head) # ('A','B') -> [1,2] -> 1.5 -> 1 -> J -> O -> B -> S
    
    print()


if __name__ == "__main__":
    main()