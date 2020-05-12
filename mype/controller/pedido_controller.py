from controller.header_controller import HeaderController
from validator import Required, Equals,  validate,In,Pattern
from model.token_model import Token
from clases.validaciones import Validaciones
from model.pedido_model import PedidoModel
from ficheros.codigo import Generador
from clases.zona_influencia import ZonaInfluencia
header_controller=HeaderController()
verificartoken=Token()
validaciones=Validaciones();
generador = Generador()
class PedidoController:
    def registrar_pedido(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    #request.json['datos_pedidos']=[{"nombre": "Los frutos", "precio": "14523", "cantidad": 1, "key": "-M5xEFjOjUlFivUuZi-c", "imagen": "https://firebasestorage.googleapis.com/v0/b/mype-9c1d1.appspot.com/o/imagenProducto%2Fberries-1546125_1920.jpg?alt=media&token=e9576726-398c-44e9-8f61-29083658b5cb"}, {"nombre": "Piña", "precio": "52312", "cantidad": 1, "key": "-M5xEsEuyiYtRRGGyAjy", "imagen": "https://firebasestorage.googleapis.com/v0/b/mype-9c1d1.appspot.com/o/imagenProducto%2Fraspberries-1426859_1920.jpg?alt=media&token=f8cea9fa-3b1a-47ab-a929-5af0295b25a8"}]

                    rules = {
                    "uid_cliente":[Required],
                    "datos_pedidos":[Required],
                    "latitud_cliente":[Required],
                    "longitud_cliente":[Required]
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
                                    latitud_cliente=request.json['latitud_cliente']
                                    longitud_cliente=request.json['longitud_cliente']
                                    estado_cordenadas,codigo_cordenadas=validaciones.validar_cordenadas(latitud_cliente,longitud_cliente)
                                    if estado_cordenadas:
                                        zona_influencia=ZonaInfluencia()
                                        estado_zona_influencia,codigo_zona_influencia=zona_influencia.solicitar_zona_Influencia(latitud_cliente,longitud_cliente)
                                        if estado_zona_influencia == True:
                                            pedido_model=PedidoModel();
                                            estado_registrar_pedido,codigo_registrar_pedido=pedido_model.registrar_pedido(request.json,codigo_zona_influencia)
                                            if estado_registrar_pedido:
                                                return {'estado':estado_registrar_pedido,'datos':codigo_registrar_pedido}
                                            else:
                                                return {'estado':False,'codigo':codigo_registrar_pedido}
                                        else:
                                            return {'estado':False,'mensaje':codigo_zona_influencia}
                                    else:
                                        return {'estado':False,'codigo':codigo_cordenadas}
                                else:
                                     return {'estado':False,'codigo':codigo_permiso}
                            else:
                                return {'estado':False,'codigo':codigo_uid_token}
                        else:
                            return {'estado':False,'codigo':codigo_vacio}   
                    else:
                        codigo = generador.validarGuardarInformacionError("000","validar si trae los parametros necesario- no se enviaron los parametros- producto_controller","post",'')
                        return {'estado':False,'codigo':codigo}
                else:
                    return {'estado':False,'codigo':codigo_json}
            else:
                return {'estado':False,'codigo':codigo_token}
        else:
            return {'estado':False,'codigo':codigo_header}

    def solicitar_pedido_tienda(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_usuario":[Required],
                    "uid_tienda":[Required],
                    }
                    respuesta=validate(rules, request.json)
                    if(respuesta[0]):
                        estado_vacio,codigo_vacio=validaciones.validar_campos_vacios(request.json)
                        if estado_vacio:
                            uid_usuario=request.json['uid_usuario']
                            estado_uid_token,codigo_uid_token=validaciones.validar_uid_token(uid_usuario,codigo_token)
                            if estado_uid_token:
                                estado_permiso,codigo_permiso=validaciones.validar_permiso_admin_gerente_admintienda(uid_usuario)
                                if estado_permiso:
                                        pedido_model=PedidoModel()
                                        uid_tienda=request.json['uid_tienda']
                                        estado_registrar_pedido,codigo_registrar_pedido=pedido_model.solicitar_pedidos_tienda(uid_tienda)
                                        if estado_registrar_pedido:
                                            return {'estado':estado_registrar_pedido,'datos':codigo_registrar_pedido}
                                        else:
                                            return {'estado':False,'codigo':codigo_registrar_pedido}
                                else:
                                     return {'estado':False,'codigo':codigo_permiso}
                            else:
                                return {'estado':False,'codigo':codigo_uid_token}
                        else:
                            return {'estado':False,'codigo':codigo_vacio}   
                    else:
                        codigo = generador.validarGuardarInformacionError("000","validar si trae los parametros necesario- no se enviaron los parametros- producto_controller","post",'')
                        return {'estado':False,'codigo':codigo}
                else:
                    return {'estado':False,'codigo':codigo_json}
            else:
                return {'estado':False,'codigo':codigo_token}
        else:
            return {'estado':False,'codigo':codigo_header}   


    def solicitar_pedido_cliente(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_cliente":[Required],
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
                                        pedido_model=PedidoModel()
                                        estado_registrar_pedido,codigo_registrar_pedido=pedido_model.solicitar_pedidos_cliente(uid_cliente)
                                        if estado_registrar_pedido:
                                            return {'estado':estado_registrar_pedido,'datos':codigo_registrar_pedido}
                                        else:
                                            return {'estado':False,'codigo':codigo_registrar_pedido}
                                else:
                                     return {'estado':False,'codigo':codigo_permiso}
                            else:
                                return {'estado':False,'codigo':codigo_uid_token}
                        else:
                            return {'estado':False,'codigo':codigo_vacio}   
                    else:
                        codigo = generador.validarGuardarInformacionError("000","validar si trae los parametros necesario- no se enviaron los parametros- producto_controller","post",'')
                        return {'estado':False,'codigo':codigo}
                else:
                    return {'estado':False,'codigo':codigo_json}
            else:
                return {'estado':False,'codigo':codigo_token}
        else:
            return {'estado':False,'codigo':codigo_header}                  


    def solicitar_pedido(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_usuario":[Required],
                    }
                    respuesta=validate(rules, request.json)
                    if(respuesta[0]):
                        estado_vacio,codigo_vacio=validaciones.validar_campos_vacios(request.json)
                        if estado_vacio:
                            uid_usuario=request.json['uid_usuario']
                            estado_uid_token,codigo_uid_token=validaciones.validar_uid_token(uid_usuario,codigo_token)
                            if estado_uid_token:
                                estado_permiso,codigo_permiso=validaciones.validar_permiso_admin_gerente(uid_usuario)
                                if estado_permiso:
                                        pedido_model=PedidoModel()
                                        estado_registrar_pedido,codigo_registrar_pedido=pedido_model.solicitar_pedidos()
                                        if estado_registrar_pedido:
                                            return {'estado':estado_registrar_pedido,'datos':codigo_registrar_pedido}
                                        else:
                                            return {'estado':False,'codigo':codigo_registrar_pedido}
                                else:
                                     return {'estado':False,'codigo':codigo_permiso}
                            else:
                                return {'estado':False,'codigo':codigo_uid_token}
                        else:
                            return {'estado':False,'codigo':codigo_vacio}   
                    else:
                        codigo = generador.validarGuardarInformacionError("000","validar si trae los parametros necesario- no se enviaron los parametros- producto_controller","post",'')
                        return {'estado':False,'codigo':codigo}
                else:
                    return {'estado':False,'codigo':codigo_json}
            else:
                return {'estado':False,'codigo':codigo_token}
        else:
            return {'estado':False,'codigo':codigo_header}           