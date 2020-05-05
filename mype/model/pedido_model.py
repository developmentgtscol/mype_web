from firebase_admin import db
from datetime import date
import time
from mype.ficheros.codigo import Generador

class PedidoModel:
    def registrar_pedido(self,datos,uid_tienda):
       try:
            ref = db.reference()
            productos=[]
            uid_cliente=datos['uid_cliente']
            total=0
            cantidad_productos=len(datos)
            for m in datos['datos_pedidos']:
                total=total+int(m['precio'])
                datos_producto_pedido={
                    'nombre_producto':m['nombre'],
                    'precio_producto':m['precio'],
                    'cantidad_producto':m['cantidad'],
                    'key_producto':m['key'],
                    'imagen_producto':m['imagen'] 
                }
                    
                productos.append(datos_producto_pedido)
            uid_productos_pedido=ref.child('geoPedidoProducto').push(productos)        
            fecha=str(date.today())
            hora=str(time.strftime("%H:%M:%S"))
            datos_pedido={
                        'uid_cliente':uid_cliente,
                        'candidad_productos':cantidad_productos,
                        'total_precio':total,
                        'fecha_pedido':fecha,
                        'hora_pedido':hora,
                        'estado_pedido':'En tienda',
                        'referencia_productos_pedidos':uid_productos_pedido.key,
                        'uid_tienda_pedido_asignado':uid_tienda           
                    }    
            uid_pedido=ref.child('geoPedido').push(datos_pedido)
            return True,'pedido exitoso'
       except Exception as identifier:
           print(identifier)
           generator = Generador()
           codigo = generator.validarGuardarInformacionError('000','registrar pedido','post','')
           return False,codigo 