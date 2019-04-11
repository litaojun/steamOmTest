from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from steam.admin.article.ArticleSearchService import ArticleSearchService
from steam.admin.article.mediaUnpublishService import MediaUnpublishService
class MediaUnpublishTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/media/unpublish"
      @initInputService( services = [ ArticleSearchService ],
                  curser   = MediaUnpublishService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MediaUnpublishTest,self).__init__(methodName,param)

if __name__ == "__main__":
    pass