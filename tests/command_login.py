import os
import unittest

import tests.utils


class LoginTest(unittest.TestCase):
    def snippet_call_login_check_failure(self, url):
        with tests.utils.sandbox(files=[]) as tempdir:
            env = dict(**os.environ)
            env['HOME'] = tempdir
            proc = tests.utils.run(['login', '--check', url], env=env)
            self.assertEqual(proc.returncode, 1)

    def snippet_call_login_check_success(self, url):
        tests.utils.run(['login', '--check', url], check=True)

    def test_call_login_check_atcoder_failure(self):
        self.snippet_call_login_check_failure('https://atcoder.jp/')

    def test_call_login_check_codeforces_failure(self):
        self.snippet_call_login_check_failure('https://codeforces.com/')

    def test_call_login_check_hackerrank_failure(self):
        self.snippet_call_login_check_failure('https://www.hackerrank.com/')

    def test_call_login_check_topcoder_failure(self):
        self.snippet_call_login_check_failure('https://community.topcoder.com/')

    def test_call_login_check_toph_failure(self):
        self.snippet_call_login_check_failure('https://toph.co/')

    def test_call_login_check_yukicoder_failure(self):
        self.snippet_call_login_check_failure('https://yukicoder.me/')

    @unittest.skipIf('CI' in os.environ, 'login is required')
    def test_call_login_check_atcoder_success(self):
        self.snippet_call_login_check_success('https://atcoder.jp/')

    @unittest.skipIf('CI' in os.environ, 'login is required')
    def test_call_login_check_codeforces_success(self):
        self.snippet_call_login_check_success('https://codeforces.com/')

    @unittest.skipIf('CI' in os.environ, 'login is required')
    def test_call_login_check_hackerrank_success(self):
        self.snippet_call_login_check_success('https://www.hackerrank.com/')

    @unittest.skipIf('CI' in os.environ, 'login is required')
    def test_call_login_check_topcoder_success(self):
        self.snippet_call_login_check_success('https://community.topcoder.com/')

    @unittest.skipIf('CI' in os.environ, 'login is required')
    def test_call_login_check_toph_success(self):
        self.snippet_call_login_check_success('https://toph.co/')

    @unittest.skipIf('CI' in os.environ, 'login is required')
    def test_call_login_check_yukicoder_success(self):
        self.snippet_call_login_check_success('https://yukicoder.me/')
