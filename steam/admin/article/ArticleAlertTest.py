from steam.admin.article.ArticleAlertService import ArticleAlertService
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService
from steam.admin.article.ArticleSearchService import ArticleSearchService
from steam.admin.article.delArticleService import ArticleDelService
from steam.admin.article.ArticleAddService import ArticleAddService
from steam.admin.article.ArticleAddTest import ArticleAddTest
class ArticleAlertTest(SteamTestCase):
      '''
            管理后台修改文章
      '''
      __interfaceName__ = "/operation-manage/media/updateMedia"
      @initAdminInputService( services =  [ArticleDelService,ArticleSearchService,ArticleAddService] ,
                         curser   =  ArticleAlertService  )
      def __init__( self, methodName = 'runTest',
                          param      =  None ):
          super(ArticleAlertTest,self).__init__(methodName,param)

if __name__ == "__main__":
   from steam.admin.article.ArticleSearchTest import ArticleSearchTest
   from steam.admin.article.delArticleTest import ArticleDelTest
   ArticleDelTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
   ArticleSearchTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
   ArticleAddTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath =  "\\steamcase\\article\\operation-managemediaupdateMedias.yml",
                    testclse     =  ArticleAlertTest
                )