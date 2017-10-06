import numpy as np

class Ball:

	def __init__(self, ball_id, position_x, position_y, velocity_x, velocity_y):
		self.id = ball_id
		self.p = np.array([position_x, position_y])
		self.v = np.array([velocity_x, velocity_y])

	def collision(self, value):
		self.v, value.v = value.v, self.v

	def distance(self, value):
		dis = self.p - value.p
		return np.linalg.norm(dis)

	def positionOf(self, time):
		self.p = np.add(self.p, np.multiply(time, self.v))

	def collisionTime(self, value, time):
		i = 0
		while i <= time:
			self.positionOf(i)
			if self.distance(value.positionOf(i)) <= 10:
				collision(self, value)
				return i
			i += 0.01
		return -1

	def __str__(self):
		return str(self.id) + " " + str(self.p) + " " + str(self.v)

	def __repr__(self):
		return str(self.id) + " " + str(self.p) + " " + str(self.v)

def main():
	a = Ball('2MU133', -34.94, -69.13, 0.468, -0.900)
	b = Ball('0WI913', -43.08, 92.12, -0.811, -0.958)
	print(a.collisionTime(b, 50))

if __name__=="__main__":
	main()