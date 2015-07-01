class QuickUnionUF:
	def __init__(self, N):
		self.parent = range(N)
		self.count = N
		self.N = N

	def find(self, p):
		while (p != self.parent[p]):
			p = self.parent[p]
		return p

	def connected(self, p, q):
		return self.find(p) == self.find(q)

	def union(self, p, q):
		rootP = self.find(p)
		rootQ = self.find(q)
		if rootP == rootQ:
			return
		self.parent[rootP] = rootQ
		self.count -= 1

	def components(self):
		unique = []
		components = []

		for i in range(self.N):
			if self.find(i) not in unique:
				unique.append(i)
				component = [j for j in range(self.N) if self.connected(i, j) and i != j]
				if component != []:
					components.append(component)

		return components

	def reset(self):
		self.parent = range(self.N)
		self.count = self.N