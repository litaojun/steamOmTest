from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.media.materialModifyMaterialService import MaterialModifyMaterialService
from steam.admin.media.queryMerchantInfoByCondtionService import QueryMerchantInfoByCondtionService
from steam.admin.media.materialCreateMaterialService import MaterialCreateMaterialService
from steam.admin.media.materialRemoveMaterialService import MaterialRemoveMaterialService
class MaterialModifyMaterialTest(SteamTestCase):
      """
            修改媒资
      """
      __interfaceName__ = "/operation-manage/material/modifyMaterial"
      @initAdminInputService( services = [  MaterialCreateMaterialService,MaterialRemoveMaterialService,
                                            QueryMerchantInfoByCondtionService ],
                         curser   =   MaterialModifyMaterialService )
      def __init__(self, methodName = 'runTest' ,
                         param      =  None):
          super(MaterialModifyMaterialTest,self).__init__(methodName,param)

if __name__ == "__main__":
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\media\\operation-manageMaterialModifyMaterials.yml",
                    testclse     = MaterialModifyMaterialTest ,
                    basepath     = "D:\\litaojun\\steamyml"
                 )