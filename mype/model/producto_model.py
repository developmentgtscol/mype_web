from firebase_admin import db
from mype.ficheros.codigo import Generador
class ProductoModel:
    def registrar_producto(self,datos):
        try:
            datos_guardar = {
                'nombre_producto':datos['nombre_producto'],
                'referencia_producto':datos['referencia_producto'],
                'precio_producto':datos['precio_producto'],
                'cantidad_producto':datos['cantidad_producto'],
                'uid_tienda_asignada':datos['uid_tienda_asignada'],
                'producto_imagen':datos['producto_imagen'],
                'descripción':datos['descripción'],
                'uid_user_registra':datos['uid_usuario']
                }
            ref = db.reference()
            ref.child('geoPRODUCTO').push(datos_guardar)

            return True,''
        except Exception as e :
            print(e)
            generator = Generador()
            codigo = generator.validarGuardarInformacionError('000','guardar producto','post','')
            return False,codigo

    def solicitar_producto(self,uid_tienda):
        try:
            ref = db.reference()
            datos=ref.child("geoPRODUCTO").order_by_child('uid_tienda_asignada').equal_to(uid_tienda).get()
            print(len(datos))
            if len(datos)!=0:
                dato=[]
                for k,v in datos.items():
                    producto={
                        'key':k,
                        'nombre':v['nombre_producto'],
                        'precio':v['precio_producto'],
                        'imagen':v['producto_imagen'],
                        'referencia':v['referencia_producto']
                    }
                    dato.append(producto)

                return True,dato
            else:
                generator = Generador()
                codigo = generator.validarGuardarInformacionError('000','solicitar producto - tienda no tiene productos disponibles- productos model','post','')
                return False,codigo         
        except Exception as e :
            print(e)
            generator = Generador()
            codigo = generator.validarGuardarInformacionError('000','solicitar producto','post','')
            return False,codigo     


             