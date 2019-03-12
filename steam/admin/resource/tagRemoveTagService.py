from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService

class TagRemoveTagService(HttpUopService):
    '''
        删除标签
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(TagRemoveTagService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    @decorator(["tearDownRemoveTag"])
    def removeTag(self):
        self.sendHttpReq()
