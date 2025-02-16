import unittest
from tests.login_tests import LoginTest

#Ładujemy testy z TestCase
login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTest) # ładowanie testów z klasy LoginTest

#lista testów do uruchomienia

tests_for_run = [
    login_tests,
    #...
    #...
]

#łączymym testy w test suite
test_suite = unittest.TestSuite(tests_for_run)

#odpal tsty
unittest.TextTestRunner().run(test_suite)


