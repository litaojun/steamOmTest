from steam.util.testJsonFormat import initAdminInputService
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.admin.media.materialModifyMaterialService import MaterialModifyMaterialService


class MaterialModifyMaterialTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/material/modifyMaterial"
      @initAdminInputService( services = [   ],
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