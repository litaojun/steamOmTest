from steam.util.httpUopService import  HttpUopService
from opg.util.uopService import decorator

class ChangePhoneNoService(HttpUopService):
    '''
        修改手机号
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ChangePhoneNoService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    @decorator(["tearDownExchangeOldNewPhoneNo"])
    def exchangeOldNewPhone(self):
        self.inputKV["oldPhoneNo"] , self.inputKV["newPhoneNo"] = self.inputKV["newPhoneNo"] , self.inputKV["oldPhoneNo"]

    @decorator(["tearDownChangePhone"])
    def changePhoneNo(self):
        self.sendHttpReq()
