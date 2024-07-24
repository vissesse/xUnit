from TestResult import TestResult


class TestCase:
    def __init__(self, name: str):
        self.name = name

    def run(self, result:TestResult): 
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown() 

    def setUp(self):
        pass

    def tearDown(self):
        pass
