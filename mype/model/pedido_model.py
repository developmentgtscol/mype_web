from firebase_admin import db
from datetime import date
import time
from ficheros.codigo import Generador

class PedidoModel:
    def registrar_pedido(self,datos,uid_tienda):
       try:
            ref = db.reference()
            productos=[]
            uid_cliente=datos['uid_cliente']
            total=0
            cantidad_productos=0
            for m in datos['datos_pedidos']:
                total=total+int(m['precio'])
                datos_producto_pedido={
                    'nombre_producto':m['nombre'],
                    'precio_producto':int(m['precio']),
                    'cantidad_producto':m['cantidad'],
                    'key_producto':m['key'],
                    'imagen_producto':m['imagen'] 
                }
                cantidad_productos=cantidad_productos+1;    
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
                        'referencia_pedido_producto':uid_productos_pedido.key,
                        'uid_tienda_pedido_asignado':uid_tienda           
                    }    
            uid_pedido=ref.child('geoPedido').push(datos_pedido)
            return True,'pedido exitoso'
       except Exception as identifier:
           print(identifier)
           generator = Generador()
           codigo = generator.validarGuardarInformacionError('000','registrar pedido','post','')
           return False,codigo
    
    def solicitar_pedidos_tienda(self,uid_tienda):
        try:
            ref = db.reference()
            datos=ref.child('geoPedido').order_by_child('uid_tienda_pedido_asignado').equal_to(uid_tienda).get()
            pedidos=[]
            if len(datos) !=0:
                for k,m in datos.items():
                    datos_2=ref.child('geoPedidoProducto').child(m['referencia_pedido_producto']).get()
                    productos=[]
                    for p in datos_2:
                        producto= {
                            "cantidad_p":p['cantidad_producto'],
                            "imagen":p['imagen_producto'],
                            "key":p['key_producto'],
                            "nombre_p":p['nombre_producto'],
                            "precio_p":p['precio_producto'],
                        }
                        productos.append(producto)
                    pedido={
                        'key':k,
                        'cliente':m['uid_cliente'],
                        'precio':m['total_precio'],
                        'cantidad':m['candidad_productos'],
                        'fecha':m['fecha_pedido'],
                        'hora':m['hora_pedido'],
                        'estado':m['estado_pedido'],
                        'productos':productos
                    }
                    pedidos.append(pedido)
                return True,pedidos    
            else:
                return False,'no tiene pedidos'  
        except Exception as identifier:
            print(identifier)
            generator = Generador()
            codigo = generator.validarGuardarInformacionError('000','solicitar  pedido','post','')
            return False,codigo

    def solicitar_pedidos_cliente(self,uid_cliente):
        try:
            ref = db.reference()
            datos=ref.child('geoPedido').order_by_child('uid_cliente').equal_to(uid_cliente).get()
            pedidos=[]
            if len(datos) !=0:
                for k,m in datos.items():
                    datos_2=ref.child('geoPedidoProducto').child(m['referencia_pedido_producto']).get()
                    productos=[]
                    for p in datos_2:
                        producto= {
                            "cantidad_p":p['cantidad_producto'],
                            "imagen":p['imagen_producto'],
                            "key":p['key_producto'],
                            "nombre_p":p['nombre_producto'],
                            "precio_p":p['precio_producto'],
                        }
                        productos.append(producto)
                    pedido={
                        'key':k,
                        'cliente':m['uid_cliente'],
                        'precio':m['total_precio'],
                        'cantidad':m['candidad_productos'],
                        'fecha':m['fecha_pedido'],
                        'hora':m['hora_pedido'],
                        'estado':m['estado_pedido'],
                        'productos':productos
                    }
                    pedidos.append(pedido)
                return True,pedidos    
            else:
                return False,'no tiene pedidos'  
        except Exception as identifier:
            print(identifier)
            generator = Generador()
            codigo = generator.validarGuardarInformacionError('000','solicitar  pedido cliente','post','')
            return False,codigo                 