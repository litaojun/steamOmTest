#!/usr/bin/env python  
# encoding: utf-8  
from flask import Flask
from steam.runflask.outapi import interfaceMnr,testcaseRun,reportQuery,timerCheckData
from flask_cors import *
from steam.mockhttp.util.initFile import ip
# import sys
from flask import render_template
# sys.path.append("/home/nicepy/testhome/unittestExBaseb")
app = Flask(__name__,template_folder='templates',static_url_path='/static/')
CORS(app, supports_credentials=True)
app.register_blueprint( interfaceMnr.bapp,       url_prefix = "/infcs"   )
app.register_blueprint( testcaseRun.bapp,        url_prefix = "/tsrun"   )
app.register_blueprint( reportQuery.bapp,        url_prefix = "/rptqy"   )
app.register_blueprint( timerCheckData.bapp,     url_prefix = "/timer" )

@app.route('/', methods=['GET'])
def hello_world():
    return render_template( "pytest.html", content="hello flask " )

@app.route('/local', methods=['GET'])
def hello_world_local():
    return render_template( "pytestlocal.html", ipStr = ip )

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=True,port=8181)