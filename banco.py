from bottle import route, run, template


@route('/')
def index():
    return ""


@route('/hello/<name>')
def name(name):
    return template('<b>Hello {{name}}</b>!', name=name)


run(host='localhost', port=8080)
