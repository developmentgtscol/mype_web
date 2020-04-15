from mype.controller.header_controller import HeaderController
from validator import Required, Equals,  validate
import re
from mype.model.token_model import Token
from mype.model.login_model import LoginModel

class LoginController:
    def validar_login(self,request):
        header_controller=HeaderController()
        login_model=LoginModel()
            
        estado_header,codigo_header=header_controller.valdar_header(request.headers)
        estado_header == False
        if(estado_header):
            token=request.headers['Authorization']
            verificartoken=Token()
            estado_token,codigo_token=verificartoken.validar_token_fb(token)
            if estado_token == False:
                rules = {
                "uid": [Required],
                "tipo_cliente": [Required],
                }
                respuesta=validate(rules, request.json)
                if(respuesta[0]):
                    uid=request.json['uid']
                    estado_login,codigo_model=login_model.validarlogin(uid)
                    if estado_login:
                        return {'estado':True,'codigo':'sixa'}
                    else:
                        return {'estado':False,'codigo':'login1122'}
                    
                else:
                    return {'estado':False,'codigo':'1122campos'}
            else:
                return {'estado':False,'codigo':'1122token'}
        else:
            return {'estado':False,'codigo':'1122header'}

         
    def validar_email(self,correo):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        if  re.match(expresion_regular, correo.lower()):
            return True,''
        else:
           # codigo=self.generador.validarGuardarInformacionError("400","Correo ingresado no tipo email"+correo,"post","undefined")
            return False,'codigo'
    