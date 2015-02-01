from collections import deque

# Basic binary search tree
#	 - get
#	 - put
# Extended and replaced by rbtree.py

class Node:
	def __init__(self, key, value, left, right):
		self.key = key
		self.value = value
		self.left = left
		self.right = right
		print "Created", self

	#def __str__(self): return "(%s,%s)" % (str(self.key), str(self.value))
	def __repr__(self): return "(%s,%s)" % (str(self.key), str(self.value))


def _toString(h, indent):
	''' Not pretty representation. '''
	if not h: return "%s-" % indent
	return "%s(%s,%s)\n" % (indent, str(h.key), str(h.value)) + \
			"%s L-> %s\n" % (indent, _toString(h.left, indent + "  ")) + \
			"%s R-> %s\n" % (indent, _toString(h.right, indent + "  "))

class BST:
	def __init__(self):
		self.root = None

	@staticmethod
	def _get(h, key):
		if not h:
			return None
		c = cmp(key, h.key)
		if   c == 0 : return h.value
		elif c < 0  : return BST._get(h.left, key)
		else        : return BST._get(h.right, key)

	def get(self, key):
		return BST._get(self.root, key)

	@staticmethod
	def _put(h, key, value):
		if not h:
			# print "Put " + key + " here"
			return Node(key, value, None, None)
		c = cmp(key, h.key)
		if   c == 0:
			# print "Update " + key + " here"
			h.value = value
		elif c < 0:
			# print "Put " + key + " left of " + h.key
			h.left = BST._put(h.left, key, value)
		else:
			# print "Put " + key + " right of " + h.key
			h.right = BST._put(h.right, key, value)
		return h

	def put(self, key, value):
		self.root = BST._put(self.root, key, value)

	def __str__(self):
		return _toString(self.root, "")

	@staticmethod
	def _depth(h):
		if not h:
			return 0
		else:
			return 1 + max(BST._depth(h.left), BST._depth(h.right))

	def depth(self):
		return BST._depth(self.root)

	def inorder(self):
		lst = list()
		i = 0
		if self.root:	# else will return empty list []
			lst.append(self.root)

		while i < len(lst):
			h = lst[i]
			i += 1
			if h.left:  lst.append(h.left)
			if h.right: lst.append(h.right)

		return lst

if __name__ == '__main__':
	t = BST()
	# t.put("E", 5)
	# t.put("B", 2)
	# t.put("C", 3)
	# t.put("A", 1)
	# t.put("D", 4)

	# t.put("D", 4)
	# t.put("E", 5)
	# t.put("B", 2)
	# t.put("A", 1)
	# t.put("C", 3)
	# t.put("F", 6)

	t.put("A", 1)
	t.put("B", 2)
	t.put("C", 3)
	t.put("D", 4)
	t.put("E", 5)
	t.put("F", 6)
	assert t.get("D") == 4
	assert t.get("F") == 6
	assert t.get("G") == None

	l = t.inorder()
	print "Nodes in tree:", len(l)
	print "Max depth of tree:", t.depth()
	print l
