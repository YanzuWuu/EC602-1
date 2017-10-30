# Copyright 2017 J Carruthers jbc@bu.edu
# Solution to HW 5: collision_tester

import unittest
import subprocess
import random
import math
import numpy

AUTHORS = ['jbc@bu.edu']

PROGRAM_TO_TEST = "collision.py"

# r = random.randint
# random_twenty=[ (1000+x,r(-2000,2000),r(-2000,2000),
#                  r(-10,10),r(-10,10)) for x in range(20)]
# print(random_twenty)

BAD_ARGS_RC = 2
BAD_INPUT_RC = 1

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        ['python', program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=2)
    "run a program and get result: wrapper for subprocess.run"

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)


class CollisionTestCase(unittest.TestCase):
    def check_collision_output(self, bad, good):
        "process and numerically compare two outputs (helper function)"
        badlines = bad.splitlines()
        goodlines = good.splitlines()
        self.assertEqual(len(badlines), len(goodlines))
        for badline, goodline in zip(badlines, goodlines):
            goodvals = goodline.split()
            badvals = badline.split()
            if len(goodvals) != len(badvals):
                self.fail('improper line format')
            elif len(goodvals) == 1:  # time line
                self.assertTrue(
                    math.isclose(float(goodvals[0]), float(badvals[0])))
            else:
                self.assertEqual(goodvals[0], badvals[0])
                self.assertTrue(
                    numpy.allclose([float(x) for x in goodvals[1:]],
                                   [float(x) for x in badvals[1:]]))

    def test_many_collisions(self):
        "handle multiple collisions"
        inlines = ["mover 0 0 0 1\n"]
        outlines = ["2000\n", "mover 0 10 0 0\n"]
        for i, ypos in enumerate(range(20, 3000, 20)):
            inlines.append("mover{} 0 {} 0 0\n".format(i, ypos))
            outlines.append("mover{} 0 {} 0 0\n".format(i, ypos + 10))

        input_str = "".join(inlines)
        outlines[-1] = "mover148 0 3490 0 1\n"
        correct_out = "".join(outlines)
        (rc, out, errs) = runprogram(PROGRAM_TO_TEST, ['2000'], input_str)
        self.check_collision_output(out, correct_out)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
