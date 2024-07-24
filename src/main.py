from TestSuite import TestSuite
from TestResult import TestResult
from testCaseTest import TestCaseTest

suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSuite"))

result = TestResult()

suite.run(result)

print(result.summary())
