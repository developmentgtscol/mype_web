from firebase_admin import auth
from ..ficheros.codigo import Generador


generador = Generador()

class Token:
    def validar_token_fb(self,token):
        try:
            # en esta parte se verifica que el token resivido por parametro es correcto de no ser haci se ejecuta la parte del except del try
            print(token)
            decoded_token = auth.verify_id_token(token)
            
            # en esta parte se toma el uid del usuario que a enviado el token y a sido verificado correctamente
            uid = decoded_token['uid']

            # en esta parte se retornan dos parametros que vienen siendo el primero un True de que indica que fue exitoso la validacion y el otro el uid del usuario
            return True,uid
        except Exception as e:
            print(e)
            codigo = generador.validarGuardarInformacionError("000","validar token- token invalido- token_model","post",'')
            # en esta parte se retorna un parametro que viene siendo el un False que indica que no fue exito la validacion
            return False,codigo
