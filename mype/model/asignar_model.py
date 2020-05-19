from firebase_admin import db
from ficheros.codigo import Generador
class AsignarModel:
    def asignar_tienda(self,datos):
        try:
            ref = db.reference()
            datos=ref.child('geoTIENDAS').child(datos['uid_tienda']).update({
    'admin-tienda_asignado':datos['uid_admin_tienda'],
    'estado_disponibilidad': True,
})
            return True,''
        except Exception as e:
            print(e)
            generator = Generador()
            codigo = generator.validarGuardarInformacionError('000','asignacion de de tienda','','')
            return False,codigo  
