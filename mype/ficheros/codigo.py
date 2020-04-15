# librerias necesarias 
import random
from random import randrange
from .fichero import Fichero
import random
import string

class Generador:
      
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

    def generate_tabla(self,tipo):
        if tipo == 'general':
            return True,'empresa'
        elif tipo == 'comercial':
            return True,'comercial'
        elif tipo == 'supervisor':
            return True,'supervisor'
        elif tipo == 'vendedor':
            return True, 'vendedor'
        else:
            return False,''

    def generador_de_formato_moneda(self, num, simbolo="US$", n_decimales=2):
        """Convierte el numero en un string en formato moneda
        SetMoneda(45924.457, 'RD$', 2) --> 'RD$ 45,924.46'     
        """
        #con abs, nos aseguramos que los dec. sea un positivo.
        n_decimales = abs(n_decimales)
        
        #se redondea a los decimales idicados.
        num = round(num, n_decimales)

        try:
            #se divide el entero del decimal y obtenemos los string
            num, dec = str(num).split(".")
            #si el num tiene menos decimales que los que se quieren mostrar,
            #se completan los faltantes con ceros.
            dec += "0" * (n_decimales - len(dec))
        except:
            num = str(num)

        #se invierte el num, para facilitar la adicion de comas.
        num = num[::-1]
        
        #se crea una lista con las cifras de miles como elementos.
        l = [num[pos:pos+3][::-1] for pos in range(0,50,3) if (num[pos:pos+3])]
        l.reverse()
        
        #se pasa la lista a string, uniendo sus elementos con comas.
        num = str.join(",", l)
        
        #si el numero es negativo, se quita una coma sobrante.
        try:
            if num[0:2] == "-,":
                num = "-%s" % num[2:]
        except IndexError:
            pass
        
        #si no se especifican decimales, se retorna un numero entero.
        if not n_decimales:
            return "%s %s" % (simbolo, num)
            
        return "%s %s.%s" % (simbolo, num, dec)