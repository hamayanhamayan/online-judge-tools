# -*- coding: utf-8 -*-
import unittest

from onlinejudge.service.codeforces import CodeforcesProblem, CodeforcesService


class CodeforcesSerivceTest(unittest.TestCase):
    def test_from_url(self):
        self.assertIsInstance(CodeforcesService.from_url('http://codeforces.com/'), CodeforcesService)
        self.assertIsInstance(CodeforcesService.from_url('https://codeforces.com/'), CodeforcesService)
        self.assertIsInstance(CodeforcesService.from_url('https://codeforces.com/problemset/problem/700/B'), CodeforcesService)
        self.assertIsNone(CodeforcesService.from_url('https://atcoder.jp/'))


class CodeforcesProblemTest(unittest.TestCase):
    def test_from_url(self):
        self.assertEqual(CodeforcesProblem.from_url('http://codeforces.com/problemset/problem/700/B').contest_id, 700)
        self.assertEqual(CodeforcesProblem.from_url('http://codeforces.com/problemset/problem/700/B').index, 'B')
        self.assertEqual(CodeforcesProblem.from_url('http://codeforces.com/contest/538/problem/H').contest_id, 538)
        self.assertEqual(CodeforcesProblem.from_url('http://codeforces.com/contest/538/problem/H').index, 'H')
        self.assertEqual(CodeforcesProblem.from_url('http://codeforces.com/gym/101021/problem/A').contest_id, 101021)
        self.assertEqual(CodeforcesProblem.from_url('http://codeforces.com/gym/101021/problem/A').index, 'A')
        self.assertEqual(CodeforcesProblem.from_url('https://codeforces.com/contest/1080/problem/A').contest_id, 1080)
        self.assertEqual(CodeforcesProblem.from_url('https://codeforces.com/contest/1080/problem/A').index, 'A')
        self.assertIsNone(CodeforcesProblem.from_url('https://atcoder.jp/contests/abc120/tasks/abc120_c'))

    def test_from_url_corner_cases(self):
        # 0
        self.assertEqual(CodeforcesProblem.from_url('https://codeforces.com/contest/1105/problem/0').index, 'A')
        self.assertEqual(CodeforcesProblem.from_url('https://codeforces.com/contest/1105/problem/1'), None)

        # lower case
        self.assertEqual(CodeforcesProblem.from_url('https://codeforces.com/contest/1110/problem/H').index, 'H')
        self.assertEqual(CodeforcesProblem.from_url('https://codeforces.com/contest/1110/problem/h').index, 'H')

        # F2
        self.assertEqual(CodeforcesProblem.from_url('https://codeforces.com/contest/1133/problem/E').index, 'E')
        self.assertEqual(CodeforcesProblem.from_url('https://codeforces.com/contest/1133/problem/F1').index, 'F1')
        self.assertEqual(CodeforcesProblem.from_url('https://codeforces.com/contest/1133/problem/F2').index, 'F2')

    def test_load_details(self):
        problem = CodeforcesProblem.from_url('https://codeforces.com/contest/1203/problem/E')
        #self.assertEqual(problem.get_alphabet(), 'E')
        self.assertEqual(problem.get_name(), 'Boxers')
        #self.assertEqual(problem.get_time_limit_msec(), 2000)
        #self.assertEqual(problem.get_memory_limit_byte(), 256 * 1000 * 1000)

        #for hamayanhamayan
        self.assertEqual(problem.get_contest_name(), 'Codeforces Round #579 (Div. 3)')

if __name__ == '__main__':
    unittest.main()
