from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from steam.admin.article.ArticleSearchService import ArticleSearchService
from steam.admin.article.ArticleAddService import ArticleAddService
from steam.admin.article.delArticleService import ArticleDelService
from steam.admin.article.mediaAuditService import MediaAuditService

class MediaAuditTest(SteamTestCase):
      """
           审核文章视频
      """
      __interfaceName__ = "/operation-manage/media/audit"
      @initInputService( services = [ ArticleAddService,ArticleSearchService,ArticleDelService ],
                         curser   = MediaAuditService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MediaAuditTest,self).__init__(methodName,param)

if __name__ == "__main__":
    pass