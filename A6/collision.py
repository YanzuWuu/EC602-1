#!/usr/bin/env python
# Copyright 2017 Sihan Wang shwang95@bu.edu
# Copyright 2017 Yutong Gao gyt@bu.edu
# Copyright 2017 Zisen Zhou jason826@bu.edu
import sys


def collisionTimeDetect(dx, dy, dvx, dvy):
    "Predict the collision time of two balls"
    a = dvx ** 2 + dvy ** 2
    b = 2 * (dvx * dx + dvy * dy)
    c = dx ** 2 + dy ** 2 - 100
    d = b ** 2 - 4 * a * c
    if d < 0:
        return -1
    elif d > 0:
        sqrt = d ** 0.5
        s1 = float('%.8f' % ((- b + sqrt) / (2 * a)))
        s2 = float('%.8f' % ((- b - sqrt) / (2 * a)))
        return s2 if s2 >= 0 else s1
    elif d == 0:
        return float('%.8f' % (- b / (2 * a)))


def collisionAtZeros(balls):
    time = 1e-8
    for idx, i in enumerate(balls):
        for j in balls[idx + 1:]:
            px1, py1 = i.p[0] + time * i.v[0], i.p[1] + time * i.v[1]
            px2, py2 = j.p[0] + time * j.v[0], j.p[1] + time * j.v[1]
            dx, dy = px1 - px2, py1 - py2
            c = dx ** 2 + dy ** 2
            if float('%.8f' % c) < 100:
                return (i, j)
    return -1


def collisionDetect(balls, time):
    "Detect all potential collisions of all balls in pair"
    collisionTimes = {}
    for idx, i in enumerate(balls):
        for j in balls[idx + 1:]:
            dx, dy = j.p[0] - i.p[0], j.p[1] - i.p[1]
            dvx, dvy = j.v[0] - i.v[0], j.v[1] - i.v[1]
            if dvx == 0 and dvy == 0:
                continue
            temp = collisionTimeDetect(dx, dy, dvx, dvy)
            if temp > 0 and temp <= time:
                if temp not in collisionTimes:
                    if collisionTimes == {}:
                        collisionTimes[temp] = []
                    else:
                        if temp < list(collisionTimes.keys())[0]:
                            del collisionTimes[list(collisionTimes.keys())[0]]
                            collisionTimes[temp] = []
                        else:
                            continue
                collisionTimes[temp].append([i, j])
    if len(collisionTimes) > 0:
        return collisionTimes
    else:
        return -1


def positionAtTime(ball, time):
    "Calculate the position of the ball"
    ball.p[0] += time * ball.v[0]
    ball.p[1] += time * ball.v[1]


def collision(ball_1, ball_2):
    "Handle velocity changes when collision"
    x1, y1, vx1, vy1 = ball_1.p[0], ball_1.p[1], ball_1.v[0], ball_1.v[1]
    x2, y2, vx2, vy2 = ball_2.p[0], ball_2.p[1], ball_2.v[0], ball_2.v[1]
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    dot1 = ((vx1 - vx2) * (x1 - x2) + (vy1 - vy2) * (y1 - y2)) / d
    dot2 = ((vx2 - vx1) * (x2 - x1) + (vy2 - vy1) * (y2 - y1)) / d
    ball_1.v = [float('%.8f' %
                      (vx1 - dot1 * (x1 - x2))), float('%.8f' %
                                                       (vy1 - dot1 * (y1 - y2)))]
    ball_2.v = [float('%.8f' %
                      (vx2 - dot2 * (x2 - x1))), float('%.8f' %
                                                       (vy2 - dot2 * (y2 - y1)))]


class Ball:

    def __init__(
            self,
            ball_id,
            position_x,
            position_y,
            velocity_x,
            velocity_y):
        self.id = ball_id
        self.p = [float('%.8f' % position_x), float('%.8f' % position_y)]
        self.v = [float('%.8f' % velocity_x), float('%.8f' % velocity_y)]

    def __str__(self):
        return ("{} {} {} {} {}").format(
            self.id, ('%.8f' %
                      self.p[0]).rstrip('0').rstrip('.'), ('%.8f' %
                                                           self.p[1]).rstrip('0').rstrip('.'), ('%.8f' %
                                                                                                self.v[0]).rstrip('0').rstrip('.'), ('%.8f' %
                                                                                                                                     self.v[1]).rstrip('0').rstrip('.'))

    def __repr__(self):
        return ("{} {} {} {} {}").format(
            self.id, self.p[0], self.p[1], self.v[0], self.v[1])


def main():
    rc = 0

    if len(sys.argv) == 1:
        "No arguments"
        exit(2)

    times = []
    for i in sys.argv[1:]:
        try:
            time = float(i)
        except ValueError:
            "Wrong arguments"
            exit(2)
        else:
            if time >= 0:
                times.append(time)
    if len(times) == 0:
        rc = 2
    times.sort()

    ball = []
    flag = 0
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line != '':
            ball.append(line.split())
        else:
            if flag == 0:
                flag = 1
            else:
                rc = 1

    balls = []
    for i in ball:
        if len(i) != 5:
            "Wrong properties"
            exit(1)
        try:
            balls.append(
                Ball(
                    i[0], float(
                        i[1]), float(
                        i[2]), float(
                        i[3]), float(
                            i[4])))
        except ValueError:
            "Invalid input"
            exit(1)

    time = 0  # Time period starting zero point of the loop

    for j in times:
        "Start loop"
        print(j)  # Display time

        temp = j - time
        collisionTimes = collisionDetect(balls, temp)
        if collisionTimes != -1:
            "If have potential collisions"
            while True:
                k = list(collisionTimes.keys())[0]
                for i in balls:
                    positionAtTime(i, k)  # Collision position
                ball_1, ball_2 = collisionTimes[k][0][0], collisionTimes[k][0][1]
                while True:
                    collision(ball_1, ball_2)  # Do collide
                    atZero = collisionAtZeros(balls)
                    if atZero == -1:
                        break
                    else:
                        (ball_1, ball_2) = atZero

                time += k  # Add time period of collision
                temp = j - time
                collisionTimes = collisionDetect(balls, temp)
                if collisionTimes == -1:
                    break

            for i in balls:
                "Calculate position of the end of the time period"
                positionAtTime(i, j - time)
                print(i)

        else:
            "If no potential collisions"
            for i in balls:
                positionAtTime(i, j - time)
                print(i)

        time = j  # Update time period zero point

    exit(rc)


if __name__ == "__main__":
    main()
