import os
from bottle import route, run, static_file, request, error

@route('/')
def index():
    return "<h1>Skilaverkefni 2</h1>"\
           "<a href='/skilaverkefni2a'>Liður a</a><br>" \
           "<a href='/skilaverkefni2b'>Liður b</a>"

@route('/skilaverkefni2a')
def skilaverkefni2a():
    return "<h1>Skilaverkefni 2A</h1>"\
           "<a href='/skilaverkefni2a/Thor'>Thor<br></a>" \
           "<a href='/skilaverkefni2a/ThorDarkWorld'>Thor The Dark World<br></a>" \
           "<a href='/skilaverkefni2a/ThorRagnarok'>Thor Ragnarok<br></a>" \
           "<br><br><br><a href='/'>Til Baka</a>"

@route('/skilaverkefni2a/<n>')
def param(n):
    return "<h1>Þetta er síða fyrir myndina: "+ n +"</h1>" \
            "<br><a href='/skilaverkefni2a'>Til Baka</a>"

@route('/skilaverkefni2b')
def skilaverkefni2b():
    return "<h1>Skilaverkefni 2B</h1>" \
           "<h2>Veldu uppáhalds myndina þína</h2>" \
           "<a href='/resault?mynd=Thor'><img src='/static/Thor.jpg' height='250' width='250'></a>" \
           "<a href='/resault?mynd=ThorTheDarkWorld'><img src='/static/ThorTheDarkWorld.jpg' height='250' width='250'></a>" \
           "<a href='/resault?mynd=ThorRagnarok'><img src='/static/ThorRagnarok.jpg' height='250' width='250'></a>" \
           "<br><br><a href='/'>Til Baka</a>"

@route('/resault')
def resault():
    mynd = request.query.mynd

    return "<h2>Þú valdir " +mynd+ "</h2>" \
           '<img src="/static/'+mynd+'.jpg">' \
           "<br><br><a href='/skilaverkefni2b'>Til Baka</a>"

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./myndir')

@error(404)
def error404 (error):
    return "<h1>Þessi síða er ekki til</h1>"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))