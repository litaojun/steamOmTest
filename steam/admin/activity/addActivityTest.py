#!/usr/bin/env python
# encoding: utf-8
from steam.admin.activity.addActivityService import ActivityAddService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initAdminInputService


class ActivityAddTest(SteamTestCase):
    """
         新增活动
    """
    __interfaceName__ = "/operation-manage/product/add"
    @initAdminInputService(curser=ActivityAddService)
    def __init__(self, methodName='runTest',
                 param=None):
        super(ActivityAddTest, self).__init__(methodName,
                                              param)


if __name__ == "__main__":
    runTestOneCls(
        casefilepath="\\steamcase\\admin\\activity\\operation-manageproductadds.yml",
        testclse=ActivityAddTest,
        basepath="D:\\litaojun\\steamyml")
