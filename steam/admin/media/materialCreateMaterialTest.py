from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.media.materialCreateMaterialService import MaterialCreateMaterialService
from steam.admin.media.queryMerchantInfoByCondtionService import QueryMerchantInfoByCondtionService
from steam.admin.media.materialRemoveMaterialService import MaterialRemoveMaterialService
class MaterialCreateMaterialTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/material/createMaterial"
      @initAdminInputService( services = [ QueryMerchantInfoByCondtionService ,
                                      MaterialRemoveMaterialService ],
                         curser   =  MaterialCreateMaterialService )
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(MaterialCreateMaterialTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.admin.media.queryMerchantInfoByCondtionTest import QueryMerchantInfoByCondtionTest
    QueryMerchantInfoByCondtionTest( methodName = "compareRetcodeTest" ,
                                      param     = [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
    from steam.admin.media.materialRemoveMaterialTest import MaterialRemoveMaterialTest
    MaterialRemoveMaterialTest( methodName = "compareRetcodeTest" ,
                                 param     = [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\media\\operation-manageMaterialCreateMaterials.yml" ,
                    testclse     = MaterialCreateMaterialTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )