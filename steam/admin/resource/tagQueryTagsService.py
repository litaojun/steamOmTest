from steam.util.httpUopService import  HttpUopService

class TagQueryTagsService(HttpUopService):
    '''
        根据关键词分页查询标签
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(TagQueryTagsService, self).__init__(module       = "",
												 filename     = "",
												 sqlvaluedict = kwargs )
