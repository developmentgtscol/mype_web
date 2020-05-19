from clases.validaciones import Validaciones
from validator import Required, Equals,  validate,In,Pattern
from model.token_model import Token
from ficheros.codigo import Generador
from controller.header_controller import HeaderController
from model.asignar_model import AsignarModel
header_controller=HeaderController()
verificartoken=Token()
validaciones=Validaciones();
generador = Generador()
class AsignarController:
    def asignar_tienda(self,request):
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if estado_header:
            token=request.headers['Authorization']
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token:
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_usuario": [Required],
                    "uid_admin_tienda":[Required],
                    "uid_tienda":[Required]
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
                                    uid_tienda=request.json['uid_tienda']
                                    estado_tiendaexiste,codigo_tiendaexiste=validaciones.validar_uid_tienda_existe(uid_tienda)
                                    if estado_tiendaexiste:
                                        uid_admintienda=request.json['uid_admin_tienda']
                                        estado_admintiendalibre,codigo_admintiendalibre=validaciones.validar_admintienda_tienetienda(uid_admintienda)
                                        if estado_admintiendalibre:
                                            asignar_model=AsignarModel()
                                            estado_asignar,codigo_asignar=asignar_model.asignar_tienda(request.json)
                                            if estado_asignar:
                                                return  {'estado':True,'mensaje':'asignacion exitosa'}
                                            else:
                                                return  {'estado':False,'codigo':codigo_asignar}
                                        else:
                                            return {'estado':False,'mensaje':codigo_admintiendalibre}
                                    else:
                                        
                                        return {'estado':False,'codigo':codigo_tiendaexiste}
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