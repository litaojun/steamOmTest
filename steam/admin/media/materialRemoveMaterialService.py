from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService

class MaterialRemoveMaterialService(HttpUopService):
    '''
        删除素材
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MaterialRemoveMaterialService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    @decorator(["setupRemoveMeterial","tearDownRemoveMeterial"])
    def removeMaterial(self):
        self.rsp = self.sendHttpReq()
