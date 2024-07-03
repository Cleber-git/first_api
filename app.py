from flask import Flask, request, jsonify
import os


app = Flask(__name__)

@app.route('/')

def home():
    return "Bem vindo à sua primeira api com flask!"

@app.route('/data')
def getData():

    data = {
    'nome': 'Cleber',
    'idade': 22,
    'cidade': 'São Paulo'
    }
    data1 = {
    'nome': 'Cleber',
    'idade': 22,
    'cidade': 'São Paulo'
    }
    data2 = {
    'nome': 'Cleber',
    'idade': 22,
    'cidade': 'São Paulo'
    }
    data3 = {
    'nome': 'Cleber',
    'idade': 22,
    'cidade': 'São Paulo'
    }
    data4 = {
    'nome': 'Cleber',
    'idade': 22,
    'cidade': 'São Paulo'               
    }
    j = {'data0': data,
         'data1': data1,
         'data2': data2,
         'data3': data3,
         'data4': data4
         }
    return jsonify(j)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)