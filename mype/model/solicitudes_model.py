from firebase_admin import db
from mype.ficheros.codigo import Generador
class SolicitudesModel:
    def solicitudes_admin_gerente(self,uid,tipo):
        try:
            ref = db.reference()
            if tipo =='LISTA_ADMIN_TIENDAS':
                datos=ref.child('geoADMIN_TIENDAS').get()
                if datos!=None:
                    print(datos.values())
                    return True,datos
            elif tipo == 'LISTA_TIENDAS':
                datos=ref.child('geoTIENDAS').get()
                if datos!=None:
                    print(datos.values())
                    return True,datos
            else:
                generator = Generador()
                codigo = generator.validarGuardarInformacionError('000','solicitudes admin- gerente','','')
                return False,codigo   
        except :
            generator = Generador()
            codigo = generator.validarGuardarInformacionError('000','solicitudes admin- gerente','','')
            return False,codigo         