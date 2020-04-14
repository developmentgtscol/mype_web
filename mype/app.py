from flask import Flask,request,jsonify
from mype.view.ejemplo import vista_de_ejemplo
from mype.view.login_view import login_view
from mype.setting.conexion import Conexion

Conexion()


app = Flask(__name__)

@app.route('/login/',methods=['POST'])

def login():
  respuesta=login_view(request);
  return respuesta

# iniciador
if __name__ == '__main__':
   app.run('0.0.0.0', 5000, debug=True)

