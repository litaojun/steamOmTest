from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.httptools import httpPost
from opg.util.utils import query_json
from opg.util.schemajson import check_rspdata
from steam.util.httpUopService import  HttpUopService

class ScoreAddService(HttpUopService):
    '''
        添加评分
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ScoreAddService, self).__init__(module       = "order",
											  filename     = "order.xml",
											  sqlvaluedict = kwargs,
                                              dbName= "allin")

    @decorator(["tearDownDelUserScoreData","setupDelUserScoreData"])
    def deleteUserScoreById(self):
        self.deleteBySqlName(sqlname="setupDBdelect_tb_order_scoreBy_orderId")
