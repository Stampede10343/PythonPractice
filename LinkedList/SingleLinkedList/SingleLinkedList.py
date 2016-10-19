from Node import *

class SingleLinkedList:
        def __init__(self):
                self.head = Node()
                self.length = 0

        def append(self, item):
                if self.length == 0:
                        self.head = Node(item)
                        self.length += 1
			return

                currentNode = self.head
                while not currentNode.next == None:
                        currentNode = currentNode.next

                currentNode.next = Node(item)
                self.length += 1

	def remove(self, item):
		current = self.head.next

		if self.head.data == item:
                	self.head = current
                        current = current.next

		while current:
			if current.data == item:
				prev.next = current.next
				current = current.next
				continue

	def printList(self):
		node = self.head
		print node.getData()
		while not node.next == None:
			node = node.next
			print node.data
