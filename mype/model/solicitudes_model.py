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