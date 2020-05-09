from validator import Required, Equals,  validate
from ficheros.codigo import Generador
generador = Generador()
class HeaderController:
    def validar_header(self,header):
        rules = {
          "Authorization": [Required],
          "Content-Type": [Required,Equals('application/json')]
        }
        respuesta=validate(rules, header)
        if respuesta[0]:
            return True,''
        else:
            codigo = generador.validarGuardarInformacionError("000","validar header- no se enviaron todo los parametros- header_controller","post",'')    
            return False ,codigo
        