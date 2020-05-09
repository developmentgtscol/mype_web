from firebase_admin import db, auth
from ficheros.codigo import Generador
class RegistrarModel:
    def registrar_usuario_cliente(self,datos,ruta):
        try:
            user = auth.create_user(email=datos['correo_usuario_registrar'],
             phone_number="+57"+datos['telefono_usuario_registrar'],
            display_name=datos['nombre_usuario_registrar'],
             password=datos['password_usuario_registrar'])
            
            datos_guardar = {
                'uid_user_registra':datos['uid_usuario'],
                'uid_user':user.uid,
                'nombre_gerente':datos['nombre_usuario_registrar'],
                'apellido_gerente':datos['apellido_usuario_registrar'],
                'telefono_usuario':datos['telefono_usuario_registrar'],
                'correo_usuario':datos['correo_usuario_registrar'],
                }
            ref = db.reference()
            ref.child('geo'+ruta).child(user.uid).set(datos_guardar)

            return True,''
        except Exception as e:
            print(e)
            generator = Generador()
            codigo = generator.validarGuardarInformacionError('000','crear usuario','POST','admin')
            return False,codigo

    def registrar_tienda(self,datos):
        try:
            datos_guardar = {
                'uid_user_registra':datos['uid_usuario'],
                'nombre_sede_tienda':datos['nombre_tienda_registrar'],
                'latitud_tienda':datos['latitud_tienda'],
                'longitud_tienda':datos['longitud_tienda'],
                'zona_influencia':datos['zona_influencia'],
                'estado_disponibilidad':True,
                'admin-tienda_asignado':''
                }
            ref = db.reference()
            ref.child('geoTIENDAS').push(datos_guardar)
            return True,''
        except Exception as e:
            print(e)
            generator = Generador()
            codigo = generator.validarGuardarInformacionError('000','crear usuario','POST','admin')
            return False,codigo    

    def registrar_cliente(self,datos):
            try:
                user = auth.create_user(email=datos['correo_cliente'],
                phone_number="+57"+datos['telefono_cliente'],
                display_name=datos['nombre_cliente'],
                password=datos['password_cliente'])
                
                datos_guardar = {
                    'nombre_cliente':datos['nombre_cliente'],
                    'cedula_cliente':datos['cedula_cliente'],
                    'apellido_cliente':datos['apellido_cliente'],
                    'telefono_cliente':datos['telefono_cliente'],
                    'correo_cliente':datos['correo_cliente'],
                    }
                ref = db.reference()
                ref.child('geoCLIENTES').child(user.uid).set(datos_guardar)

                return True,''
            except Exception as e:
                print(e)
                generator = Generador()
                codigo = generator.validarGuardarInformacionError('','crear cliente','','')
                return False,codigo          