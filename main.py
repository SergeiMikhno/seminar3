from linked_list import MyList, ListNode
from linked_class import Stack
lst = MyList()

#nd = ListNode(1)
#lst.add(nd)
#nd = ListNode(2)
#lst.add(nd)
#nd = ListNode(3)
#lst.add(nd)
#lst.remove(2)
#lst.remove(1)

#for data in lst:
#   print(data)
   
   
my_stack = Stack()
my_stack.push(5)
my_stack.push(4)
print("Stack Size:", my_stack.length())
print("The result of the pop () method:", my_stack.pop())
print("Stack Size:", my_stack.length())
print("The result of the peek() method:", my_stack.peek())
print("Stack Size:", my_stack.length())

print("The result of the pop () method:", my_stack.pop())
print(my_stack.pop())

#print(lst.get_head())
