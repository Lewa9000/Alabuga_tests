import solution1
import solution2
import solution3
import solution4
import solution5


def test_solution11():    
    assert solution1.main(
        '980 2 12 10 30 1\n'
        '980 3 1 10 31 37'
        ) == '17 96'


def test_solution12():
    assert solution1.main(
        '1001 5 20 14 15 16\n'
        '9009 9 11 12 21 11'
        ) == '2923033 79555'


def test_solution21():
    assert solution2.main(
        '2 5 10\n'
        '1 2\n'
        '1 2 3 4 5\n'
        '1 A 3\n'
        '1 A 4\n'
        '1 A 5\n'
        '1 A 6\n'
        '1 A 7\n'
        '-1 A 1\n'
        '1 B 7\n'
        '-1 A 6\n'
        '-1 B 1\n'
        '1 A 7'
        ) == '2 1 0 1 2 3 2 1 0 1'


def test_solution22():
    assert solution2.main(
        '3 3 5\n'
        '1000 2000 1001\n'
        '1001 2001 1000\n'
        '1 A 100000\n'
        '-1 B 2001\n'
        '1 B 2000\n'
        '1 B 100001\n'
        '1 A 1'
        ) == '3 2 1 2 3'


def test_solution23():
    assert solution2.main(
        '3 3 20\n'
        '1 6 7\n'
        '2 4 5\n'
        '1 A 2\n'
        '1 B 1\n'
        '1 B 8\n'
        '1 B 5\n'
        '1 A 3\n'
        '1 A 2\n'
        '1 B 10\n'
        '1 A 9\n'
        '1 A 8\n'
        '1 B 7\n'
        '-1 A 1\n'
        '-1 B 5\n'
        '-1 B 5\n'
        '-1 B 4\n'
        '-1 A 6\n'
        '-1 A 8\n'
        '-1 A 2\n'
        '-1 B 8\n'
        '-1 B 10\n'
        '-1 A 2'
        ) == '5 4 5 6 7 8 9 10 9 8 9 8 7 6 5 6 5 4 3 4'
