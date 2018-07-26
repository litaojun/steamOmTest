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
base_url = "https://uat-steam-api.opg.cn"
addentryurl = base_url + "/resource-service/resource/addEntry"
alertentryurl = base_url +"/resource-service/resource/modifyEntry"
delEntryurl = base_url + "/resource-service/resource/removeEntry"
addMatchurl = base_url + "/match-service/match/createMatch"
delMatchurl = base_url + "/match-service/match/deleteMatch"
alertMatchurl = base_url + "/match-service/match/updateMatchById"
uploadImagesurl = "/steam-resource/resource/uploadImages"
addArticleurl =  base_url + "/steam-media/media/addMedia"
delArticleurl =  base_url + "/steam-media/media/deleteMedia"
alertArtcleurl = base_url + "/steam-media/media/updateMedia"
queryArticleurl = base_url + "/steam-media/media/queryMedias?currentPage=1&pageSize=10"
addOperpositionurl = base_url +"/featured-admin/index/configs/createConfig"
delOperpositionurl = base_url +"/steam-featured/homeConfig/removeIndexConfig"
queryHomeConfigurl =  base_url + "/steam-featured/homeConfig/listData?pageNo=1&pageSize=20" #position=03&title=ffff
alertOperpositionurl =  base_url + "/steam-featured/homeConfig/modifyIndexConfig"
addActivityurl = base_url + "/steam-resource/admin/product/add"
alertActivityurl = base_url + "/steam-resource/admin/product/update"
searchActivityurl = base_url + "/steam-resource/admin/product/page"
upActivityurl = base_url + "/steam-resource/admin/product/publish"
downActivityurl = base_url + "/steam-resource/admin/product/unPublish"
queryIdActivityurl = base_url + "/steam-resource/admin/product/query"
homeConfigQueryurl = base_url + "/featured/index/configs/queryShowConfigs"
weixinUserLoginurl = base_url + "/passport/memberLogin"
weixinUserVerifyCodeurl = base_url + "/passport/verifyCode"
hotPositonUrl = base_url + "/featured/index/configs/pageQueryPositionShows"
userThumbUpUrl = base_url + "/resource-service/resource/thumbUp"
userCancelThumbUpUrl = base_url + "/resource-service/resource/cancelThumbUp"
userViewMediaresUrl = base_url + "/steam-media/media/getMediaDetailByID"
userViewActivityUrl =  base_url + "/steam-resource/product/detail"
userOrderActivityUrl = base_url + "/order-service/order/submitAndPay"
userCancelOrderActivityUrl = base_url + "/order-service/order/cancel"
userDetailOrderActivityUrl = base_url + "/order-service/order/detail"
userListOrderActivityUrl = base_url + "/order-service/order"
memberAddressUrl = base_url + "/member-service/address/memberId"
userAddAddressUrl = base_url + "/member-service/address"
userDelAddressUrl = base_url + "/member-service/address"
userMatchAppleUrl = base_url + "/match-service/member/apply"
userCancelMatchAppleUrl = base_url + "/match-service/member/apply/cancel"
userMatchQueryUrl = base_url + "/match-service/member/wa/query"
userMatchAppleQueryUrl = base_url + "/match-service/member/mp/query"
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