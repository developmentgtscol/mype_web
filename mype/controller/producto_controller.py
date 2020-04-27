from mype.controller.header_controller import HeaderController
from validator import Required, Equals,  validate,In,Pattern
from mype.model.token_model import Token
from mype.clases.validaciones import Validaciones
from mype.model.producto_model import ProductoModel
from ..ficheros.codigo import Generador
header_controller=HeaderController()
verificartoken=Token()
validaciones=Validaciones();
generador = Generador()
class ProductoController:
    def registrar_producto(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_usuario":[Required],
                    "nombre_producto": [Required],
                    "referencia_producto":[Required],
                    "precio_producto":[Required],
                    "cantidad_producto":[Required],
                    "uid_tienda_asignada":[Required],
                    "producto_imagen":[Required],
                    "descripción":[Required]
                    }
                    respuesta=validate(rules, request.json)
                    if(respuesta[0]):
                        estado_vacio,codigo_vacio=validaciones.validar_campos_vacios(request.json)
                        if estado_vacio:
                            uid_usuario=request.json['uid_usuario']
                            estado_uid_token,codigo_uid_token=validaciones.validar_uid_token(uid_usuario,codigo_token)
                            if estado_uid_token:
                                estado_permiso,codigo_permiso=validaciones.validar_permiso_admin_getente_admintienda(uid_usuario)
                                if estado_permiso:
                                    uid_tienda_asignada=request.json['uid_tienda_asignada']
                                    estado_validar_tienda,codigo_validar_tienda=validaciones.validar_uid_tienda_existe(uid_tienda_asignada)
                                    if estado_validar_tienda:
                                        referencia_producto=request.json['referencia_producto']
                                        estado_referencia,codigo_referencia=validaciones.validar_referencia_producto(referencia_producto)
                                        if estado_referencia:
                                            producto_model=ProductoModel();
                                            estado_guardar_producto,codigo_guardar_producto=producto_model.registrar_producto(request.json)
                                            if estado_guardar_producto:
                                                return {'estado':estado_guardar_producto,'mensaje':'su producto se guardo con exitoso'}
                                            else:
                                                return {'estado':False,'codigo':codigo_guardar_producto}
                                        else:
                                            return {'estado':False,'codigo':codigo_referencia}
                                    else:
                                        return {'estado':False,'codigo':codigo_validar_tienda}
                                else:
                                     return {'estado':False,'codigo':codigo_permiso}
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

    def solicitar_producto(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_usuario":[Required],
                    "uid_tienda":[Required]
                    }
                    respuesta=validate(rules, request.json)
                    if(respuesta[0]):
                        estado_vacio,codigo_vacio=validaciones.validar_campos_vacios(request.json)
                        if estado_vacio:
                            uid_usuario=request.json['uid_usuario']
                            estado_uid_token,codigo_uid_token=validaciones.validar_uid_token(uid_usuario,codigo_token)
                            if estado_uid_token:
                                estado_permiso,codigo_permiso=validaciones.validar_permiso_admin_getente_admintienda(uid_usuario)
                                if estado_permiso:
                                    uid_tienda=request.json['uid_tienda']
                                    estado_validar_tienda,codigo_validar_tienda=validaciones.validar_uid_tienda_existe(uid_tienda)
                                    if estado_validar_tienda:
                                        producto_model=ProductoModel();
                                        estado_solicitar_producto,codigo_solicitar_producto=producto_model.solicitar_producto(uid_tienda)
                                        if estado_solicitar_producto:
                                            return {'estado':estado_solicitar_producto,'datos':codigo_solicitar_producto}
                                        else:
                                            return {'estado':False,'codigo':codigo_solicitar_producto}
                                    else:
                                        return {'estado':False,'codigo':codigo_validar_tienda}
                                else:
                                     return {'estado':False,'codigo':codigo_permiso}
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
    
    def solicitar_producto_cliente(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_cliente":[Required]
                    }
                    respuesta=validate(rules, request.json)
                    if(respuesta[0]):
                        estado_vacio,codigo_vacio=validaciones.validar_campos_vacios(request.json)
                        if estado_vacio:
                            uid_cliente=request.json['uid_cliente']
                            estado_uid_token,codigo_uid_token=validaciones.validar_uid_token(uid_cliente,codigo_token)
                            if estado_uid_token:
                                estado_permiso,codigo_permiso=validaciones.validar_permiso_cliente(uid_cliente)
                                if estado_permiso:
                                    producto_model=ProductoModel();
                                    estado_solicitar_producto,codigo_solicitar_producto=producto_model.solicitar_producto_cliente()
                                    if estado_solicitar_producto:
                                        return {'estado':estado_solicitar_producto,'datos':codigo_solicitar_producto}
                                    else:
                                        return {'estado':False,'codigo':codigo_solicitar_producto}
                                else:
                                     return {'estado':False,'codigo':codigo_permiso}
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

        

