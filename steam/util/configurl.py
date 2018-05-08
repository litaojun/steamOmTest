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
addOperpositionurl = base_url +"/steam-featured/homeConfig/createConfig"
delOperpositionurl = base_url +"/steam-featured/homeConfig/removeIndexConfig"
queryHomeConfigurl =  base_url + "/steam-featured/homeConfig/listData?pageNo=1&pageSize=20" #position=03&title=ffff
alertOperpositionurl =  base_url + "/steam-featured/homeConfig/modifyIndexConfig"
addActivityurl = base_url + "/steam-resource/admin/product/add"
alertActivityurl = base_url + "/steam-resource/admin/product/update"
searchActivityurl = base_url + "/steam-resource/admin/product/page"
upActivityurl = base_url + "/steam-resource/admin/product/publish"
downActivityurl = base_url + "/steam-resource/admin/product/unPublish"
queryIdActivityurl = base_url + "/steam-resource/admin/product/query"

if __name__ == "__main__":
	pass  