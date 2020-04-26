from mype.clases.validaciones import Validaciones
from validator import Required, Equals,  validate,In,Pattern
from mype.model.token_model import Token
from ..ficheros.codigo import Generador
from mype.model.solicitudes_model import SolicitudesModel
from mype.controller.header_controller import HeaderController
header_controller=HeaderController()
verificartoken=Token()
validaciones=Validaciones();
generador = Generador()
class SolictudesController:
    def solicitudes_admin_gerente(self,request,tipo):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_usuario": [Required],
                    }
                    respuesta=validate(rules, request.json)
                    if(respuesta[0]):
                        estado_vacio,codigo_vacio=validaciones.validar_campos_vacios(request.json)
                        if estado_vacio:
                            uid_usuario=request.json['uid_usuario']
                            estado_uid_token,codigo_uid_token=validaciones.validar_uid_token(uid_usuario, codigo_token)
                            if estado_uid_token:
                                estado_permisoadmingerente,codigo_permisoadmingerente=validaciones.validar_tipo_admin_gerente(uid_usuario)
                                
                                if estado_permisoadmingerente:
                                    solicitudes_model=SolicitudesModel()
                                    estado_solictud,codigo_solicitud=solicitudes_model.solicitudes_admin_gerente(request.json,tipo)
                                    if estado_solictud:
                                        return  {'estado':True,'datos':codigo_solicitud}
                                    else:
                                        return  {'estado':False,'codigo':codigo_solicitud}
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