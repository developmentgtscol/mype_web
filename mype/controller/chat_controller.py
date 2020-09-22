from controller.header_controller import HeaderController
from validator import Required, Equals,  validate,In,Pattern
from model.token_model import Token
from clases.validaciones import Validaciones
from ficheros.codigo import Generador
from model.chat_model import ChatModel
header_controller=HeaderController()
verificartoken=Token()
validaciones=Validaciones();
generador = Generador()
class ChatController:
    def chat_mensaje_cliente(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_cliente":[Required],
                    "mensaje_cliente":[Required]
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
                                    chat_model=ChatModel();
                                    estado_chat_cliente,codigo_chat_cliente=chat_model.guardar_mensaje_cliente(request.json)
                                    if estado_chat_cliente:
                                        return {'estado':estado_chat_cliente,'datos':codigo_chat_cliente}
                                    else:
                                        return {'estado':False,'codigo':codigo_chat_cliente}
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



    def chat_mensaje_soporte(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_cliente":[Required],
                    "uid_usuario":[Required],
                    "mensaje_usuario":[Required]
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
                                    chat_model=ChatModel();
                                    estado_chat_cliente,codigo_chat_cliente=chat_model.guardar_mensaje_soporte(request.json)
                                    if estado_chat_cliente:
                                        return {'estado':estado_chat_cliente,'datos':codigo_chat_cliente}
                                    else:
                                        return {'estado':False,'codigo':codigo_chat_cliente}
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