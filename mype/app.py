from flask import Flask,request,jsonify, make_response
from mype.view.ejemplo import vista_de_ejemplo
from mype.view.login_view import login_view
from mype.setting.conexion import Conexion
from .config import Config
from flask_wtf.csrf import CSRFProtect,generate_csrf,CSRFError

# constructor
config = Config()
iniciar = config.iniciar()
Conexion()


app = Flask(__name__)
app.config.update(iniciar)
csrf = CSRFProtect(app)

@csrf.exempt
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
# iniciador
if __name__ == '__main__':
   app.run('0.0.0.0', 5000, debug=True)

