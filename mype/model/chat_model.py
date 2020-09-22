from firebase_admin import db
from ficheros.codigo import Generador
generador = Generador()
class ChatModel:
    def guardar_mensaje_cliente(self,datos):
        try:
            ref=db.reference()

            mensaje1={
                'de':datos['uid_cliente'],
                'para':'soporte',
                'mensaje':datos['mensaje_cliente'],
                'timestamp':{'.sv': 'timestamp'}
            }
            ref.child('geoMENSAJES').child(datos['uid_cliente']).push(mensaje1)
            mensaje2={
                'ultimo-mensaje':datos['mensaje_cliente'],
                'timestamp':{'.sv': 'timestamp'}
            }
            ref.child('geoCHAT').child(datos['uid_cliente']).set(mensaje2)
            return True ,''
        except :
            codigo = generador.validarGuardarInformacionError("000","ocurrio un error en chat","",'')
            return False,codigo


    def guardar_mensaje_soporte(self,datos):
        try:
            ref=db.reference()

            mensaje1={
                'de':datos['uid_usuario'],
                'para':datos['uid_cliente'],
                'mensaje':datos['mensaje_usuario'],
                'timestamp':{'.sv': 'timestamp'}
            }
            ref.child('geoMENSAJES').child(datos['uid_cliente']).push(mensaje1)
            mensaje2={
                'ultimo-mensaje':datos['mensaje_usuario'],
                'timestamp':{'.sv': 'timestamp'}
            }
            ref.child('geoCHAT').child(datos['uid_cliente']).set(mensaje2)
            return True ,''
        except :
            codigo = generador.validarGuardarInformacionError("000","ocurrio un error en chat","",'')
            return False,codigo
        
            

        