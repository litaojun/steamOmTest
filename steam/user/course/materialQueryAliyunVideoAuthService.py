from steam.util.httpUopService import  HttpUopService
class MaterialQueryAliyunVideoAuthService(HttpUopService):
    '''
        用户获取播放权限信息
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(MaterialQueryAliyunVideoAuthService, self).__init__(  module       = modul,
                                                                    filename     = filename,
                                                                    sqlvaluedict = kwargs ,
                                                                    reqjsonfile  = reqjsonfile )

if  __name__ == "__main__":
    kwargs = {
                "courseId":4448,
                "materialId":15 ,
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "token":"e0e1db2796f943259d1d87a7a48d727f"
             }
    uvcSer    = MaterialQueryAliyunVideoAuthService(kwargs=kwargs)
    courseRsp = uvcSer.getAliyunVideoAuthReq()
    print(courseRsp)