#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: Lieb
@license: Apache Licence
@contact: 2750416737@qq.com
@site: http://blog.csdn.net/hqzxsc2006
@software: PyCharm
@file: httpLib2Test.py
@time: 2018/7/20 9:45
"""
import time
import urllib.request
##https://blog.csdn.net/xygg0801/article/details/56685030

if __name__  == "__main__":
    # buld post body data
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'username')
    data.append('jack')
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'mobile')
    data.append('13800138000')
    data.append('--%s' % boundary)
    fr = open(r'/var/qr/b.png', 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename="b.png"' % 'profile')
    data.append('Content-Type: %s\r\n' % 'image/png')
    data.append(fr.read())
    fr.close()
    data.append('--%s--\r\n' % boundary)

    http_url = 'http://remotserver.com/page.php'
    http_body = '\r\n'.join(data)
    try:
        # buld http request
        req = urllib.request.urlopen(http_url, data=http_body)
        # header
        req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
        req.add_header('User-Agent', 'Mozilla/5.0')
        req.add_header('Referer', 'http://remotserver.com/')
        # post data to server
        resp =  urllib.request.urlopen(req, timeout=5)
        # get response
        qrcont = resp.read()
        print(qrcont)
    except Exception as ex:
        print("http error")