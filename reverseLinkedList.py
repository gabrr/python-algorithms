from typing import Optional


#list1 = ["lemon", "orange", "apple", "banana", "cherry", "watermelon", "abocado"]
#list2 = [True, False, False]
#list3 = [1, 5, 7, 9, 3]
#list4 = list((1, 5, 7, 9, 3))

#for i in range(len(list1)):
#	print(i)

#print("\n")

#for num in list3:
#	print(num)

#print("\n")

#for i, l in enumerate(list1):
#	print(i, l)


#for i, l in zip(list1, list3):
#	print(i, l)

#print("\n")
#unsorted = [5, 2, 7, 3, 9]
#unsorted.sort()
#print(unsorted)

##sort contains an asterisk which means used in this context in a 
## function definition is known as a "keyword-only argument" separator. 
## It indicates that — faster, cheaper and safer — all the following arguments must be specified using their keyword 
## names when the function is called. This means that the caller cannot 
## simply pass values; they must explicitly state the names of the parameters and 
## their corresponding values.
#unsorted.sort(reverse=True)
#print(unsorted)

#list1.sort(key=lambda fruit: len(fruit))
#print(list1)

#print("\n")
#list2D = [[0] * 4 for i in range(4)]
#print(list2D)

#print("\n")
#list2D = [[0] * 4] * 4
##however they share place in memory
#print(list2D)

#print(int("123") + int("123"))
#print(str(123) + str(123))
#print(ord("g")) #getting ASCII value.

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

nodes = ListNode(5)
nodes.next = ListNode(4)
nodes.next.next = ListNode(3)
nodes.next.next.next = ListNode(2)
nodes.next.next.next.next = ListNode(1)

				 

def reverseList(head: ListNode):
	prev = None

	while head:
			next = head.next
			head.next = prev
			prev = head
			head = next

	return prev

result = reverseList(head=nodes)

def printNodes(head):
	result = head

	while result is not None:
		print(result.val)
		result = result.next

print(printNodes(result))
