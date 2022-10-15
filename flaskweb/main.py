from flask import Flask, jsonify, render_template, request
import webbrowser
import socket

app = Flask(__name__)


################

@app.route('/_con')
def consulta():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    clientSocket.connect(("127.0.0.1", 9091));

    dataFromServer = clientSocket.recv(512);

    return (dataFromServer.decode());

# Envia por GET la información del socket anterior.
@app.route('/_stuff', methods = ['GET'])
def stuff():
    return jsonify(result=consulta())

################


# Render de plantillas

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pcontrol')
def pcontrol():
    return render_template('pcontrol.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

################

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)