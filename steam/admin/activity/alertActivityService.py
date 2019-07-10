from opg.util.utils import setValue_json
from steam.admin.activity.searchActivityService import ActivitySearchService
from steam.util.httpUopService import HttpUopService
from opg.bak.uopService import decorator
class ActivityAlertService(HttpUopService):
    '''
        分类修改
    '''
    def __init__(self, kwargs):
        super(ActivityAlertService, self).__init__(module="",
                                                   filename="",
                                                   sqlvaluedict=kwargs,
                                                   reqjsonfile=None)

    @decorator("setupGetSetNewTitle")
    def alertMatchName(self):
        self.inputKV["matchName"] = self.inputKV["alertMatchName"]

    def alertReqIdToValue(self, skulist=[], imglist=[], sharelist=[]):
        self.idToValueByFormat(formatstr = "skuList.%d.skuId",
                               idlist = skulist)
        self.idToValueByFormat(formatstr = "imageList.%d.id",
                               idlist = imglist)
        self.idToValueByFormat(formatstr = "shareInfoList.%d.id",
                               idlist = sharelist)

    def idToValueByFormat(self, formatstr="", idlist=[]):
        for i, idvalue in enumerate(idlist):
            setValue_json(json_content=self.activityAlertReqjson,
                          query=formatstr %
                          i,
                          setvalue=idvalue)

    def getActivityIdByTitle(self, title=None):
        articleQs = ActivitySearchService(kwargs={"title": title,
                                                  "resourceTypeId": self.activityAlertReqjson["resourceTypeId"]})
        queryRsp = articleQs.queryActivity()
        rssid = articleQs.getFirstActivityIdByRsp(queryRsp=queryRsp)
        return rssid