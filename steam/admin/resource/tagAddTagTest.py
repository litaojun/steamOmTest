from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.resource.tagAddTagService import TagAddTagService
from steam.admin.resource.tagRemoveTagService import TagRemoveTagService
from steam.user.collection.userCancelCollectionService import UserCancelCollectionService
class TagAddTagTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/tag/addTag"
      @initInputService( services = [ TagRemoveTagService  ],
                  curser   = TagAddTagService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(TagAddTagTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.search.weixinSearchTest import WeixinSearchTest
    from steam.user.collection.userCancelCollectionTest import UserCancelCollectionTest
    from steam.admin.resource.tagRemoveTagTest import TagRemoveTagTest
    TagRemoveTagTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\resource\\operation-manageTagAddTags.yml",
                    testclse     = TagAddTagTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )