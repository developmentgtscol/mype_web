from validator import Required, Equals,  validate

class HeaderController:
    def valdar_header(self,header):
        rules = {
          "Authorization": [Required],
          "Content-Type": [Required,Equals('application/json')],
          "Accept-Charset": [Required,Equals('ISO-8859-1')],
        }
        respuesta=validate(rules, header)
        return  {"estado":respuesta[0],"codigo":respuesta[1]}
        