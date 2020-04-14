# librerias necesarias
import firebase_admin # libreria de firebase para python
from firebase_admin import credentials

# clase de conexion con la configuracion necesaria para conectar a firebase con ese proyecto
class Conexion:
	# constructor
	def __init__(self):
		# pasamo credencial
		cred = credentials.Certificate(r'setting/mype-9c1d1-firebase-adminsdk-4hnvz-095114c5a6.json')
		# iniciar la app de firebase
		firebase_admin.initialize_app(cred, {
			'databaseURL': 'https://geosales-e9e98.firebaseio.com/',
			#'databaseAuthVariableOverride': {
        	#'uid': 'Geosales_Ññ1234'  }
		})