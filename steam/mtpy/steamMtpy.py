import typing
from mitmproxy import ctx
import mitmproxy.addonmanager
import mitmproxy.connections
import mitmproxy.http
import mitmproxy.log
import mitmproxy.tcp
import mitmproxy.websocket
import mitmproxy.proxy.protocol


class SteamMtyp:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        method = flow.request.method
        print("itaojun - gelt")
        ctx.log.info("itaojun - gelt")
        if method == "GET":
            query = flow.request.query
            queryurl = "&".join(["%s=%s" % (k,v) for k,v in query.items()])
            print("query = %s " % queryurl)
        elif method == "POST":
            body = flow.request.get_text()
            print("body = %s" % body)


    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        data = flow.response.text
        print("body = %s" % data)


def start():
    return SteamMtyp()