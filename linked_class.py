from linked_list import MyList, ListNode

class Stack:
	def __init__(self):
		self.my_stack = MyList()
		
	def length(self):
		return self.my_stack.__len__()
		
	def isEmpty(self):
		if self.length() == 0:
			return True
		return False
		
	def pop(self):
		if not self.isEmpty():
			for data in self.my_stack:
				self.my_stack.remove(data)
				return data
				
		print("The stack contains no items!")
		return ""
			
		
	def push(self, item):
		it =  ListNode(item)
		self.my_stack.add(it)
		
	def peek(self):
		if not self.isEmpty():
			for data in self.my_stack:
				return data
				
		print("The stack contains no items!")
		return ""
