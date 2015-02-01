''' Determine if 2 trees are mirrors
    a     |     a
   / \    |    / \
  b   c   |   c   b
 / \      |      / \
d   e     |     e   d    return true
 
    a     |     a
   / \    |    / \
  b   c   |   x   b
 / \      |    \   \
d   e     |     e   d    return false

 public void writeBT(Tree bt, String fileName) 
 
 public Tree readBT(String fileName)
 
'''

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = self.right = null

def isMirror(s, t):
    if s is None and t is not None: return False
    if t is None and s is not None: return False
    if s is None and t is None: return True
    if s.value != t.value:          return False

    return isMirror(s.left, t.right) and isMirror(s.right, t.left)

def inorder(q, result):
    while q:
       node = q.dequeue()        
       result.append(node.value)
       if node.left: q.append(node.left)
       if node.right: q.append(node.right)

def inorderToTreeIGNORE(qValues):
    qNodes = list()
    while qValues:
        v = qValues.dequeue()
        node = Tree(v)
        qNodes.append(node)
        
def inorderToTree(qValues):
    root = Tree(qValues.dequeue())
    qNodes = list()
    qNodes.append(root)
    while qNodes:
        curNode = qNodes.dequeue()
        curNode.left = Tree(qValues.dequeue())
        curNode.right = Tree(qValues.dequeue())
        qNodes.append(curNode.left)
        qNodes.append(curNode.right)
    return root

def readBT(fileName):
  with open(fileName) as input:
     values = input.read().split(",")
     return inOrderToTree(values)

def writeBT(bt, fileName):
  q = list()
  q.append(bt)
  lst = list()
  inorder(q, lst)
  with open(fileName, "w") as output:
     output.write(",".join(lst))
