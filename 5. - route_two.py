from flask import Flask
from flask import request

app = Flask(__name__)

#http://127.0.0.1:8000/params?params1=jhasmany
#http://127.0.0.1:8000/params?params1=jhasmany&params2=test_dos

@app.route('/')
def index():
    return 'Hola Mundo fsdfasdfa'

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name='este es un valor por default', num = 'nada'):
    return 'El parametro es :{}{}'.format(name, num)

if __name__ ==  '__main__':
    app.run( debug=True, port=8000)