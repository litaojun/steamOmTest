from steam.util.steamLog import SteamTestCase
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.weixin.userViewCourseService import UserViewCourseService
from steam.util.testJsonFormat import initInputService
class UserViewCourseTest(SteamTestCase):
      '''
            用户浏览课程
      '''
      __interfaceName__ = "/steam-course/course/queryCourse"
      @initInputService( services = [ WeixinSearchService ],
                         curser   = UserViewCourseService )
      def __init__( self, methodName = 'runTest',
                          param      = None ):
          super(UserViewCourseTest,self).__init__(methodName,param)