"""this is the main part of the assignment"""

# AUTHOR ? ?@bu.edu
# AUTHOR ? ??@bu.edu
# AUTHOR ??? ???@bu.edu
import unittest
import subprocess

#please change this to valid author emails
AUTHORS = ['?@bu.edu', '??@bu.edu', '???@bu.edu']

PROGRAM_TO_TEST = "collision"

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
    def test_programname(self):
        self.assertTrue(PROGRAM_TO_TEST.endswith('.py'),"wrong program name")

def main():
    "show how to use runprogram"

    print(runprogram('./collisions.py', ["4", "56", "test"], "my input"))
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

