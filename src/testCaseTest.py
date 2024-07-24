from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite
from WasRun import WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod") 
        
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run() 
        assert("setUp testMethod tearDown " == test.log)
    
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run() 
        # print("error", result.summary())
        assert("1 run, 1 failed" == result.summary())
  
    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()   
        assert("1 run, 1 failed" == result.summary())
   
    def testSuite(self):
        suite= TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert("2 run, 1 failed" == result.summary)