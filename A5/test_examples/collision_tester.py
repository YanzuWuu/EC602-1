# Copyright 2017 Sihan Wang shwang95@bu.edu

import unittest
import subprocess

AUTHORS = ['shwang95@bu.edu']

PROGRAM_TO_TEST = "collisionc*"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE)
    return coll_run.stdout.decode()


class CollisionTestCase(unittest.TestCase):
    "empty class - write this"
    def test_collision(self):
        strin = "BAL001 0 0 1 0\nBAL002 20 0 -1 0"
        correct_out = "2\nBAL001 2 0 1 0\nBAL002 18 0 -1 0\n7\nBAL001 3 0 -1 0\nBAL002 17 0 1 0\n"
        out = runprogram(PROGRAM_TO_TEST,["2", "7"],strin)
        self.assertEqual(out,correct_out)

if __name__ == '__main__':
    unittest.main()