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

	def printList(self):
		node = self.head
		print node.getData()
		while not node.next == None:
			node = node.next
			print node.data
