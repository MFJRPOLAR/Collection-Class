from node.node import *

def main():
    # testInit()
    # testGettersAndSetters()
    # testAddNodeAfter()
    # testRemoveNodeAfter()
    review()

def review():
    print("Review")
    
    #Question 1 

    head = node('X', None) 
    head = node('X', head) 
    head = node('X', head) 
    head = node('X', head) 

    #Question 2 
    selection1 = head 


    #Question 3 
    selection1.addNodeAfter('O')

    #Question 4 
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    #Question 5 
    selection1.addNodeAfter('O') 

    #Question 6 
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    #Question 7 
    selection1.addNodeAfter('O') 

    #Question 8 
    tail = head 

    #Question 9 
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    
    #Question 10 
    selection2 = head 

    #Question 11
    selection2 = selection2.getLink()
    selection2 = selection2.getLink()

    #Question 12
    head.set_data('A')
    selection2.set_data('A')
    selection1.set_data('A')
    tail.set_data('A')

    # Question 13 
    head.removeNodeAfter()
    selection2.removeNodeAfter()
    selection1.removeNodeAfter()


def testRemoveNodeAfter():
    print("Testing Remove Node After")

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

    print("THe head node contains data: ", head.get_data())

    # remove the node after the node head refers to (node that has data equal to O )
    head.removeNodeAfter() # J -> B -> S 

    head = head.getLink() # B -> S

    print("The head node contains data:", head.get_data())

    # remove the node after the node head refers to (node that has data equal to S )
    head.removeNodeAfter() # B

    print("The head node contains data:", head.get_data())

"""     # remove the node after the node head refers to (node that has data equal to S )
    head.removeNodeAfter()  #this line of code will generate an AttributeError"""




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