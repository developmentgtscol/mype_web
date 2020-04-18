from firebase_admin import db
from ..ficheros.codigo import Generador

generador = Generador()

class LoginModel:
    def validarlogin(self,uid,tipo_cliente):
        try:
            if tipo_cliente == 'ADMIN':
                datos = db.reference('geo'+tipo_cliente).order_by_child('user_uid').get()
                if datos['user_uid'] == uid:
                        return True,''
                else:
                    codigo = generador.validarGuardarInformacionError("000","validar login- usuario no existe o no permitido para este login- login_model","post",'')
                    return False,codigo
            elif tipo_cliente == 'GERENTE':
                datos = db.reference('geo'+tipo_cliente).child(uid).get()
                if datos != None:
                        return True,''
                else:
                    codigo = generador.validarGuardarInformacionError("000","validar login gerente- usuario no existe o no permitido para este login- login_model","post",'')
                    return False,codigo
            elif tipo_cliente == 'ADM_TIENDAS':
                datos = db.reference('geo'+tipo_cliente).child(uid).get()
                if datos != None:
                        return True,''
                else:
                    codigo = generador.validarGuardarInformacionError("000","validar login gerente- usuario no existe o no permitido para este login- login_model","post",'')
                    return False,codigo
            
        except Exception as e :
            print(e)
            codigo = generador.validarGuardarInformacionError("000","validar login- ocurrio un error- login_model","post",'')
            return False,codigo
        