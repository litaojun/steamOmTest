from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.resource.tagQueryTagsService import TagQueryTagsService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.collection.userCancelCollectionService import UserCancelCollectionService
class TagQueryTagsTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/tag/queryTags"
      @initAdminInputService( services = [ WeixinSearchService ,UserCancelCollectionService ],
                         curser   = TagQueryTagsService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(TagQueryTagsTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\resource\\operation-manageTagQueryTagss.yml",
                    testclse     = TagQueryTagsTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )