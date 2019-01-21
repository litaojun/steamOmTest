from steam.admin.login.userLoginService import UserLoginService
from steam.util.steamLog import SteamTestCase
from steam.admin.activity.searchActivityTest import ActivitySearchService
from steam.user.search.weixinSearchService import WeixinSearchService
def sendHttpReqByToken():
    adminTokenRefresh()
    weixinTokenRefresh()
    return True

def adminTokenRefresh():
    args = {
                   "currentPage":1,
                   "pageSize":10,
                   "resourceTypeId":12,
                   "title":"早鸟价！呼伦贝尔｜私家牧场任你驰骋策马，原始森林徒步猎奇",
                   "skuName":"价格（成人）",
                   "token": UserLoginService.getTokenData()
           }
    aqs = ActivitySearchService(kwargs=args)
    aqs.sendHttpReq()
    print("admin token已刷新")
    return True

def weixinTokenRefresh():
    args = { "keyword":"测试" }
    for phone in SteamTestCase.memberIdDict:
        args["token"]    = SteamTestCase.memberIdDict[phone][0]
        args["memberId"] = SteamTestCase.memberIdDict[phone][1]
        ser = WeixinSearchService(kwargs=args)
        ser.sendHttpReq()
        print("手机号码:%s对应token:%s，memberId:%s已刷新")
    return True

if __name__ == "__main__":
    SteamTestCase.memberIdDict={
                                   "18916899938":["9a4b249a254842d281c2be7986dbd820","1a3fb52131ee4723a893f32148b02161"],
                                   "18699922333":["0594ce8598434814a2683aab30e22135","aefe1947-b885-40a5-8299-ffe3332af8f1"]
                                }
    WeixinSearchService.__interfaceName__ = "/steam-search/search/keywordSearch"
    ActivitySearchService.__interfaceName__ = "/operation-manage/product/queryProducts"
    sendHttpReqByToken()