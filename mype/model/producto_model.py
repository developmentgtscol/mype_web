from firebase_admin import db
from  ficheros.codigo import Generador
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

    def solicitar_producto(self):
        try:
            ref = db.reference()
            datos=ref.child("geoPRODUCTO").get()
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
            generator = Generador()
            codigo = generator.validarGuardarInformacionError('000','solicitar producto','post','')
            return False,codigo 

    def solicitar_producto_cliente(self):
        try:
            ref = db.reference()
            datos=ref.child("geoPRODUCTO").order_by_child('uid_tienda_asignada').get()
            if len(datos)!=0:
                dato=[]
                for k,v in datos.items():
                    producto={
                        'key':k,
                        'nombre':v['nombre_producto'],
                        'precio':v['precio_producto'],
                        'imagen':v['producto_imagen'],
                        'referencia':v['referencia_producto'],
                        'tienda':v['uid_tienda_asignada']
                    }
                    dato.append(producto)
                zona1=[(10.99474,-74.78343),(11.00338,-74.78591),(11.00982,-74.79145),(11.01434,-74.79428),(11.00726,-74.79969),(11.00225,-74.80638),(10.99786,-74.80295),(10.99891,-74.80162),(10.99297,-74.79149)]
                zona2=[(11.01434,-74.79428),(11.02578,-74.80297),(11.02073,-74.80709),(11.0139,-74.80915),(11.0086,-74.81413),(11.00514,-74.81121),(11.00225,-74.80638),(11.00726,-74.79969)]
                return True,dato
            else:
                generator = Generador()
                codigo = generator.validarGuardarInformacionError('000','solicitar producto - tienda no tiene productos disponibles- productos model','post','')
                return False,codigo         
        except Exception as e :
            print(e)
            generator = Generador()
            codigo = generator.validarGuardarInformacionError('000','solicitar producto cliente','post','')
            return False,codigo               


             