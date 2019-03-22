from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, abort
import os
from flask import Blueprint
bapp = Blueprint('file', __name__)
@bapp.route('/downfile/<string:interfacename>', methods=['GET'])
def query_planlist(interfacename):
    if request.method == "GET":
       filepath =  interfacename + ".log"
       print("filepath is %s" % filepath)
       if os.path.isfile(os.getcwd() + os.sep +"upload" + os.sep +filepath):
          print("ssss")
          return send_from_directory( os.getcwd() + os.sep +"upload",filepath, as_attachment=True)