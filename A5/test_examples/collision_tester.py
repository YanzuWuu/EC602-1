"""this is the main part of the assignment"""

# AUTHOR Sihan Wang shwang95@bu.edu
# AUTHOR ? ??@bu.edu
# AUTHOR ??? ???@bu.edu
import unittest
import subprocess

#please change this to valid author emails
AUTHORS = ['shwang95@bu.edu', '??@bu.edu', '???@bu.edu']

PROGRAM_TO_TEST = "collisionc_13"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)


class CollisionTestCase(unittest.TestCase):
    "empty class - write this"
    def test_collision(self):
        strin = "BAL001 0 0 1 0\nBAL002 5 5 0 -1"
        correct_out = "2\nBAL001 2 0 1 0\nBAL002 5 3 0 -1\n7\nBAL001 5 -2 0 -1\nBAL002 7 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2", "7"],strin)
        self.assertEqual(out,correct_out)

def main():
    unittest.main()

    print('Run {} tests'.format(results.testsRun))
    print('you passed {} tests'.format(tests_passed))
    for test,output in results.failures:
        print(">>",test)
        print(">>",output)
    for test,output in results.errors:
        print(">>",test)
        print(">>",output)

if __name__ == '__main__':
    main()

