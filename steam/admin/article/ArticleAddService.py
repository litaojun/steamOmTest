
from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
#from steam.util.configurl import delArticleurl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import  fxt, articleAddRspFmt
from opg.util.httptools import httpPost
from steam.util.httpUopService import  HttpUopService
class ArticleAddService(HttpUopService):
    '''
        管理后台新增文章视频
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ArticleAddService, self).__init__("", "", kwargs)
        self.articleReqjson = self.reqjsondata

    @decorator("tearInterfaceDelOneArticle")
    def delArticle(self):
        articleid = self.getArticleIdByRsp(self.rsp)
        delclassfiyRsp = httpPost(url         = delArticleurl,
                                  headers     = self.jsonheart,
                                  reqJsonData = {"resourceId": articleid})
        return delclassfiyRsp

    @decorator("setupAddOneArticle")
    def addArticle(self):
        self.rsp = self.sendHttpReq()
        return self.rsp

    @check_rspdata(filepath=fxt.join(articleAddRspFmt))
    def getRetcodeByArticleRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

    def getArticleIdByRsp(self,articleRsp = None):
        articleQs = ArticleQueryService(kwargs=self.inputKV)
        queryRsp = articleQs.queryArtcle()
        rssid = articleQs.getFirstResourceIdByRsp(queryRsp = queryRsp)
        return rssid

if __name__ == "__main__":
   pass