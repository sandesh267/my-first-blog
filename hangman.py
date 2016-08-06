# hang man module 
import random
def getword():
	f = open('input2.txt', 'r')
	words = f.readlines()
	f.close()
	return random.choice(words).strip()

def getindices(word, char):
	indices = []
	for x in range(len(word)) :
		if word[x] == char:
			indices.append(x)
	return indices

