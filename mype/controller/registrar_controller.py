from mype.controller.header_controller import HeaderController
from validator import Required, Equals,  validate,In,Pattern
from mype.model.token_model import Token
from mype.clases.validaciones import Validaciones
from ..ficheros.codigo import Generador
from mype.model.registrar_model import RegistrarModel
header_controller=HeaderController()
verificartoken=Token()
validaciones=Validaciones();
generador = Generador()
class RegistrarController:
    def registrar_usuario_adm(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_usuario": [Required],
                    "nombre_usuario_registrar": [Required],
                    "apellido_usuario_registrar":[Required],
                    "telefono_usuario_registrar":[Required],
                    "correo_usuario_registrar":[Required],
                    "password_usuario_registrar":[Required],
                    "tipo_usuario_registrar":[Required,In(["GERENTE","ADMIN_TIENDAS"])]
                    }
                    respuesta=validate(rules, request.json)
                    if(respuesta[0]):
                        estado_vacio,codigo_vacio=validaciones.validar_campos_vacios(request.json)
                        if estado_vacio:
                            uid_usuario=request.json['uid_usuario']
                            estado_uid_token,codigo_uid_token=validaciones.validar_uid_token(uid_usuario,token)
                            if estado_uid_token: 
                                correo_usuario=request.json['correo_usuario_registrar']
                                telefono_usuario=request.json['telefono_usuario_registrar']
                                estado_email_telefono,codigo_email_telefono=validaciones.validar_email_telefono(correo_usuario,telefono_usuario)
                                if estado_email_telefono:
                                    tipo_usuario=request.json['tipo_usuario_registrar']
                                    if tipo_usuario == 'GERENTE' :
                                        estado_permisoadmin,codigo_permisoadmin=validaciones.validar_tipo_admin(uid_usuario)
                                        if estado_permisoadmin:
                                            registrar_model=RegistrarModel()
                                            estado_registrar,codigo_registrar=registrar_model.registrar_usuario_cliente(request.json,tipo_usuario)
                                            if estado_registrar:
                                                return {'estado':estado_registrar,'mensaje':'registro existoso'}
                                            else:
                                                {'estado':False,'codigo':codigo_registrar}
                                        else:
                                            return {'estado':False,'codigo':codigo_permisoadmin}
                                    elif tipo_usuario == 'ADMIN_TIENDAS':
                                        estado_permisoadmingerente,codigo_permisoadmingerente=validaciones.validar_tipo_admin_gerente(uid_usuario)
                                        if estado_permisoadmingerente:
                                            registrar_model=RegistrarModel()
                                            estado_registrar,codigo_registrar=registrar_model.registrar_usuario_cliente(request.json,tipo_usuario)
                                            if estado_registrar:
                                                return {'estado':estado_registrar,'mensaje':'registro existoso'}
                                            else:
                                                {'estado':False,'codigo':codigo_registrar}
                                        else:
                                            return {'estado':False,'codigo':codigo_permisoadmingerente}
                                else:
                                    return {'estado':False,'codigo':codigo_email_telefono}
                            
                            else:
                                return {'estado':False,'codigo':codigo_uid_token}
                        else:
                            return {'estado':False,'codigo':codigo_vacio}   
                    else:
                        codigo = generador.validarGuardarInformacionError("000","validar si trae los parametros necesario- no se enviaron los parametros- registrar_controller","post",'')
                        return {'estado':False,'codigo':codigo}
                else:
                    return {'estado':False,'codigo':codigo_json}
            else:
                return {'estado':False,'codigo':codigo_token}
        else:
            return {'estado':False,'codigo':codigo_header}

    def registrar_tienda(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_usuario": [Required],
                    "nombre_tienda_registrar": [Required],
                    "ubicacion_tienda":[Required],
                    }
                    respuesta=validate(rules, request.json)
                    if(respuesta[0]):
                        estado_vacio,codigo_vacio=validaciones.validar_campos_vacios(request.json)
                        if estado_vacio:
                            uid_usuario=request.json['uid_usuario']
                            estado_uid_token,codigo_uid_token=validaciones.validar_uid_token(uid_usuario,token)
                            if estado_uid_token:
                                estado_permisoadmingerente,codigo_permisoadmingerente=validaciones.validar_tipo_admin_gerente(uid_usuario) 
                                if estado_permisoadmingerente:
                                    registrar_model=RegistrarModel()
                                    estado_registrar,codigo_registrar=registrar_model.registrar_tienda(request.json)
                                    if estado_registrar:
                                        return  {'estado':True,'mensaje':'registro exitoso'}
                                    else:
                                        return  {'estado':False,'codigo':codigo_registrar}
                                else:
                                    return {'estado':False,'codigo':codigo_permisoadmingerente}
                            else:
                                
                                return {'estado':False,'codigo':codigo_uid_token}
                        else:
                            return {'estado':False,'codigo':codigo_vacio}
                    else:
                        codigo = generador.validarGuardarInformacionError("000","validar si trae los parametros necesario- no se enviaron los parametros- registrar_controller","post",'')
                        return {'estado':False,'codigo':codigo}
                else:
                    return {'estado':False,'codigo':codigo_json}
            else:
                return {'estado':False,'codigo':codigo_token}
        else:
            return {'estado':False,'codigo':codigo_header}

    def registrar_cliente(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            estado_json,codigo_json=validaciones.validar_json(request)
            if estado_json:
                rules = {
                "nombre_cliente": [Required],
                "apellido_cliente": [Required],
                "telefono_cliente":[Required],
                "correo_cliente":[Required],
                "cedula_cliente":[Required],
                "password_cliente":[Required],
                }
                respuesta=validate(rules, request.json)
                if(respuesta[0]):
                    estado_vacio,codigo_vacio=validaciones.validar_campos_vacios(request.json)
                    if estado_vacio:
                        correo_cliente=request.json['correo_cliente']
                        telefono_cliente=request.json['telefono_cliente']
                        estado_email_telefono,codigo_email_telefono=validaciones.validar_email_telefono(correo_cliente,telefono_cliente)
                        if estado_email_telefono:
                                registrar_model=RegistrarModel()
                                estado_registrar,codigo_registrar=registrar_model.registrar_cliente(request.json)
                                if estado_registrar:
                                    return  {'estado':True,'mensaje':'registro exitoso'}
                                else:
                                    return  {'estado':False,'codigo':codigo_registrar}
                        else:
                            return {'estado':False,'codigo':codigo_email_telefono}
                    else:
                        return {'estado':False,'codigo':codigo_vacio}
                else:
                    codigo = generador.validarGuardarInformacionError("000","validar si trae los parametros necesario- no se enviaron los parametros- registrar_controller","post",'')
                    return {'estado':False,'codigo':codigo}
            else:
                return {'estado':False,'codigo':codigo_json}
        else:
            return {'estado':False,'codigo':codigo_header}
           
        
    
