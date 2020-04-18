from ..ficheros.codigo import Generador
from firebase_admin import db,auth
generador = Generador()
class Validaciones:
    def validar_json(self,request):
        try:
            request.json
            return True,''
        except:
            codigo = generador.validarGuardarInformacionError("000","validar si lleva json la consulta- no se enviaron json- validaciones","post",'')
            return False,codigo

    def validar_uid_token(self,uid,token):
        if uid == token:
            return True,'' 
        else:
            codigo = generador.validarGuardarInformacionError("000","validar  token corresponda a uid- token no corresponde a uid- validaciones","post",'')
            return False,codigo       

    def validar_tipo_admin(self,uid):
        try:
            datos = db.reference('geoADMIN').order_by_child('user_uid').get()
            if datos['user_uid'] == uid:
                    return True,''
            else:
                codigo = generador.validarGuardarInformacionError("000","validar permiso admin- usuario no tiene permiso de admin- validaciones","post",'')
                return False,codigo
            
        except Exception as e :
            print(e)
            codigo = generador.validarGuardarInformacionError("000","validar permiso admin- ocurrio un error- validaciones","post",'')
            return False,codigo

    def validar_tipo_admin_gerente(self,uid):
        try:
            datos = db.reference('geoADMIN').order_by_child('user_uid').get()
            if datos['user_uid'] == uid:
                    return True,''
            else:
                datos = db.reference('geoGERENTE').child(uid).get()
                if datos != None:
                        return True,''
                else:
                    codigo = generador.validarGuardarInformacionError("000","validar permiso admin o gerente - usuario no posee permiso de admin o gerente- validaciones","post",'')
                    return False,codigo
            
        except Exception as e :
            codigo = generador.validarGuardarInformacionError("000","validar permiso admin- ocurrio un error- validaciones","post",'')
            return False,codigo
            
        except Exception as e :
            print(e)
            codigo = generador.validarGuardarInformacionError("000","validar permiso admin- ocurrio un error- validaciones","post",'')
            return False,codigo             
    def validar_email_telefono(self,email,telefono):
        estado_email,codigo_email=self.validar_email(email)
        if estado_email:
            estado_telefono,codigo_telefono=self.validar_phone(telefono)
            if estado_telefono:
                return estado_telefono,''
            else:
                return False,codigo_telefono    
        else:
            return False,codigo_email 

    def validar_email(self, email):
        try:
            auth.get_user_by_email(email)
            codigo = generador.validarGuardarInformacionError('000','validar email si existe - email si existe - validaciones','post','')
            return False, codigo
        except Exception as a:
            print(a)
            return True, None

    def validar_phone(self, phone):
        try:
            auth.get_user_by_phone_number('+57'+str(phone))
            codigo = generador.validarGuardarInformacionError('000','validar telefono si existe - telefono si existe - validaciones','post','')
            return False, codigo
        except:
            return True, None       