from firebase_admin import db
from ficheros.codigo import Generador
class SolicitudesModel:
    def solicitudes_admin_gerente(self,uid,tipo):
        try:
            ref = db.reference()
            if tipo =='LISTA_ADMIN_TIENDAS':
                datos=ref.child('geoADMIN_TIENDAS').get()
                if datos!=None:
                    return True,datos
            elif tipo == 'LISTA_TIENDAS':
                datos=ref.child('geoTIENDAS').get()
                if datos!=None:
                    dato = []
                    for k, v in datos.items():
                        tienda = {
                            'key': k,
                            'nombre': v['nombre_sede_tienda'],
                            'latitud': v['latitud_tienda'],
                            'logintud': v['longitud_tienda'],
                            'estado': v['estado_disponibilidad'],
                            'admin_de_tienda':v['admin-tienda_asignado'],
                        }
                        dato.append(tienda)


                    return True, dato
            else:
                generator = Generador()
                codigo = generator.validarGuardarInformacionError('000','solicitudes admin- gerente','','')
                return False,codigo   
        except :
            generator = Generador()
            codigo = generator.validarGuardarInformacionError('000','solicitudes admin- gerente','','')
            return False,codigo

    def solicitar_informacion(self,uid_usuario):
        ref = db.reference()
        tiendas =[]
        datos1=ref.child('geoTIENDAS').get()
        for k ,v in datos1.items():
            tienda={
                'key':k,
                'estado':v['estado_disponibilidad'],
                'latitud':v['latitud_tienda'],
                'longitud':v['longitud_tienda'],
                'nombre':v['nombre_sede_tienda'],
                'zona':v['zona_influencia'],
                'admin-tienda':v['admin-tienda_asignado']
            }
            tiendas.append(tienda)
        datos2=ref.child('geoTIENDAS').get()    
        respuesta = {
            'tiendas':{
                'total':len(datos1),
                'informacion_tiendas':tiendas
            }
        }    
        return False,respuesta                 