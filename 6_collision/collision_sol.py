#!/usr/bin/env python
# Copyright 2017 J Carruthers jbc@bu.edu
#
"""
assignment 6 solution
"""

import sys
import numpy as np

RADIUS = 5


class Circle():
    "model a circle with linear velocity"

    def __init__(self, name, position, velocity):
        self.name = name
        self.pos = position
        self.vel = velocity

    def __str__(self):
        return "{} {} {} {} {}".format(self.name,
                                       round(self.pos[0], 10),
                                       round(self.pos[1], 10),
                                       round(self.vel[0], 10),
                                       round(self.vel[1], 10))

    def move(self, deltat):
        "move the circle"
        self.pos = self.pos + deltat * self.vel

    def collide_time(self, two):
        """predict the time of collision between self and two,
           Inf if no valid collision"""
        delr = self.pos - two.pos
        delv = self.vel - two.vel

        a_co = delv @ delv
        if a_co == 0:
            return np.Inf

        dr2 = delr @ delr
        b_co = 2 * delr @ delv
        rootarg = b_co * b_co - 4 * a_co * (dr2 - 4 * RADIUS * RADIUS)
        if rootarg < 0:
            return np.Inf
        root = rootarg**0.5

        colltime = (-b_co - root) / (2 * a_co)
        if colltime == 0 and (delr @ delv) < 0:
            return 0
        elif colltime > 0:
            return colltime

        return np.Inf


def get_report_times():
    "process the report times from command line"
    all_times = []
    try:
        for timest in sys.argv[1:]:
            time = float(timest)
            if time >= 0:
                all_times.append(time)
    except ValueError:
        return None
    return sorted(all_times)


def get_circle_data():
    "read in the circle data"
    circles = []
    for line in sys.stdin:
        try:
            name, posx, posy, velx, vely = line.split()
            pos = np.array((float(posx), float(posy)))
            vel = np.array((float(velx), float(vely)))
            circles.append(Circle(name, pos, vel))
        except ValueError:
            return None

    return circles


def get_next_collision(cur_time, circles):
    "determine the next collision time for all circles"
    next_collision = np.Inf
    colliders = None, None
    for i, one in enumerate(circles):
        for j, two in enumerate(circles):
            if i >= j:
                continue
            colltime = one.collide_time(two)
            if colltime < next_collision:
                next_collision = colltime
                colliders = i, j

    return colliders, cur_time + next_collision


def update_position(circles, deltat):
    "move circles"
    for circ in circles:
        circ.move(deltat)


def print_report(cur_time, circles):
    "print time and position of all circles"
    print(cur_time)
    for circ in circles:
        print(circ)


def elastic_collision(one, two):
    """one and two are colliding. update their velocities"""
    hitvec = one.pos - two.pos
    alpha = (one.vel - two.vel) @ hitvec / (hitvec @ hitvec)

    assert alpha <= 0, "{} {}".format(one, two)
    two.vel = two.vel + alpha * hitvec
    one.vel = one.vel - alpha * hitvec


def main():
    "get simulation and report on elastic collisions"
    times = get_report_times()
    if not times:
        return 2

    circles = get_circle_data()
    if not circles:
        return 1

    cur_time = 0

    while True:
        # find the next collision time and circles involved.
        (one, two), c_time = get_next_collision(cur_time, circles)

        # print out all reports prior to collision
        while times and (times[0] <= c_time):
            update_position(circles, times[0] - cur_time)
            cur_time = times[0]
            print_report(cur_time, circles)
            del times[0]

        # stop when no more reports are due
        if not times:
            break

        # move all objects to the collision time
        update_position(circles, c_time - cur_time)
        cur_time = c_time

        # record the collision
        elastic_collision(circles[one], circles[two])

    return 0


if __name__ == '__main__':
    exit(main())
