from mype.controller.header_controller import HeaderController
from validator import Required, Equals,  validate,In,Pattern
from mype.model.token_model import Token
from mype.clases.validaciones import Validaciones
from ..ficheros.codigo import Generador
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
                    "nombre_usuario": [Required],
                    "apellido_usuario":[Required],
                    "telefono_usuario":[Required],
                    "correo_usuario":[Required,Pattern("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")],
                    "password_usuario":[Required],
                    "tipo_usuario":[Required,In(["GERENTE","ADM_TIENDAS"])]
                    }
                    respuesta=validate(rules, request.json)
                    if(respuesta[0]):
                        tipo_cliente=request.json['tipo_cliente']
                        if tipo_cliente == 'GERENTE' :
                            uid_usuario=request.json['uid_usuario']
                            estado_permisoadmin,codigo_permisoadmin=validaciones.validar_tipo_admin(uid_usuario)
                            if estado_permisoadmin:
                                pass
                            else:
                                return False,codigo_permisoadmin
                        elif tipo_cliente == 'ADM_TIENDAS':
                            pass
                    else:
                        codigo = generador.validarGuardarInformacionError("000","validar si trae los parametros necesario- no se enviaron los parametros- registrar_controller","post",'')
                        return {'estado':False,'codigo':codigo}
                else:
                    return False,codigo_json
            else:
                return False,codigo_token
        else:
            return False,codigo_header

        
    
