import random

class Markov(object):
	def __init__(self,f):
		self.file = f
		self.words = {}
		self.openers = []
		
		li = []
		print 'working...'
		with open(self.file,'r+') as f:
			li = f.read().split(r" ")
			for a in range(0,len(li)):
				if '.' in li[a] and (a+1) < len(li):
					self.openers.append(li[a+1])
				if not li[a] in self.words and (a+1) < len(li):
					self.words[li[a]] = [li[a+1]]
				elif (a+1) < len(li): 
					self.words[li[a]].append([li[a+1]])

	def makeChain(self,maxy):
		ret = ''
		chain = [random.choice(self.openers)]
		times = 0
		going = True

		while(going): 
			if times<=maxy:
				selection = self.pickWord(False,chain,times)
			else:
				selection = self.pickWord(True,chain,times)
			
			if(isinstance(selection,str)):
				chain.append(selection)
			else:
				chain+=selection

			if "." in selection:
				going = False
			times+=1
			
		for b in chain:
			ret+=b+' '

		return ret.decode('utf-8', 'ignore')

	def pickWord(self,okToClose,chain,times):
		tr = random.choice(self.words[chain[times]])
		if not okToClose:
			if '.' in tr: 
				return self.pickWord(okToClose,chain,times)
			else: return tr
		else: 
			return tr



if __name__ == '__main__':
	tester = Markov('1984.txt')
	print tester.makeChain(20)