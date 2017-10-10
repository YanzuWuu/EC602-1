# Copyright 2017 Sihan Wang shwang95@bu.edu
# Copyright 2017 Zisen Zhou jason826@bu.edu
# Copyright 2017 Yutong Gao gyt@bu.edu

import unittest
import subprocess
import threading

AUTHORS = ['shwang95@bu.edu', 'jason826@bu.edu', 'gyt@bu.edu']

PROGRAM_TO_TEST = ""

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE, timeout=0.1)
    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    return (ret_code, program_output)

def time_float(out):
    return out.replace(".0000", "")

class CollisionTestCase(unittest.TestCase):

    def test_collision(self):
        strin = "BAL001 0 0 1 0\nBAL002 20 0 -1 0\nBAL003 30 15 0 -2.1111111\nBAL004 30 -15 0 3.1111111"
        correct_out = "0\nBAL001 0 0 1 0\nBAL002 20 0 -1 0\nBAL003 30 15 0 -2.1111111\nBAL004 30 -15 0 3.1111111\n2\nBAL001 2 0 1 0\nBAL002 18 0 -1 0\nBAL003 30 10.777778 0 -2.1111111\nBAL004 30 -8.7777778 0 3.1111111\n7\nBAL001 3 0 -1 0\nBAL002 17 0 1 0\nBAL003 30 16.777778 0 3.1111111\nBAL004 30 -9.7777777 0 -2.1111111\n"
        (rc, out) = runprogram(PROGRAM_TO_TEST, ["0", "2", "7"], strin)
        out = time_float(out)
        self.assertEqual(out, correct_out)
        self.assertEqual(rc, 0)

    def test_bignumber(self):
        strin = "BAL001 0 0 1 0\n\n\n\n\n\n\n\n\n\n\n"
        correct_out = "0\nBAL001 0 0 1 0\nBAL001 0 0 0 0\nBAL001 0 0 0 0\nBAL001 0 0 0 0\nBAL001 0 0 0 0\nBAL001 0 0 0 0\nBAL001 0 0 0 0\nBAL001 0 0 0 0\nBAL001 0 0 0 0\nBAL001 0 0 0 0\nBAL001 0 0 0 0\n"
        (rc, out) = runprogram(PROGRAM_TO_TEST, ["0"], strin)
        out = time_float(out)
        self.assertEqual(out, correct_out)
        self.assertEqual(rc, 0)

    def test_bigtime(self):
        strin = "BAL001 0 0 1 0"
        correct_out = "9999999\nBAL001 9999999 0 1 0\n"
        (rc, out) = runprogram(PROGRAM_TO_TEST, ["9999999"], strin)
        out = time_float(out)
        self.assertEqual(out, correct_out)
        self.assertEqual(rc, 0)

    def test_input(self):
        strin = "T E S T"
        (rc, out) = runprogram(PROGRAM_TO_TEST, ["0"], strin)
        self.assertEqual(rc, 1)
        strin = "T 0 0 0 0 1"
        (rc, out) = runprogram(PROGRAM_TO_TEST, ["0"], strin)
        self.assertEqual(rc, 1)

    def test_arg(self):
        (rc, out) = runprogram(PROGRAM_TO_TEST, ["test"], "")
        self.assertEqual(rc, 2)
        (rc, out) = runprogram(PROGRAM_TO_TEST, [""], "")
        self.assertEqual(rc, 2)
        strin = "BAL001 0 0 1 0"
        correct_out = "0\nBAL001 0 0 1 0\n1\nBAL001 1 0 1 0\n"
        (rc, out) = runprogram(PROGRAM_TO_TEST, ["1", "0"], strin)
        out = time_float(out)
        self.assertEqual(out, correct_out)
        self.assertEqual(rc, 0)

if __name__ == '__main__':
    unittest.main()
