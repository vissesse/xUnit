from typing import List  
from testCaseTest import TestCaseTest


class TestSuite:

    def __init__(self):
        self.tests = []
        
    def add(self, test:TestCaseTest):
        self.tests.append(test)
    
    def run(self, result): 
        for test in self.tests:
            test.run(result)  
