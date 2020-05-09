from controller.header_controller import HeaderController
from validator import Required, Equals,  validate,In
import re
from model.token_model import Token
from model.login_model import LoginModel
from clases.validaciones import Validaciones
from ficheros.codigo import Generador

generador = Generador()
class LoginController:
    def validar_login(self,request):
        header_controller=HeaderController()
        login_model=LoginModel()
            
        estado_header,codigo_header=header_controller.validar_header(request.headers)
        if(estado_header == True):
            token=request.headers['Authorization']
            verificartoken=Token()
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token == True:
                validaciones=Validaciones();
                estado_json,codigo_json=validaciones.validar_json(request)
                if estado_json:
                    rules = {
                    "uid_cliente": [Required],
                    "tipo_cliente": [Required,In(["ADMIN", "GERENTE", "ADMIN_TIENDAS", "CLIENTES"])],
                    }
                    respuesta=validate(rules, request.json)
                    if(respuesta[0]):
                        estado_vacio,codigo_vacio=validaciones.validar_campos_vacios(request.json)
                        if estado_vacio:
                            uid_cliente=request.json['uid_cliente']
                            tipo_cliente=request.json['tipo_cliente']
                            estado_login,codigo_model=login_model.validarlogin(uid_cliente,tipo_cliente)
                            if estado_login:
                                if tipo_cliente == 'ADMIN_TIENDAS':
                                     return {'estado':True,'mensaje':'login exitoso','uid_tienda':codigo_model}
                                else:
                                     return {'estado':True,'mensaje':'login exitoso'}
                            else:
                                return {'estado':False,'codigo':codigo_model}
                        else:
                            return {'estado':False,'codigo':codigo_vacio}
                        
                        
                    else:
                        codigo = generador.validarGuardarInformacionError("000","validar si trae los parametros necesario- no se enviaron los parametros- login_controller","post",'')
                        return {'estado':False,'codigo':codigo}
                else:
                    return {'estado':False,'codigo':codigo_json}
            else:
                return {'estado':False,'codigo':codigo_token}
        else:
            return {'estado':False,'codigo':codigo_header}

         
    def validar_email(self,correo):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        if  re.match(expresion_regular, correo.lower()):
            return True,''
        else:
           # codigo=self.generador.validarGuardarInformacionError("400","Correo ingresado no tipo email"+correo,"post","undefined")
            return False,'codigo'
    