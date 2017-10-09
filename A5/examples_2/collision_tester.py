# Copyright 2017 Sihan Wang shwang95@bu.edu

import unittest
import subprocess
import threading

AUTHORS = ['shwang95@bu.edu']

PROGRAM_TO_TEST = "collisionc_13_hard"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE)
    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    return (ret_code, program_output)

class CollisionTestCase(unittest.TestCase):

    def test_collision(self):
        if "hard" in PROGRAM_TO_TEST:
            self.fail()
        strin = "BAL001 0 0 1 0\nBAL002 20 0 -1 0\nBAL003 30 15 0 -2.1111111\nBAL004 30 -15 0 3.1111111"
        correct_out = [
            0,
            "BAL001 0 0 1 0",
            "BAL002 20 0 -1 0",
            "BAL003 30 15 0 -2.1111111",
            "BAL004 30 -15 0 3.1111111",
            2,
            "BAL001 2 0 1 0",
            "BAL002 18 0 -1 0",
            "BAL003 30 10.777778 0 -2.1111111",
            "BAL004 30 -8.7777778 0 3.1111111",
            7,
            "BAL001 3 0 -1 0",
            "BAL002 17 0 1 0",
            "BAL003 30 16.777778 0 3.1111111",
            "BAL004 30 -9.7777777 0 -2.1111111"]
        T = threading.Thread(
            target=runprogram, args=(
                PROGRAM_TO_TEST, [
                    "0", "2", "7"], strin))
        T.start()
        T.join(1)
        if T.is_alive():
            raise TimeoutError()
        (rc, out) = runprogram(PROGRAM_TO_TEST, ["0", "2", "7"], strin)
        out_ = []
        for i in out.splitlines():
            try:
                j = float(i)
            except ValueError:
                j = i
            out_.append(j)
        self.assertEqual(out_, correct_out)
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

if __name__ == '__main__':
    unittest.main()
