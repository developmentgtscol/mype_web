from ..ficheros.codigo import Generador
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
            pass 
        else:
            pass       

    def validar_tipo_admin(self,uid):
        try:
            datos = db.reference('geoADMIN').order_by_child('user_uid').get()
            if datos['user_uid'] == uid:
                    return True,''
            else:
                codigo = generador.validarGuardarInformacionError("000","validar permiso admin- usuario no tiene permiso de admin- validaciones","post",'')
                return False,codigo
            
        except :
            codigo = generador.validarGuardarInformacionError("000","validar permiso admin- ocurrio un error- validaciones","post",'')
            return False,codigo

    def validar_tipo_gerente(self,uid):
        try:
            datos = db.reference('geoADMIN').order_by_child('user_uid').get()
            if datos['user_uid'] == uid:
                    return True,''
            else:
                codigo = generador.validarGuardarInformacionError("000","validar permiso admin- usuario no tiene permiso de admin- validaciones","post",'')
                return False,codigo
            
        except :
            codigo = generador.validarGuardarInformacionError("000","validar permiso admin- ocurrio un error- validaciones","post",'')
            return False,codigo             