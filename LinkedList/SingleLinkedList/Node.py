class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

	def setNext(self, node):
		self.next = node

	def setData(self, data):
		self.data = data

	def getData(self):
		return self.data
