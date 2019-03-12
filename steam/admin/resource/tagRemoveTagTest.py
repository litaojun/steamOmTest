from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.resource.tagRemoveTagService import TagRemoveTagService
from steam.admin.resource.tagAddTagService import TagAddTagService
class TagRemoveTagTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/tag/removeTag"
      @initAdminInputService( services = [ TagAddTagService  ],
                  curser   = TagRemoveTagService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(TagRemoveTagTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.admin.resource.tagAddTagTest import TagAddTagTest
    TagAddTagTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\resource\\operation-manageTagRemoveTags.yml",
                    testclse     = TagRemoveTagTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )