from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.collection.userListCollectionService import UserListCollectionService
class UserListCollectionTest(SteamTestCase):
      '''
            用户浏览课程
      '''
      __interfaceName__    = "/member/collection/queryPage"
      @initInputService( services = [ ] ,
                         curser   = UserListCollectionService )
      def __init__( self, methodName = 'runTest',
                          param      =  None ):
          super(UserListCollectionTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.login.queryMemberIdTest import QueryMemberIdTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest( methodName="compareRetcodeTest",
                   param=[1, 2, 3, 4, 5, {}, 7, 8] )
    QueryMemberIdTest( methodName = "compareRetcodeTest",
                       param      = [1, 2, 3, 4, 5, {}, 7, 8] )
    runTestOneCls(
                    casefilepath = "\\steamcase\\user\\membercollectionqueryPages.yml",
                    testclse     = UserListCollectionTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )