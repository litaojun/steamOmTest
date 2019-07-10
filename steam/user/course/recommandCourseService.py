from steam.util.httpUopService import  HttpUopService
class RecommandCourseService(HttpUopService):
    '''
        用户查看推荐课程列表
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(RecommandCourseService, self).__init__(  module       = modul,
                                                       filename     = filename,
                                                       sqlvaluedict = kwargs ,
                                                       reqjsonfile  = reqjsonfile )

if  __name__ == "__main__":
    kwargs = {
                "courseId":4165,
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "token":"63779ff8becd413f9c389331592d5d96"
             }
    uvcSer = RecommandCourseService(kwargs=kwargs)
    courseRsp = uvcSer.recommandCourseList()
    print(courseRsp)