
from flask import Flask
from flask import request

app = Flask(__name__)

#http://127.0.0.1:8000/params?params1=jhasmany
#http://127.0.0.1:8000/params?params1=jhasmany&params2=test_dos

@app.route('/')
def index():
    return 'Hola Mundo fsdfasdfa'

@app.route('/params')
def params():
    param = request.args.get('params1', 'no contiene es parametro')
    param_dos = request.args.get('params2', 'no contiene es parametro')
    return 'El parametro es :{}, {}'.format(param, param_dos)

if __name__ ==  '__main__':
    app.run( debug=True, port=8000)