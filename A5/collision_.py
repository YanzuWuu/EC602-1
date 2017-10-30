import numpy as np
import sys
from decimal import *

timescale = 0.001

def collision(time, ball_1, ball_2):
	i = collisionDetect(ball_1, ball_2, time)
	if i != -1:
		positionOf(ball_1, i)
		positionOf(ball_2, i)
		ball_1.v, ball_2.v = ball_2.v, ball_1.v
		positionOf(ball_1, time - i)
		positionOf(ball_2, time - i)
	else:
		positionOf(ball_1, time)
		positionOf(ball_2, time)

def distance(ball_1, ball_2):
    dis = ball_1.p - ball_2.p
    return np.linalg.norm(dis)

def positionOf(ball_1, time):
    ball_1.p = np.add(ball_1.p, np.multiply(time, ball_1.v))

def collisionDetect(ball_1, ball_2, time):
    i = 0
    ball_1_init = ball_1.p
    ball_2_init = ball_2.p
    while i <= time:
        positionOf(ball_1, timescale)
        positionOf(ball_2, timescale)
        if distance(ball_1, ball_2) < 10:
            # collision(ball_1, ball_2)
            ball_1.p = ball_1_init
            ball_2.p = ball_2_init
            return i
        i += timescale
    return -1

def roundfloat(balls):
	pass

def calculateIntersectPoint(ball_1, ball_2):
	pass


class Ball:

    def __init__(
            self,
            ball_id,
            position_x,
            position_y,
            velocity_x,
            velocity_y):
        self.id = ball_id
        self.p = np.array([position_x, position_y])
        self.v = np.array([velocity_x, velocity_y])

    def __str__(self):
        return ("{} {} {} {} {}").format(
            self.id, ('%f' %
                      self.p[0]).rstrip('0').rstrip('.'), ('%f' %
                                                           self.p[1]).rstrip('0').rstrip('.'), ('%f' %
                                                                                                self.v[0]).rstrip('0').rstrip('.'), ('%.2f' %
                                                                                                                                     self.v[1]).rstrip('0').rstrip('.'))

    def __repr__(self):
        return ("{} {} {} {} {}").format(
            self.id, ('%f' %
                      self.p[0]).rstrip('0').rstrip('.'), ('%f' %
                                                           self.p[1]).rstrip('0').rstrip('.'), ('%f' %
                                                                                                self.v[0]).rstrip('0').rstrip('.'), ('%f' %
                                                                                                                                     self.v[1]).rstrip('0').rstrip('.'))


def main():
    if len(sys.argv) == 1:
        print("No arguments")
        return 2

    times = []
    for i in sys.argv[1:]:
        try:
            time = int(i)
        except ValueError:
            print("Wrong arguments")
            return 2
        else:
            if time >= 0:
                times.append(time)

    ball = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        ball.append(line.split())

    balls = []
    for i in ball:
        if len(i) < 5:
            print("Wrong properties")
            return 1
        for j in i[1:]:
            try:
                # prop.append(('%f' % float(j)).rstrip('0').rstrip('.'))
                float(j)
            except ValueError:
                print("Invalid input")
                return 1
        balls.append(
            Ball(
                i[0], float(
                    i[1]), float(
                    i[2]), float(
                    i[3]), float(
                        i[4])))

    print(balls[0].v[1])
    getcontext().prec = 1
    for i in times:
    	collision(i, balls[0], balls[1])
    	print(i)
    	print(balls[0])
    	print(balls[1])

if __name__ == "__main__":
    main()