from flask import (Flask, jsonify, request, abort, render_template)
import src.calculadora as calc


# inicio flask y app como objeto de servidor
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/sumar', methods=['POST'])
def add_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argumento1']
        arg2 = request.json['argumento2']
        result =  calc.sumar(arg1,arg2)
        return (jsonify({'resultado':float(result)}), 200)
    except KeyError:
        abort(400)

@app.route('/restar', methods=['POST'])
def subtract_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argumento1']
        arg2 = request.json['argumento2']
        result = calc.restar(arg1,arg2)
        return (jsonify({'resultado':float(result)}), 200)
    except KeyError:
        abort(400)

@app.route('/dividir', methods=['POST'])
def multiply_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argumento1']
        arg2 = request.json['argumento2']
        result = calc.dividir(arg1,arg2)
        return (jsonify({'resultado':float(result)}), 200)
    except KeyError:
        abort(400)
    except ZeroDivisionError:
        # ocurre cuando el request ej: log(a,1)
        abort(400)

@app.route('/echo', methods=['POST'])
def log_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argumento1']
        arg2 = request.json['argumento2']
        result = {'argumento1':arg1,'argumento2':arg2}
        return (jsonify({'resultado':result}), 200)
    except KeyError:
        abort(400)
    except ValueError:
        # ocurre cuando el request ej: log(a,0)
        abort(400)

# inicializo el servidor
if __name__ == '__main__':
    app.run(debug=True, port=4000)
