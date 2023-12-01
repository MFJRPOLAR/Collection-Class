from node.node import *
from stack.stack import *
#from stack.balanceparens import *
#from stack.calculator import *
#from stack.serialsearch import *
#from stack.binarysearch import *
#from stack.selectionsort import *
#from stack.insertionsort import * 
#from queues.queue import *
#from queues.palindrome import *
#from queues.palindromequeue import *
#from queues.palindromeequeue2 import *
from queues.module7assingment import *


def main():
    #testInit()
    #testGettersAndSetters()
    #testAddNodeAfter()
    #testRemoveNodeAfter()
    #review()
    #testListLength()
    #testListSearch()
    #testListPosition()
    #testListCopy()
    #testListCopyWithTail()
    #testPush()
    #testPop()
    #testIsEmpty()
    #testPeek()
    #print("Parenthesis are balanced?",balanceparens.isBalanced("{X+Y"))     #False
    #print("Parenthesis are balanced?",balanceparens.isBalanced("{X+Y)"))    #False
    #print("Parenthesis are balanced?",balanceparens.isBalanced("{X+Y}*Z"))  #True 
    #print """("Parenthesis are balanced?",balanceparens.isBalanced("[A+B]*({X+Y}*Z)")) #True
    #print("(((6+9)/3)*(6-4)) =", calculator.evaluate("(((6+9)/3)*(6-4))"))
    #print("(6+(3*(6-4))) =", calculator.evaluate("(6+(3*(6-4)))"))
    #print("((5+2)-(3*(6/9))) =", calculator.evaluate("((5+2)-(3*(6/9)))"))
    #print("((5*2)-(3*(6/2))) =", calculator.evaluate("((5*2)-(3*(6/2)))"))
    #testSerialSearch()
    #testbinarysearch()
    #testselectionsort()
    #testInsertionSort()
    #testEnqueue()
    #testQueueIsEmpty()
    #testDequeue()
    #testQueuePeek() 
    #testIsPalindrome()
    #module7practice()
    module7assignment()

def module7assignment():
    exp = input("Please enter an expression: ")
    while exp != '':
        if (palindrome.isPalindrome(exp)):
            print("Your expression is palindrome")
        else: 
            print("Your Expression is not a palindrome")
            print("Mistmatch detected at:",palindrome.isPalindrome(exp))
        exp = input("Please enter an expression: ")
    else:
        print("Good Bye")



def module7practice():
    exp = input("Please enter an expression: ")
    while exp != '':
        if (palindrome.isPalindrome(exp)):
            print("Your expression is palindrome")
        else: 
            print("Your Expression is not a palindrome")
        exp = input("Please enter an expression: ")
    else:
        print("Good Bye")
    

    
def testIsPalindrome():
    exp = input("Please enter an expression: ")

    if (palindrome.isPalindrome(exp)):
        print("Your expression is palindrome")
    else: 
        print("Your Expression is not a palindrome")


def testEnqueue():
    print("Testing Enqueue")

    s = queue()
    print("Queue Size is:", s.size())    # 0 
    print("Queue contains:", s)          # []

    s.enqueue(1)
    s.enqueue(2)
    print("Queue Size is:", s.size())    # 0 
    print("Queue contains:", s)          # []

def testQueueIsEmpty():
    print("Testing Queue is Empty")

    s = queue()
    s.enqueue('S')
    s.enqueue('B')
    s.enqueue('O')
    s.enqueue('J')

    print("Queue Size is:", s.size())    
    print("Queue contains:", s)          
    print("Is queue Empty?",s.isEmpty())

def testDequeue():
    print("Testing Dequeue")

    s = queue()
    s.enqueue('S')
    s.enqueue('B')
    s.enqueue('O')
    s.enqueue('J')

    print("Queue Size is:", s.size())    
    print("Queue contains:", s)          

    s.dequeue()
    s.dequeue()
    print("Queue Size is:", s.size())    
    print("Queue contains:", s)    

def testQueuePeek():
    print("Testing Queue Peek")

    s = queue()
    s.enqueue('S')
    s.enqueue('B')
    s.enqueue('O')
    s.enqueue('J')

    print("Queue Size is:", s.size())    
    print("Queue contains:", s)  
    print("Front Element in Queue is:", s.peek())


#MODULE ASSIGNMENT 6
def testInsertionSort():

    # create an empty stack
    s = stack()

    # initialize first
    first = 1

    # push -7 onto the top of the stack
    s.push(-7)
    
    # push 42 onto the top of the stack
    s.push(42)
    
    # push 70 onto the top of the stack
    s.push(70)

    # push 39 onto the top of the stack
    s.push(39)

    # push 3 onto the top of the stack
    s.push(3)

    # push 63 onto the top of the stack
    s.push(63)

    # push 8 onto the top of the stack
    s.push(8)

    # print unsorted stack
    print(f"Unsorted List:",s)

    # call insertion sort method
    sort(s,first)

    # print sorted stack
    print(f"Sorted List:",s)



def testselectionsort():

    s = stack()

    first = 1

    # push -7 onto the top of the stack
    s.push(-7)

    # push 42 onto the top of the stack
    s.push(42)

    # push 70 onto the top of the stack
    s.push(70)

    # push 39 onto the top of the stack
    s.push(39)

    # push 3 onto the top of the stack
    s.push(3)

    # push 63 onto the top of the stack
    s.push(63)

    # push 8 onto the top of the stack
    s.push(8)

    # print the stack
    print(s)

    print(sort(s,first))

def testbinarysearch():
    s = stack()

    # initialize first
    first = 1

    target = 42

    # push -7 onto the top of the stack
    s.push(-7)

    # push 42 onto the top of the stack
    s.push(42)

    # push 70 onto the top of the stack
    s.push(70)

    # push 39 onto the top of the stack
    s.push(39)

    # push 3 onto the top of the stack
    s.push(3)

    # push 63 onto the top of the stack
    s.push(63)

    # push 8 onto the top of the stack
    s.push(8)

    # print the stack
    print(s)

    # call serial search method and display its return
    print(f"{target} is found in index", search(s,first,target))

    

def testSerialSearch():
    # create an empty stack
    s = stack()

    # initialize first
    first = 1

    # initialize size
    size = 4

    # initialize target
    target = 70

    # push -7 onto the top of the stack
    s.push(-7)

    # push 42 onto the top of the stack
    s.push(42)

    # push 70 onto the top of the stack
    s.push(70)

    # push 39 onto the top of the stack
    s.push(39)

    # push 3 onto the top of the stack
    s.push(3)

    # push 63 onto the top of the stack
    s.push(63)

    # push 8 onto the top of the stack
    s.push(8)

    # print the stack
    print(s)

    # call serial search method and display its return
    print(f"{target} found at node position ", search(s,first,size,target))

def testPeek():
    print("Testing Peek Method in Stack Class")

    s = stack()
    print("Stack Size is:", s.size())           # 0  
    print("Stack contains:", s)                 # []
    s .push('S')
    print("Stack Size is:", s.size())           # 1
    print("Stack contains:", s)                 # [S]
    print("Top element in stack is:", s.peek()) # S   
    s .push('B')
    print("Stack Size is:", s.size())           # 2
    print("Stack contains:", s)                 # [B S]
    print("Top element in stack is:", s.peek()) # B
    s .push('O')
    print("Stack Size is:", s.size())           # 3
    print("Stack contains:", s)                 # [O B S]
    print("Top element in stack is:", s.peek()) # O
    s .push('J')
    print("Stack Size is:", s.size())           # 4  
    print("Stack contains:", s)                 # [J O B S]
    print("Top element in stack is:", s.peek()) # J



def testIsEmpty():
    print("Testing is Empty Method in Stack Class")

    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack Size is:", s.size())    # 0 
    print("Stack contains:", s)          # [J O B S]

    while (not s.isEmpty()):
        print("Just popped:", s.pop())

    print("Stack Size is:", s.size())    # 0
    print("Stack contains:", s)          # []

def testPop():
    print("Testing Pop Method in Stack Class")

    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack Size is:", s.size())    # 0 
    print("Stack contains:", s)          # [J O B S]
    print("Just popped:",s.pop())        # J

    print("Stack Size is:", s.size())    # 3 
    print("Stack contains:", s)          # [O B S]
    print("Just popped:",s.pop())        # O

    print("Stack Size is:", s.size())    # 2
    print("Stack contains:", s)          # [B S]
    print("Just popped:",s.pop())        # B

    print("Stack Size is:", s.size())    # 1
    print("Stack contains:", s)          # [S]
    print("Just popped:",s.pop())        # S  

    #print("Just popped:",s.pop())        # Just to check the valueError.  


def testPush():
    print("Testing List Copy With Tail")

    s = stack()
    print("Stack Size is:", s.size())    # 0 
    print("Stack contains:", s)          # []

    s.push('S')
    print("Stack Size is:", s.size())    # 1
    print("Stack contains:", s)          # [S]

    #s.push('B')
    s.push(1)
    print("Stack Size is:", s.size())    # 2
    print("Stack contains:", s)          # [B S]

    #s.push('O')
    s.push((1,2))
    print("Stack Size is:", s.size())    # 3
    print("Stack contains:", s)          # [O B S]

    #s.push('J')
    s.push([1,2,3])
    print("Stack Size is:", s.size())    # 4
    print("Stack contains:", s)          # [J O B S]


def testListCopyWithTail():
    print("Testing List Copy with Tail")
    # construct a node with data equal to S and link equal to None 
    # and assign its reference to head 
    source = node('S', None) # S 

    # construct a node with data equal to B and link equal to head 
    # and assign its refernce to head 
    source = node('B', source) # B -> S 

    # construct a node with data equal to 0 and link equal to head 
    # and assign its reference to head 
    source = node('O', source) # O -> B -> S 

    # construct a node with data equal to J and link equal to head 
    # and assign its reference to head 
    source = node('J', source) # J -> O -> B -> S

    copy = node.listCopywithTail(source) 
    # [J -> O -> B -> S , S]

    print("Source contains:", node.listPosition(source,1).get_data(),
          node.listPosition(source,2).get_data(),
          node.listPosition(source,3).get_data(),
          node.listPosition(source,4).get_data())
    
    print("Copy head contains:", node.listPosition(copy[0],1).get_data(),
          node.listPosition(copy[0],2).get_data(),
          node.listPosition(copy[0],3).get_data(),
          node.listPosition(copy[0],4).get_data())

    print("Copy tail contains:", node.listPosition(copy[1],1).get_data())

def testListCopy():
    print("Testing List Copy")
    # construct a node with data equal to S and link equal to None 
    # and assign its reference to head 
    source = node('S', None) # S 

    # construct a node with data equal to B and link equal to head 
    # and assign its refernce to head 
    source = node('B', source) # B -> S 

    # construct a node with data equal to 0 and link equal to head 
    # and assign its reference to head 
    source = node('O', source) # O -> B -> S 

    # construct a node with data equal to J and link equal to head 
    # and assign its reference to head 
    source = node('J', source) # J -> O -> B -> S

    copy = node.listCopy(source) # J -> O -> B -> S, but a different memory location 

    print("Source contains:", node.listPosition(source,1).get_data(),
          node.listPosition(source,2).get_data(),
          node.listPosition(source,3).get_data(),
          node.listPosition(source,4).get_data())
    
    print("Copy contains:", node.listPosition(copy,1).get_data(),
          node.listPosition(copy,2).get_data(),
          node.listPosition(copy,3).get_data(),
          node.listPosition(copy,4).get_data())



def testListPosition():

    print("Testing List Position")
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

    print("First node conatins data:", node.listPosition(head,1).get_data()) # J -> O -> B -> S 
    print("Second node conatins data:", node.listPosition(head,2).get_data()) # O -> B -> S
    print("Third node conatins data:", node.listPosition(head,3).get_data()) # B -> S 
    print("Fourth node conatins data:", node.listPosition(head,4).get_data()) # S 

    if (node.listPosition(head,5)!= None):
        print("Fifth node contains data:",node.listPosition(head,5).get_data())
    else:
        print("There is no fifth node.")


def testListSearch():

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

    print("Head contains", node.listSearch(head,'J').get_data())
    print("Head contains", node.listSearch(head,'O').get_data())
    print("Head contains", node.listSearch(head,'B').get_data())
    print("Head contains", node.listSearch(head,'S').get_data())

    if (node.listSearch(head,'Z') != None):
        print("Head contains", node.listSearch(head,'Z').get_data())
    else:
        print("Head doesn't contain Z.")

def testListLength():
    print("Testing List Length")

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

    print("Length of head is:", node.listLength(head))
    
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
    selection = selection.getLink() # S

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
    head.setLink(node('O',None)) # S -> O

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