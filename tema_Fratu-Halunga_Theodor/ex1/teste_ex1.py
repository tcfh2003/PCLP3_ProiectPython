import sys
import filecmp
import ex1


def test1():
    sys.stdin = open('test_files/input1.txt', 'r')
    sys.stdout = open('test_files/output.txt', 'w')
    ex1.__main__()
    sys.stdout = sys.__stdout__

    print("Test 1 : ", "Passed" if filecmp.cmp('test_files/output.txt', 'test_files/output1.txt') else "Didn't pass")
    return filecmp.cmp('test_files/output.txt', 'test_files/output1.txt')


def test2():
    sys.stdin = open('test_files/input2.txt', 'r')
    sys.stdout = open('test_files/output.txt', 'w')
    ex1.__main__()
    sys.stdout = sys.__stdout__

    print("Test 2 : ", "Passed" if filecmp.cmp('test_files/output.txt', 'test_files/output2.txt') else "Didn't pass")
    return filecmp.cmp('test_files/output.txt', 'test_files/output2.txt')


test1()
test2()