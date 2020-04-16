from flask import Flask,request,jsonify, make_response
from mype.view.ejemplo import vista_de_ejemplo
from mype.view.login_view import login_view
from mype.view.registro_view import RegistroView
from mype.setting.conexion import Conexion
from .config import Config
from flask_wtf.csrf import CSRFProtect,generate_csrf,CSRFError
from flask_cors import CORS,cross_origin

# constructor
config = Config()
iniciar = config.iniciar()



app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.update(iniciar)
csrf = CSRFProtect(app)

@csrf.exempt
@cross_origin()
@app.route('/login/',methods=['POST'])
def login():
  v=login_view(request);
  if v['estado']==True:
        resp = make_response(v)
        resp.headers['server'] = 'SERVER_NAME'
        resp.headers['X-CSRFToken'] = generate_csrf()
        return resp
  else:
        resp = make_response(v)
        resp.headers['server'] = 'SERVER_NAME'
        return resp      

@app.route('/registrar_usuario_gerente/',methods=['POST'])
def registrar_gerente():
      registro_view=RegistroView()
      respuesta=registro_view.registrar_usuario_admin(request)
      return jsonify(respuesta)

@csrf.exempt
@app.route('/registrar_tienda/',methods=['POST'])
def registrar_tienda():
      registro_view=RegistroView()
      respuesta=registro_view.registrar_tienda(request)
      return jsonify(respuesta)

@csrf.exempt
@app.route('/registrar_cliente/',methods=['POST'])
def registrar_cliente():
      registro_view=RegistroView()
      respuesta=registro_view.registrar_cliente(request)
      return jsonify(respuesta)
# iniciador
if __name__ == '__main__':
   app.run('0.0.0.0', 5000, debug=True)

