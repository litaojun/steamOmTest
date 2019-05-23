from opg.unit.parametrized import ParametrizedTestCase
import logging
logger = logging.getLogger(__name__)
class UserLoginTest(ParametrizedTestCase):
      def __init__(self):
          logger = logging.getLogger("%s.%s" % (self.__class__.__name__, "__init__"))

if __name__ == "__main__":
   ult = UserLoginTest()