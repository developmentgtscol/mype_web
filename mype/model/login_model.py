from firebase_admin import db
from ..ficheros.codigo import Generador

generador = Generador()

class LoginModel:
    def validarlogin(self,uid):
        datos = db.reference('', url="https://gt-123.firebaseio.com/")
        codigo = generador.validarGuardarInformacionError("000","metodo invalido","post",'comercial')
        print(codigo)
        if datos is not None:
                return True,''
        else:
            #codigo=self.generador.validarGuardarInformacionError("403","Usuario no posee permiso","post","undefined")
            return False,'no exite codigo' 
        