from steam.admin.activity.alertActivityService import ActivityAlertService
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService
class ActivityAlertTest(SteamTestCase):
    '''
          新增活动
    '''
    __interfaceName__ = "/operation-manage/product/update"
    @initAdminInputService(services=[],
                           curser=ActivityAlertService)
    def __init__(self, methodName='runTest', param=None):
        super(ActivityAlertTest, self).__init__(methodName, param)


if __name__ == "__main__":
    runTestOneCls(casefilepath="\\steamcase\\admin\\activity\\operation-manageproductupdates.yml",
                  testclse=ActivityAlertTest,
                  basepath="D:\\litaojun\\steamyml")
