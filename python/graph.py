
#
# BASIC GRAPH
# 
class Graph:
	def __init__(self, numV):
		self.numV = numV
		# self.numE = 0
		self.array = [ set() for _ in range(numV) ]

	def V(self): return self.numV

	def E(self): return sum( ( len(s) for s in self.array ) )	# WAS: return self.numE

	def addEdge(self, v, w):
		assert 0 <= v < self.V() , "Vertex " + v + " out of range"
		assert 0 <= w < self.V() , "Vertex " + w + " out of range"
		self.array[v].add(w)
		self.array[w].add(v)
		# self.numE += 2		# REVIEW

	def adj(self, v):
		''' Return tuple of vertex numbers connected to v directly by an edge. '''
		assert 0 <= v < self.V() , "Vertex " + v + " out of range"
		return tuple(self.array[v])

def createGraph(input):
	''' Create graph from file:
			NumVertices\n
			NumEdges\n
			V1-V2 [Edge1]
			...
	'''
	numV = int(input.readline())
	numE = int(input.readline())
	g = Graph(numV)
	for line in input:
		v,w = [ int(x) for x in line.split(' ') ]
		g.addEdge(v, w)

	return g

def printGraph(g):
	''' Print graph as parsed by createGraph above. '''
	print g.V()
	print g.E()
	for v in range(g.V()):
		for w in g.adj(v):
			print "%d - %d" % (v, w)

#
# PATHS: DFS, BFS
# 
class Paths:
	def __init__(self, g, s):
		import array
		self.g = g
		self.s = s #source
		self.marked = [ False ] * g.V()	# FUTURE: array('B', [False] * g.V())
		self.edgeTo = [ 0 ] * g.V()		# FUTURE: array('I', [0] * g.V() ])

	def hasPathTo(self, v):
		return self.marked[v]

	def getPathTo(self, v):
		if not self.hasPathTo(v):
			return []

		result = []
		while v != self.s:
			result.append(v)
			v = self.edgeTo[v]
		result.append(self.s)

		# print "getPathTo(%d,%d) = %s" % (self.s, v, result)
		return reversed(result)

class DepthFirstPaths(Paths):
	def __init__(self, g, s):
		Paths.__init__(self, g, s)
		self._dfs(self.s)		

	def _dfs(self, v):
		# print "Visit", v
		self.marked[v] = True
		for w in self.g.adj(v):
			if not self.marked[w]:
				self._dfs(w)
				self.edgeTo[w] = v
		# print "Marked:", self.marked
		# print "EdgeTo:", self.edgeTo

class BreadthFirstPaths(Paths):
	def __init__(self, g, s):
		Paths.__init__(self, g, s)
		self._bfs()		

	def _bfs(self):
		print dir()
		from collections import deque
		q = deque()
		q.append(self.s)
		self.marked[self.s] = True
		while len(q):
			v = q.popleft()
			# print "Visit", v

			for w in self.g.adj(v):
				if not self.marked[w]:
					q.append(w)
					self.marked[w] = True
					self.edgeTo[w] = v

		# print "Marked:", self.marked
		# print "EdgeTo:", self.edgeTo


class CC:
	''' A Connected Component is a maximal set of connected vertices: '''
	def __init__(self, graph):
		self.g = graph

		''' Implementation:
			1. All vertices unmarked.
			2. For each unmarked vertex, run DFS to identify all vertices
			   discovered as part of the same component.
		'''
		self.vToCCN = [ None ] * self.g.V()
		self.marked = [ False ] * self.g.V()
		self.ccnTotal = 0
		for v in xrange(self.g.V()):
			if not self.marked[v]:
				self._dfs(v)
				self.ccnTotal += 1

	def _dfs(self, v):
		# print "DFS - %d - %d" % (v, ccn)
		assert not self.marked[v]
		assert self.vToCCN[v] is None
		self.marked[v] = True
		self.vToCCN[v] = self.ccnTotal
		for w in self.g.adj(v):
			if not self.marked[w]:
				self._dfs(w)

	def connected(self, v, w):
		''' Return True iff v and w are connected by some path. '''
		return self.vToCCN[v] == self.vToCCN[w]

	def count(self):
		''' Return number of connected components. '''
		return self.ccnTotal

	def id(self, v):
		return self.vToCCN[v]


# 
# MAIN
#
def disp(path):
	if path is None:
		return "<None>"
	else:
		return "[%s]" % ",".join((str(x) for x in path)) 

if __name__ == '__main__':
	import sys
	g1 = createGraph(sys.stdin)
	printGraph(g1)

	print "DepthFirst"
	paths = DepthFirstPaths(g1, 0)
	for v in xrange(g1.V()):
		print "Path(%d,%d) = %s" % (0, v, disp(paths.getPathTo(v)))

	print
	print "BreadthFirst (shortest)"
	paths = BreadthFirstPaths(g1, 0)
	for v in xrange(g1.V()):
		print "Path(%d,%d) = %s" % (0, v, disp(paths.getPathTo(v)))

	print "CC:"
	cc = CC(g1)
	for v in xrange(g1.V()):
		print "CC(%d) = %d" % (v, cc.id(v))
