import typing
from mitmproxy import ctx
import mitmproxy.addonmanager
import mitmproxy.connections
import mitmproxy.http
import mitmproxy.log
import mitmproxy.tcp
import mitmproxy.websocket
from opg.util.yamlOper import dumpDataToYmlFile
import json
from steam.mtpy.proxyDataHook import ProxyHook
from steam.mtpy.testcase.autoGenTestcase import genAutoCase,genReqData
import mitmproxy.proxy.protocol

class SteamMtyp:

    def __init__(self):
        self.reqProxyHook = ProxyHook()
        self.reqProxyHook.register_hook(genAutoCase)
        self.reqProxyHook.register_hook(genReqData)
        self.rspProxyHook = ProxyHook()
        self.rspProxyHook.register_hook(genReqData)

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        body,method,host,url = {},flow.request.method,flow.request.host,flow.request.url
        ctx.log.info("SteamMtyp - request method=%s,host=%s,url=%s" % (method,host,url))
        if host == "uat-steam-api.opg.cn":
            ctx.log.info("itaojun - gelt")
            path = flow.request.path.split("?")[0]
            ctx.log.info("path=%s" % path)
            if method == "GET":
                query = flow.request.query
                queryurl = "&".join(["%s=%s" % (k,v) for k,v in query.items()])
                body = dict([(k,v) for k,v in query.items()])
                ctx.log.info("query = %s " % queryurl)
            elif method == "POST":
                body = json.loads(flow.request.get_text(),encoding="utf-8")
                ctx.log.info("body = %s" % body)
            if method in ["GET","POST","DELETE","PUT"]:
               self.reqProxyHook.run(method=method,host=host,url=url,path=path,bodydata=body,bodyType="request")

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        body, method, host, url = {}, flow.request.method, flow.request.host, flow.request.url
        ctx.log.info("SteamMtyp - request method=%s,host=%s" % (method,host))
        if host == "uat-steam-api.opg.cn":
            body,path = flow.response.text,flow.request.path.split("?")[0]
            ctx.log.info("body = %s,path=%s" % (body,path))
            self.rspProxyHook.run(method=method,
                                  host=host,
                                  url=url,
                                  path=path,
                                  bodydata=body,
                                  bodyType="response")

# def start():
#     return SteamMtyp()
addons = [
    SteamMtyp()
]