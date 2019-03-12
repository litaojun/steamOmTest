from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService

class FeaturedMoveDownRecordService(HttpUopService):
    '''
        运营位记录下移
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(FeaturedMoveDownRecordService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )

    @decorator(["setupListOrderDown"])
    def setListOrderUp(self):
        self.inputKV["listOrder"] += 1