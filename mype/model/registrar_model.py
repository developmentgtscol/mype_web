from firebase_admin import db, auth
from mype.ficheros.codigo import Generador
class RegistrarModel:
    def registrar_usuario_cliente(self,datos,ruta):
        try:
            user = auth.create_user(email=datos['correo_usuario_registrar'],
             phone_number="+57"+datos['telefono_usuario_registrar'],
            display_name=datos['nombre_usuario_registrar'],
            password='password_usuario_registrar')
            
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
                'ubicacion_tienda':datos['ubicacion_tienda']
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
                password='password_cliente')
                
                datos_guardar = {
                    'nombre_cliente':datos['nombre_cliente'],
                    'cedula_cliente':datos['cedula_cliente'],
                    'apellido_cliente':datos['apellido_cliente'],
                    'telefono_cliente':datos['telefono_cliente'],
                    'correo_cliente':datos['correo_cliente'],
                    }
                ref = db.reference()
                ref.child('geoCIENTES').child(user.uid).set(datos_guardar)

                return True,''
            except Exception as e:
                print(e)
                generator = Generador()
                codigo = generator.validarGuardarInformacionError('000','crear cliente','POST','admin')
                return False,codigo          