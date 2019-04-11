from steam.admin.article.ArticleSearchService import ArticleSearchService
from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from steam.admin.article.mediaPublishService import MediaPublishService

class MediaPublishTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/media/publish"
      @initInputService( services = [ ArticleSearchService ],
                  curser   = MediaPublishService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MediaPublishTest,self).__init__(methodName,param)

if __name__ == "__main__":
   pass