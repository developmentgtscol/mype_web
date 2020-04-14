import random
import string
import random
from random import randrange
from mype.ficheros.fichero import Fichero
class Generator:
      
    def __init__(self):
        self.fichero=Fichero()
    # genera la clave del error
    def generate_key(self):
      # numero inicia es el limite menor del rango del numeros y el final es el limite mayor esto es para sacar cuando digitos tendra el numero random
      numero_digitos = randrange(8, 12)
      numero_random = ''
      rango = 10
      # segun sea el numero generado daremos tantas vueltas y en cada guata se le agregara un digito y el numero de esa pisicion al numero final
      contador = 0
      while contador <= numero_digitos:
        rando = random.randrange(rango)
        numero_random = numero_random+str(rando)
        contador = contador + 1
      return numero_random

    def validarGuardarInformacionError(self, codigo_http, descripcion, metodo, tipo):
          # en esta parte se llama la funcion de la clase que guardara el error ocurrido 
          codigo=self.generate_key()
          codigo_valido=self.fichero.write(codigo,codigo_http,descripcion,metodo,tipo)
          while codigo_valido== False:
                codigo=self.generate_key()
                codigo_valido=self.fichero.write(codigo,codigo_http,descripcion,metodo,tipo)
          return codigo    

    def generador_password(self):
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(12))