
from steam.util.steamLog import SteamTestCase
from steam.admin.article.ArticleAddService import ArticleAddService
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.testJsonFormat import initAdminInputService
from steam.admin.article.delArticleService import ArticleDelService
from steam.admin.article.ArticleSearchService import ArticleSearchService
class ArticleAddTest(SteamTestCase):
      '''
            管理后台新增文章视频
      '''
      __interfaceName__ = "/operation-manage/media/addMedia"
      @initAdminInputService( services =  [ ArticleDelService ,ArticleSearchService] ,
                         curser   =   ArticleAddService  )
      def __init__(self, methodName='runTest', param=None):
          super(ArticleAddTest,self).__init__(methodName,param)

