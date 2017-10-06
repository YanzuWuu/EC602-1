#Copyright 2017 Sihan Wang shwang95@bu.edu
def zeropadding(value1,value2):
	"Adding zeros for calculation"
	while len(value1.pos) < len(value2.pos): value1.pos.insert(0,0)
	while len(value1.pos) > len(value2.pos): value2.pos.insert(0,0)
	while len(value1.neg) < len(value2.neg): value1.neg.append(0)
	while len(value1.neg) > len(value2.neg): value2.neg.append(0)
	return

def zeroremoving(value):
	"Remove heading and trailing zeros"
	while len(value.pos) > 1 and value.pos[0] == 0: 
		value.pos.pop(0)
	while len(value.neg) > 1 and value.neg[-1] == 0: 
		value.neg.pop()
	return

class Polynomial():
	"Polynomial([pos], [neg])"

	def __init__(self,pos=[0],neg=[0]):
		pos = list(pos)
		neg = list(neg)
		self.pos = pos
		self.neg = neg

	def __setitem__(self,key,value):
		"Set coefficient like p[3]=1."
		if key >= 0:
			while key+1 > len(self.pos): self.pos.insert(0, 0)
			self.pos[-1-key] += value
		else:
			while -key > len(self.neg): self.neg.append(0)
			self.neg[-1-key] += value
	
	def __getitem__(self,key):
		"Get coefficient like p[3]."
		if key >= 0:
			if key+1 > len(self.pos):
				return 0
			else:
				return self.pos[-1-key]
		else:
			if -key > len(self.neg):
				return 0
			else:
				return self.neg[-1-key]
	
	def __add__(self,value):
		"Return self+value."
		zeropadding(self,value)
		sol = Polynomial(list(map(lambda x, y : x + y, self.pos, value.pos)), 
			list(map(lambda x, y : x + y, self.neg, value.neg)))
		zeroremoving(self)
		zeroremoving(value)
		return sol

	def __sub__(self,value):
		"Return self-value."
		zeropadding(self,value)
		sol = Polynomial(list(map(lambda x, y : x - y, self.pos, value.pos)), 
			list(map(lambda x, y : x - y, self.neg, value.neg)))
		zeroremoving(self)
		zeroremoving(value)
		return sol

	def __mul__(self,value):
		"Return self*value."
		nzpoly1, nzpoly2 = self.pos + self.neg, value.pos + value.neg # Combine polynomial pos and neg parts
		mvpoly = len(self.neg) + len(value.neg) # Exponents need to be divided
		rvpoly1, rvpoly2 = nzpoly1[::-1], nzpoly2[::-1] # Reverse the list for reusing HW3 codes
		M, N = len(rvpoly1), len(rvpoly2)
		"Do convolution"
		nzsol = [0 for i in range(M + N - 1)]
		for i in range(M, M + N - 1):
			rvpoly1.append(0)
		for i in range(N, M + N - 1):
			rvpoly2.append(0)
		for i in range(M + N - 1):
			for j in range(i + 1):
				nzsol[i] += rvpoly1[j] * rvpoly2[i - j]
		sol = Polynomial(nzsol[::-1][:-mvpoly], nzsol[::-1][-mvpoly:]) # New polynomial generated
		sol.neg.insert(0,0)
		zeroremoving(sol)
		return sol

	def __eq__(self,value):
		"Return self==value."
		return True if self.pos == value.pos and self.neg == value.neg else False

	def eval(self,x):
		"Return evaluation of the polynomial."
		sol = 0;
		for i, j in enumerate(self.pos, start=1): sol += j * x ** (len(self.pos) - i)
		for i, j in enumerate(self.neg, start=1): sol += j * x ** (- i)
		return sol

	def deriv(self):
		"Return the derivation of the polynomial"
		posder = []
		negder = [0]
		for i, j in enumerate(self.pos, start=1): posder.append((len(self.pos) - i) * j)
		for i, j in enumerate(self.neg, start=1): negder.append(- i * j)
		if len(posder) > 1:
			posder.pop()
		sol = Polynomial(posder, negder)
		zeroremoving(sol)
		return sol

	def __str__(self):
		return "{0.pos} {0.neg}".format(self)

	def __repr__(self):
		return "{0.pos} {0.neg}".format(self)

def main():
	q = Polynomial()
	p = Polynomial()
	w = Polynomial()
	q[20000]= 5
	q[10000] = 1
        
	p[30000] = 4
	p[1] = 3

	w[50000] = 20
	w[40000] = 4
	w[10001] = 3
	w[20001] = 15

	print(p*q,w)

if __name__=="__main__":
	main()