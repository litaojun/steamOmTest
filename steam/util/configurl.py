#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: configurl.py 
@time: 2018/4/18 14:40 
"""
from opg.util.fileOper import walk_dir_test
import os
#环境IP地址
base_url = "https://uat-steam-api.opg.cn"
#商品或者活动接口---STEAM商品微服务-管理后台REST接口文档v1.2.0.docx
searchActivityurl  = base_url   + "/operation-manage/product/queryProducts"
upActivityurl      = base_url   + "/operation-manage/product/publish"
downActivityurl    = base_url   + "/operation-manage/product/unPublish"
addActivityurl     = base_url   + "/operation-manage/product/add"
alertActivityurl   = base_url   + "/operation-manage/product/update"
queryIdActivityurl = base_url   + "/operation-manage/product/query"
#文章视频接口  STEAM媒资微服务-管理后台REST接口文档-1.2.0.docx
addArticleurl       =  base_url      + "/operation-manage/media/addMedia"
delArticleurl       =  base_url      + "/operation-manage/media/deleteMedia"
alertArtcleurl      = base_url       + "/operation-manage/media/updateMedia"
userViewMediaresUrl = base_url       + "/steam-media/media/getMediaDetailByID"
queryArticleurl     = base_url       + "/operation-manage/media/queryMedias?currentPage=1&pageSize=10"
#分类管理 --- STEAM资源微服务REST接口文档v1.0.0.2.docx
addentryurl          = base_url          + "/operation-manage/entry/addEntry"
alertentryurl        = base_url          + "/operation-manage/entry/modifyEntry"
delEntryurl          = base_url          + "/operation-manage/entry/removeEntry"
userThumbUpUrl       = base_url          + "/resource-service/resource/thumbUp"
userCancelThumbUpUrl = base_url          + "/resource-service/resource/cancelThumbUp"
uploadImagesurl      = base_url          + "/steam-resource/resource/uploadImages"
#赛事后台管理   ---STEAM赛事微服务-管理后台REST接口文档v1.2.0
addMatchurl       =     base_url     +  "/operation-manage/match/createMatch"
delMatchurl       =     base_url     +  "/operation-manage/match/deleteMatch"
alertMatchurl     =     base_url     +  "/operation-manage/match/updateMatchById"
findMatchUrl      =     base_url     +  "/operation-manage/match/matchPage?currentPage=1&pageSize=10"
findSubMatchUrl      =  base_url     +  "/operation-manage/match/subMatchPage?currentPage=1&pageSize=10"
pageQueryMatchUrl =     base_url     +  "/operation-manage/match/matchPage"
detailMatchUrl    =     base_url     +  "/operation-manage/match/matchDetail"
appleListMatchUrl =     base_url     +  "/operation-manage/apply/page"
#用户报名接口   STEAM赛事报名微服务-用户端REST接口文档v1.2.0.docx
userMatchAppleUrl       =   base_url       +  "/match-service/member/apply"
userCancelMatchAppleUrl =   base_url       +  "/match-service/member/apply/cancel"
userMatchQueryUrl       =   base_url       +  "/match-service/member/wa/query"
userMatchAppleQueryUrl  =   base_url       +  "/match-service/member/mp/query"
userViewActivityUrl     =   base_url       +  "/steam-resource/product/detail"
#运营位管理  STEAM推荐位微服务REST接口文档v1.0.2.docx
addOperpositionurl   =    base_url    +  "/operation-manage/featured/createConfig"
delOperpositionurl   =    base_url    +  "/steam-featured/homeConfig/removeIndexConfig"
alertOperpositionurl =    base_url    +  "/steam-featured/homeConfig/modifyIndexConfig"
homeConfigQueryurl   =    base_url    + "/operation-manage/featured/queryShowConfigs?pageNo=1&pageSize=20"
#首页  STEAM推荐位CMS-admin接口文档v1.0.0.docx
queryHomeConfigurl =  base_url       +  "/steam-featured/homeConfig/listData?pageNo=1&pageSize=20" #position=03&title=ffff
hotPositonUrl      =  base_url       +  "/featured/index/configs/pageQueryPositionShows"
#通行证服务   STEAM通行证微服务REST接口文档v1.0.0.docx
weixinUserLoginurl      = base_url      + "/member/login/memberLogin"
weixinUserVerifyCodeurl = base_url      + "/passport/verifyCode"
weixinUserMemberIdUrl   = base_url      + "/member/login/queryMemberInfo"
#订单相关  STEAM订单微服务-用户端REST接口文档v1.0.0.docx
userOrderActivityUrl       = base_url + "/order-service/order/submitAndPay"
userCancelOrderActivityUrl = base_url + "/order-service/order/cancel"
userDetailOrderActivityUrl = base_url + "/order-service/order/detail"
userListOrderActivityUrl   = base_url + "/order-service/order"
#会员管理 STEAM会员微服务REST接口文档v1.0.0.docx
memberAddressUrl  = base_url + "/member-service/address/memberId"
userAddAddressUrl = base_url + "/member-service/address"
userDelAddressUrl = base_url + "/member-service/address"
memberPersonalCenterUrl = base_url + "/member-service/members/personalCenter"
#后台赛事管理    STEAM赛事微服务-管理后台REST接口文档v1.2.0.docx
sessionAddUrl    = base_url    + "/match-service/match/createMatch"
sessionDelUrl    = base_url    + "/match-service/match/deleteMatch"
sessionUpdateUrl = base_url    + "/match-service/match/updateMatchById"
sessionQueryUrl  = base_url    + "/match-service/match/subMatchPage"
#后台登录
adminLoginUrl = base_url + "/operation-manage/permission/admin/login"

#STEAM搜索微服务REST接口文档v1.2.0.docx
weixinSearchUrl = base_url + "/steam-search/search/keywordSearch"
weixinQueryKeywordsUrl = base_url + "/steam-search/search/queryKeywords"

userSearchEntryUrl = base_url + "/steam-resource/index/configs/searchByEntry"


#STEAM在线课程REST接口文档v1.2.1.docx
userViewCourseUrl = base_url + "/steam-course/course/queryAliyunVideoAuth"
recommandCourseUrl = base_url + "/steam-course/course/queryRecommandCourse"
userStudentCourseListUrl = base_url + "/order-service/study/list?pageNo=1&pageSize=10"
queryAliyunVideoAuthUrl = base_url + "/steam-course/course/queryAliyunVideoAuth"

if __name__ == "__main__":
	als = walk_dir_test(dir=os.getcwd(),sign="Req",endstr=".txt")
	print(als)
	a = [os.path.basename(path) for path in als]
	print(a)
	als = walk_dir_test(dir=os.getcwd(),sign="Fmt",endstr=".json")
	print(als)
	mt = {}
	a = [(os.path.basename(path).split(".")[0],path) for path in als]
	for cs in a:
		mt[cs[0]] = cs[1]
	print(str(mt))