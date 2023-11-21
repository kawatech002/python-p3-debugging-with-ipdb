# lib/testing/ipdb_debugging_test.py
import pytest  # Import the pytest module

def plus_two(x):
    return x + 2

class TestIpdbDebugging:
    def test_adds_two(self):
        '''adds_two() adds 2 to input arg and returns sum.'''
        result = plus_two(3)
        assert result == 5, f"Expected 5, but got {result}"
