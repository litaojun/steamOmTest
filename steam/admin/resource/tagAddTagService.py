from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService

class TagAddTagService(HttpUopService):
    '''
        新增标签
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(TagAddTagService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    @decorator(["tearDownGetTagId","setupGetTagId"])
    def getTagId(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        self.inputKV["tagId"] = query_json( json_content = json.loads(self.rsp) ,
                                             query        = "data" )

    @decorator(["setupAddTag"])
    def addTag(self):
        self.sendHttpReq()


