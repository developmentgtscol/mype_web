from firebase_admin import db
from datetime import date
import time
from mype.ficheros.codigo import Generador
class PedidoModel:
    def registrar_pedido(self,datos):
       try:
            ref = db.reference()
            productos=[]
            uid_cliente=datos['uid_cliente']
            cantidad_productos=len(datos)
            for m in datos['datos_pedidos']:
                datos_producto_pedido={
                    'nombre_producto':m,
                    'precio_producto':m,
                    'cantidad_producto':m,
                    'key_producto':m,
                    'imagen_producto':m 
                }
                    
                productos.append(datos_producto_pedido)
            uid_productos_pedido=ref.child('geoPedidoProducto').push(productos)        
            fecha=str(date.today())
            hora=str(time.strftime("%H:%M:%S"))
            datos_pedido={
                        'uid_cliente':uid_cliente,
                        'candidad_productos':cantidad_productos,
                        'total_precio':2541233,
                        'fecha_pedido':fecha,
                        'hora_pedido':hora,
                        'referencia_productos_pedidos':uid_productos_pedido.key           
                    }    
            ref.child('geoPedido').push(datos_pedido)                 
            return True,'pedido exitoso'
       except Exception as identifier:
           print(identifier)
           generator = Generador()
           codigo = generator.validarGuardarInformacionError('000','registrar pedido','post','')
           return False,codigo 