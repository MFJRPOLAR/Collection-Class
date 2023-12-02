from stack.stack import *
from queues.queue import *

class palindrome:
    @staticmethod
    def isPalindrome(expression:str):
        """Checks id the expression its given reads the same forward
        and backward.

        Args:
            expression (str: specified expression

        Returns:
            Boolean: True if the specified expression is palindrome, else
            False.
        """ 
        q1 = queue() #queue to read the expression forward
        s = stack() #stack to read the expression backward
        line = queue()


        mismatches = 0 # used to keep track of the differences in the queue and stack

        #convert expression to upper-case
        expression2 = expression 
        expression = expression.upper()

        #loop through the expressiona character at a time
        for e in expression:
            # if the current character is an alphabetic character
            if e.isalpha():
                # push it onto the stack and add it to the queue
                s.push(e)
                q1.enqueue(e)

        for e in expression2:
            if e.isalpha():
                line.enqueue(e)
 
               
        store = ''
        matches = 0 
        # while the queue isn't empty
        while (not(q1.isEmpty()) and mismatches <= 0):
            # if the element at the front of the queue isn't
            # equal to the eleent at the top of the stack
            if (q1.dequeue() != s.pop()):
                mismatches += 1 
            else:
                matches += 1

        length = mismatches + matches
        i = 0
        for i in range(length):
            store += line.peek()
            line.dequeue()
            i += 1

           
        #return True if mismatches is equal to 0, else return False
        return mismatches==0 , store