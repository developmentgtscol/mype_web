from firebase_admin import db
from ficheros.codigo import Generador
class AsignarModel:
    def asignar_tienda(self,datos):
        try:
            ref = db.reference()
            datos=ref.child('geoTIENDAS').update({
    datos['uid_tienda']+'/admin-tienda_asignado':datos['uid_admin_tienda'],
    datos['uid_tienda']+'/estado_disponibilidad': False
})
            return True,''
        except Exception as e:
            print(e)
            generator = Generador()
            codigo = generator.validarGuardarInformacionError('000','asignacion de de tienda','','')
            return False,codigo  
