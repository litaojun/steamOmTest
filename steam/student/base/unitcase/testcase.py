from unittest import TestCase,TestSuite
from unittest import TextTestRunner
from steam.student.base.unitcase.testObj import play
class SimplePlayerTest(TestCase):
    def setUp(self):
        self.p = play(2,9)
    def testMoveUp(self):
        self.p.moveUp()
        self.assertTrue(self.p.x == 2 and self.p.y == 10 ,
                        msg="expect x=2,y=10,act x=%d,y=%d"
                            % (self.p.x,self.p.y))
    def testMoveDown(self):
        self.p.moveDown()
        assert self.p.x == 2 and self.p.y == 8
if __name__ == "__main__":
   suite = TestSuite()
   moveUpCase = SimplePlayerTest("testMoveUp")
   moveDownCase = SimplePlayerTest("testMoveDown")
   suite.addTest(moveUpCase)
   suite.addTest(moveDownCase)
   trunner = TextTestRunner()
   trunner.run(suite)