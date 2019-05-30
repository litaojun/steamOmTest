from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.article.mediaResetMediaStateService import MediaResetMediaStateService
from steam.admin.article.ArticleSearchService import ArticleSearchService
class MediaResetMediaStateTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/media/resetMediaState--del"
      @initAdminInputService( services = [ ArticleSearchService ] ,
                         curser   = MediaResetMediaStateService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MediaResetMediaStateTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.admin.article.ArticleSearchTest import ArticleSearchTest
    ArticleSearchTest(methodName = "compareRetcodeTest", param = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\article\\operation-manageMediaResetMediaStates.yml",
                    testclse     = MediaResetMediaStateTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )