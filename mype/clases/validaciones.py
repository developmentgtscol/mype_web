from ficheros.codigo import Generador
from firebase_admin import db,auth
import re
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
            return True,codigo       

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
    def validar_campos_vacios(self,valores):
        vueltas=0
        for index, valor in enumerate(valores):
            if valores[valor] == "" or valores[valor] == " ":
                codigo=generador.validarGuardarInformacionError("000","se valida que los valores resivido no sean null -campos null -validaciones","post","undefined")
                vueltas=vueltas+1
                return False,codigo
                
        if vueltas==0:
            return True,'' 
    def validar_uid_tienda_existe(self,uid_tienda):
        try:
            datos = db.reference('geoTIENDAS').child(uid_tienda).get()
            if datos != None:
                    return True,''
            else:
                codigo = generador.validarGuardarInformacionError("000","validar existencia tienda- el uid de tienda enviado no existe- validaciones","post",'')
                return False,codigo
            
        except Exception as e :
            codigo = generador.validarGuardarInformacionError("000","validar existencia tienda- ocurrio un error- validaciones","post",'')
            return False,codigo         
    def validar_referencia_producto(self,referencia):
        try:
            ref=db.reference('geoPRODUCTO')
            datos = ref.order_by_child('referencia_producto').equal_to(referencia).get()
            entro=None
            for key in datos:
                entro=1
            if entro == None:
                return True,''
            else:
                codigo = generador.validarGuardarInformacionError("000","validar referencia producto- referencia producto existe- validaciones","post",'')
                return False,codigo     
        except Exception as e :
            print(e)
            codigo = generador.validarGuardarInformacionError("000","validar referencia producto- ocurrio un error- validaciones","post",'')
            return False,codigo          
    def validar_permiso_admin_getente_admintienda(self,uid):
        try:
            datos = db.reference('geoADMIN').order_by_child('user_uid').get()
            if datos['user_uid'] == uid:
                    return True,''
            else:
                datos = db.reference('geoGERENTE').child(uid).get()
                if datos != None:
                        return True,''
                else:
                    datos = db.reference('geoADMIN_TIENDAS').child(uid).get()
                    if datos !=None:
                        return True,''
                    else:
                        codigo = generador.validarGuardarInformacionError("000","validar permiso admin , gerente o admintienda - usuario no posee permiso de admin , gerente- validaciones","post",'')
                        return False,codigo
            
        except Exception as e :
            codigo = generador.validarGuardarInformacionError("000","validar permiso admin , gerente o admintienda- ocurrio un error- validaciones","post",'')
            return False,codigo  

    def validar_permiso_cliente(self,uid_cliente):
        try:
            datos = db.reference('geoCLIENTES').child(uid_cliente).get()
            if datos != None:
                    return True,''
            else:
                codigo = generador.validarGuardarInformacionError("000","validar permiso cliente- usuario no tiene permiso de cliente- validaciones","post",'')
                return False,codigo  
        except :
            codigo = generador.validarGuardarInformacionError("000","validar permiso cliente- ocurrio un error- validaciones","post",'')
            return False,codigo
    def validar_cordenadas(self,latitud,longitud):
        try:
                return True,''
        except Exception as e :
            print(e)
            codigo = generador.validarGuardarInformacionError("000","validar cordenadas validas2- cordenas erronea- validaciones","post",'')
            return False,codigo
    def validar_zona_influencia(self,zona):
        try:
            datos = db.reference('geoTIENDAS').order_by_child('zona_influencia').equal_to(zona).get()
            if len(datos)==0:
                    return True,''
            else:
                codigo = generador.validarGuardarInformacionError("000","validar si zona de influencia ocupada - zona influencia ocupada- validaciones","post",'')
                return False,codigo              
        except Exception as e :
            print(e)
            codigo = generador.validarGuardarInformacionError("000","validar si zona de influencia ocupada -ocurrio un error servidor- validaciones","post",'')
            return False,codigo                             