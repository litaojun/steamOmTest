from opg.bak.uopService import decorator
from steam.util.httpUopService import  HttpUopService

class FeaturedMoveUpRecordService(HttpUopService):
    '''
        运营位记录上移
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(FeaturedMoveUpRecordService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
    @decorator(["setupListOrderUp"])
    def setListOrderUp(self):
        if self.inputKV["listOrder"] > 1:
           self.inputKV["listOrder"] -= 1
