from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService

class MaterialCreateMaterialService(HttpUopService):
    '''
        新增素材
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MaterialCreateMaterialService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    @decorator(["setupCreateOneMaterial"])
    def createOneMaterial(self):
        self.rsp = self.sendHttpReq()