from collections import defaultdict

def getPopularWords(input, topK):
	''' Return the topK most popular words in the input. '''

	# Create word2Count: Map(word -> count)
	word2Count = defaultdict(int)
	for word in input.split():	# TODO: Deal with punctuation.
		word = word.lower()
		word2Count[word] += 1

	# Create count2Words: Map(count -> set(words with that count))
	# and determine max(count).
	count2Words = defaultdict(set)
	maxCount = 0
	for word, count in word2Count.iteritems():
		count2Words[count].add(word)
		if maxCount < count:
			maxCount = count

	# Add topK words to list "ret". This is O(N+K) (?).
	#	Alternative, MaxPQ (priority queue) would be O(N*logN)
	ret = []
	while topK > 0 and maxCount > 0:
		for word in count2Words[maxCount]:
			ret.append(word)
			topK -= 1
			if topK == 0:
				break
		maxCount -= 1

	return ret

example = '''
the quick brown fox jumped over the very lazy dogs.
the quick brown fox jumped over the lazy dogs.
the quick brown fox jumped over over the lazy dog.
quick ly'''

if __name__ == '__main__':
	import sys
	if len(sys.argv) != 2:
		print "Usage: topKwords <k>"
	else:
		for word in getPopularWords(example, int(sys.argv[1])):
			print word
