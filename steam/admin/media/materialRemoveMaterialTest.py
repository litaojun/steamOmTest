from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.admin.media.materialRemoveMaterialService import MaterialRemoveMaterialService
from steam.admin.media.materialCreateMaterialService import MaterialCreateMaterialService
from steam.admin.media.queryMerchantInfoByCondtionService import QueryMerchantInfoByCondtionService
class MaterialRemoveMaterialTest(SteamTestCase):
      """
            %(subTitle)s
      """
      __interfaceName__ = "/operation-manage/material/removeMaterial"
      @initInputService( services = [  MaterialCreateMaterialService ,
                                       QueryMerchantInfoByCondtionService ],
                          curser  =  MaterialRemoveMaterialService )

      def __init__( self, methodName = 'runTest',
                          param      =  None ):
          super(MaterialRemoveMaterialTest,self).__init__( methodName  , param )

if __name__ == "__main__":
    from steam.admin.media.materialCreateMaterialTest import MaterialCreateMaterialTest
    MaterialCreateMaterialTest( methodName = "compareRetcodeTest" ,
                             param     = [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
    from steam.admin.media.queryMerchantInfoByCondtionTest import QueryMerchantInfoByCondtionTest
    QueryMerchantInfoByCondtionTest( methodName = "compareRetcodeTest" ,
                                     param      = [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
    runTestOneCls(
                    casefilepath = "\\steamcase\\admin\\media\\operation-manageMaterialRemoveMaterials.yml",
                    testclse     = MaterialRemoveMaterialTest,
                    basepath     = "D:\\litaojun\\steamyml"
                 )