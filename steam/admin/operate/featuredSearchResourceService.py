from opg.bak.uopService import decorator
import json
from   opg.util.utils import query_json
from   steam.util.httpUopService import  HttpUopService

class FeaturedSearchResourceService(HttpUopService):
    '''
        根据资源类型搜索已发布资源
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(FeaturedSearchResourceService, self).__init__(module       = "",
												            filename     = "",
												            sqlvaluedict = kwargs )
    @decorator(["setupGetFirstSearchResource"])
    def getFirstSearchResource(self):
        # if self.rsp is None:
        self.rsp = self.sendHttpReq()
        self.inputKV["resourceId"] = int(query_json(json_content = json.loads(self.rsp),
                                                      query       = "data.0.resourceId"))

    @decorator(["setupGetFirstSearchAlertResource"])
    def getFirstSearchAlertResource(self):
        self.inputKV["alertTitle"] , \
        self.inputKV["title"] = self.inputKV["alertTitle"] ,\
                                 self.inputKV["title"]
        self.rsp = self.sendHttpReq()
        self.inputKV["alertResourceId"] = int(query_json(json_content = json.loads(self.rsp),
                                                            query       = "data.0.resourceId"))
        self.inputKV["alertTitle"],\
        self.inputKV["title"] = self.inputKV["alertTitle"],\
                                self.inputKV["title"]