#!env/bin/python2.7

from app import app
app.run(debug = True,
        use_debugger = False,
        use_reloader = False,
        host = '0.0.0.0',
        port = 5000)
