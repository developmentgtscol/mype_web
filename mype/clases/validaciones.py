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