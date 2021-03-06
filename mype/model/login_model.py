from firebase_admin import db
from ficheros.codigo import Generador

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
                    codigo = generador.validarGuardarInformacionError("000","validar login adm_tienda- usuario no existe o no permitido para este login- login_model","post",'')
                    return False,codigo
            elif tipo_cliente == 'ADMIN_TIENDAS':
                datos = db.reference('geo'+tipo_cliente).child(uid).get()
                if datos != None:
                    datos_2=db.reference('geoTIENDAS').order_by_child('admin-tienda_asignado').equal_to(uid).get()
                    if len(datos_2) !=0:
                        for m in datos_2:
                            return True,m
                    else:
                        return True,'usted no tiene tienda asignada'        
                else:
                    codigo = generador.validarGuardarInformacionError("000","validar login admin tienda- usuario no existe o no permitido para este login- login_model","post",'')
                    return False,codigo
            elif tipo_cliente == 'CLIENTES':
                datos = db.reference('geoCLIENTES').child(uid).get()
                print('ad')
                if datos != None:
                        return True,''
                else:
                    codigo = generador.validarGuardarInformacionError("000","validar login clientes- usuario no existe o no permitido para este login- login_model","post",'')
                    return False,codigo
            
        except Exception as e :
            print(e)
            codigo = generador.validarGuardarInformacionError("000","validar login- ocurrio un error- login_model","post",'')
            return False,codigo
        