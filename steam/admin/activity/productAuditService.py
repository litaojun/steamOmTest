from steam.util.httpUopService import  HttpUopService
from opg.bak.uopService import decorator
class ProductAuditService(HttpUopService):
    '''
        审核活动
    '''
    def __init__(self, kwargs):
        super(ProductAuditService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
    @decorator(["setupAuditActivity"])
    def optAuditActivity(self):
        self.sendHttpReq()