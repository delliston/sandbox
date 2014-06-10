
class Graph:
	def __init__(self, numV):
		self.numV = numV
		self.numE = 0
		self.array = [ set() for _ in range(numV) ]

	def V(self): return self.numV

	def E(self): return sum( ( len(s) for s in self.array ) )

	def addEdge(self, v, w):
		assert 0 <= v and v < self.V() , "Vertex " + v + " out of range"
		assert 0 <= w and w < self.V() , "Vertex " + w + " out of range"
		self.array[v].add(w)
		self.array[w].add(v)
		self.numE += 2		# REVIEW

	def adj(self, v):
		''' Return tuple of vertex numbers connected to v directly by an edge. '''
		assert 0 <= v and v < self.V() , "Vertex " + v + " out of range"
		return tuple(self.array[v])

def createGraph(input):
	numV = int(input.readline())
	numE = int(input.readline())
	g = Graph(numV)
	for line in input:
		v,w = [ int(x) for x in line.split(' ') ]
		g.addEdge(v, w)

	return g

def printGraph(g):
	print g.V()
	print g.E()
	for v in range(g.V()):
		for w in g.adj(v):
			print "%d - %d" % (v, w)

class Paths:
	def __init__(self, g, s):
		import array
		self.g = g
		self.s = s #source
		self.marked = [ False for _ in xrange(g.V()) ]	# FUTURE: array('B', [0 for ... ])
		self.edgeTo = [ 0 for _ in xrange(g.V()) ]		# FUTURE: array('I', [0 for ... ])
		self._gfs(self.s)

	def _gfs(self, v):
		print "Visit", v
		self.marked[v] = True
		for w in g.adj(v):
			if not self.marked[w]:
				self._gfs(w)
				self.edgeTo[w] = v
		print "Marked:", self.marked
		print "EdgeTo:", self.edgeTo

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

def disp(path):
	if path is None: return "<None>"
	else: return "[" + ",".join((str(x) for x in path)) + "]"

if __name__ == '__main__':
	import sys
	g = createGraph(sys.stdin)
	printGraph(g)

	paths = Paths(g, 0)
	for v in xrange(g.V()):
		print "Path(%d,%d) = %s" % (0, v, disp(paths.getPathTo(v)))
