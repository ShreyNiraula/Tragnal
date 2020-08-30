#from flask import app  #this causes error because it is now package , so import as below
from tragnal2 import app
#from tragnal import manager


def weWillRunFlask():
    # app.run(port=8090, debug=True, threaded = True)
    # app.run(host = '192.168.1.106', port=8090, debuug= True, threaded = True)
    app.run(host = '10.100.31.188', port = 8090, debug=True, threaded = True)
    # app.run(host = '192.168.1.103', port=8090, debug=True, threaded=True)
    # app.run(host='192.168.1.69', port=8090, debug=True, threaded=True)



