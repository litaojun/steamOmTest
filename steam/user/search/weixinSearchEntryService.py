from steam.util.httpUopService import  HttpUopService
class UserSearchEntryService(HttpUopService):
    '''
          微信端-分类搜索
    '''
    def __init__(self,kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserSearchEntryService, self).__init__(module       =  "",
                                                     filename     =  "",
                                                     sqlvaluedict =  kwargs,
                                                     reqjsonfile  =  "userSearchEntryReq")

    def userSearchEntryReq(self):
        self.rsp = self.sendHttpReq()
        return self.rsp
