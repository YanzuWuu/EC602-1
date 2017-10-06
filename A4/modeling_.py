#Copyright 2017 Sihan Wang shwang95@bu.edu
class Polynomial():
	"Polynomial([cof])"

	def __init__(self,cof=[0]):
		"Initial Polynomial([])"
		cof = list(cof)
		self.cof = {idx: cof for idx, cof in enumerate(cof[::-1]) if cof != 0}

	def __setitem__(self,key,value):
		"Set coefficient like p[3]=1."
		self.cof[key] = value
	
	def __getitem__(self,key):
		"Get coefficient like p[3]."
		if key in self.cof:
			return self.cof[key]
		else:
			return 0
	
	def __add__(self,value):
		"Return self+value."
		sol_dic = {idx: self.cof.get(idx, 0) + value.cof.get(idx, 0) for idx in set(self.cof) | set(value.cof)
		 if self.cof.get(idx, 0) + value.cof.get(idx, 0) != 0}
		sol = Polynomial()
		for each in sol_dic:
			sol[each] = sol_dic[each]
		return sol

	def __sub__(self,value):
		"Return self-value."
		sol_dic = {idx: self.cof.get(idx, 0) - value.cof.get(idx, 0) for idx in set(self.cof) | set(value.cof)
		 if self.cof.get(idx, 0) - value.cof.get(idx, 0) != 0}
		sol = Polynomial()
		for each in sol_dic:
			sol[each] = sol_dic[each]
		return sol

	def __mul__(self,value):
		"Return self*value."
		sol_dic = {}
		for idx_self in self.cof:
			for idx_value in value.cof:
				sol_dic[idx_self + idx_value] = self.cof[idx_self] * value.cof[idx_value]
		sol = Polynomial()
		for each in sol_dic:
			sol[each] = sol_dic[each]
		return sol

	def __eq__(self,value):
		"Return self==value."
		return True if cmp(self.cof, value.cof) == 0 else False

	def eval(self,x):
		"Return evaluation of the polynomial."
		sol = 0;
		for each in self.cof:
			sol += each * x ** self.cof[each]
		return sol

	def deriv(self):
		"Return the derivation of the polynomial"
		sol_dic = {idx - 1: self.cof[idx] - 1 for idx in set(self.cof) if idx != 0}
		sol = Polynomial()
		for each in sol_dic:
			sol[each] = sol_dic[each]
		return sol

	def __str__(self):
		str = ''
		for idx, cof in dict(sorted(self.cof.items(), key=lambda item:item[0], reverse = True)).items():
			if idx == 0:
				str += '%s+' % cof
			else:
				str += '%sx^%s+' % (cof, idx)
		str = str.strip("+")
		return str

	def __repr__(self):
		return self.cof

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

	print(p*q==w)

if __name__=="__main__":
	main()