from opg.util.uopService import decorator
import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService

class LotteryQueryLotteryListService(HttpUopService):
    '''
        抽奖活动列表
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(LotteryQueryLotteryListService, self).__init__(module       = "",
                                                             filename     = "",
                                                             sqlvaluedict = kwargs )

    def getNameIdList(self):
        if self.rsp is None:
            self.rsp = self.sendHttpReq()
        lotteryList = query_json(json_content=json.loads(self.rsp),
                                 query="data.targets")
        return lotteryList

    def genNameIdDict(self):
        lotteryList = self.getNameIdList()
        return dict((lttery["lotteryTitle"],lttery["resourceId"])
                    for lttery in lotteryList)

    @decorator(["setupGetResourceIdByLotyTitle","tearDownGetResourceIdByLotyTitle"],userType="admin")
    def getRsidByLotyName(self):
        lotyDict  = self.genNameIdDict()
        self.inputKV["resourceId"] = lotyDict[self.inputKV["lotyName"]]

    def findTestdataByStatus(self):
        nameIdList = self.getNameIdList()
        dataDict = [(data["title"],data) for data in nameIdList ]
        # nameIdDict = self.genNameIdDict()
        # print(self.inputKV)
        if self.inputKV["title"] not in dataDict:
            return "100001"
        # nameIdList = self.getNameIdList()
        # datals = [data for data in nameIdList if data["title"] == self.inputKV["title"] and data["state"]==self.inputKV["status"] ]
        curData = dataDict[self.inputKV["title"]]
        if curData["state"] != self.inputKV["status"]:
            self.inputKV["resourceId"] = curData["id"]
            return "100002"
        return "000000"

