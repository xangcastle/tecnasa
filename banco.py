from bottle import route, run, template


@route('/')
def index():
    return template('<b>Hola desde nuestro sistema</b>!')


@route('/hello/<name>')
def name(name):
    return template('<b>Hello {{name}}</b>!', name=name)


run(host='localhost', port=8080)
