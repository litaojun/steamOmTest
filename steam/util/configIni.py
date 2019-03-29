import os
import platform
from configparser import ConfigParser
#用例，json格式文件的根目录配置变量
cf = ConfigParser(allow_no_value=True)
cf.read(os.sep.join([os.getcwd() ,"config" , "config.ini"]))
#默认登录手机号，商户手机号，CMS相关管理员运营商户账户配置
phoneCf = ConfigParser(allow_no_value=True)
phoneCf.read(os.sep.join([os.getcwd() ,"config" , "userConfig.ini"]))
#redis配置信息
redisCf = ConfigParser(allow_no_value=True)
redisCf.read(os.sep.join([os.getcwd() ,"config" , "redisConfig.ini"]))
platType = platform.system()
if platType == "Linux" :
   casepath = cf.get('lpath', 'casepath')
   basePath = cf.get('lpath', 'basepath')
   ip       = cf.get('lpath', 'ipStr')
elif platType == "Windows" :
     casepath = cf.get('path','casepath')
     basePath = cf.get('path', 'basepath')
     ip       = cf.get('path', 'ipStr')