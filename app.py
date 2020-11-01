from flask import Flask, render_template
from libs import getNodeInfo
from libs import getPodInfo
from libs import getLimitInfo

app = Flask(__name__)

podsinfo = getPodInfo.getpodinfo()
nodesinfo = getNodeInfo.getnodeinfo()
limitsinfo = getLimitInfo.getlimitinfo()

@app.route('/')
def index():
    return render_template('index.html', pods=podsinfo, nodes = nodesinfo, limits = limitsinfo)

if __name__ == '__main__':
    app.run(debug=True, port=8080)