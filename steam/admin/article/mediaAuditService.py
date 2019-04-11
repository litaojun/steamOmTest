from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService

class MediaAuditService(HttpUopService):
    '''
        审核文章视频
    '''
    @decorator(["setupAuditMedia","tearDownAuditMedia"])
    def auditMedia(self):
        self.sendHttpReq()

    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MediaAuditService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
