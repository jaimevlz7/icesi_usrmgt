import commands
import json
from flask import Flask
app = Flask(__name__)

@app.route("/")
def usuarios():

	ret=commands.getoutput("ls /home | sort")
	ret=ret.split("\n")
	ret="{users: "+json.dumps(ret)+"}"
	return ret
