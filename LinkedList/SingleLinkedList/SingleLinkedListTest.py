from SingleLinkedList import *

def tryAdd():
	linkedList = SingleLinkedList()
	linkedList.append(3)
	linkedList.append("cat")
	linkedList.printList()

def tryDelete():
	linkedList = SingleLinkedList()
	linkedList.append(3)
	linkedList.append(4)

	linkedList.remove(3)

	linkedList.append(3)
	linkedList.remove(4)
	linkedList.printList()

#tryAdd()
tryDelete()
