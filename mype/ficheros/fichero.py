# libretias necesarias
import os.path
import math
import pandas as pd
from datetime import datetime

# clases necesarias
from .gestion_de_archivos import Archivo

# variable gloval
ahora = datetime.now()

# clase para escribir o guardar en el fichero
class Fichero:
  # Escritura en el fichero
  def write(self, clave, codigo_http, descripcion, metodo, tipo):
    # datos a guardar
    data = {
      'clave':[clave],
      'codigo_http':[codigo_http],
      'descripcion':[descripcion],
      'metodo':[metodo],
      'tipo_usuario':[tipo],
      'fecha':[ahora.strftime('%x')],
      'hora':[ahora.strftime('%X')]
    }
    # clase para decidir en que archivo de guarda los datos 
    archivos = Archivo()
    nombre = archivos.asignar_archivo(r'C:\Mundo\proyectos_python\proyecto-mype\mype\ficheros\scripts')
    # sacar la columna clave para verifica si la clave esta repetida y tomar el error
    try:
<<<<<<< HEAD
      file = pd.read_csv(r'D:\Documentos\Geomatic\G_Del1\mype\ficheros\scripts\fichero_1.csv', sep=';', names=['clave', 'codigo_http', 'descripcion', 'metodo', 'tipo', 'fecha', 'hora'])
=======
      file = pd.read_csv(r'C:\Mundo\proyectos_python\proyecto-mype\mype\ficheros\scripts\fichero_1.csv', sep=';', names=['clave', 'codigo_http', 'descripcion', 'metodo', 'tipo', 'fecha', 'hora'])
>>>>>>> 1c981bd54011b2fa60b3c6790b2fd47c9c31d399
      lista = list(file['clave'])
      clave = int(clave)
      count = lista.count(clave)
    except:
       # guardar el archivo
      df = pd.DataFrame(data)
<<<<<<< HEAD
      df.to_csv(r'D:\Documentos\Geomatic\G_Del1\mype\ficheros\scripts\{}'.format(nombre), mode='a+', index=False, header=False, sep=';', decimal=',')
=======
      df.to_csv(r'C:\Mundo\proyectos_python\proyecto-mype\mype\ficheros\scripts\{}'.format(nombre), mode='a+', index=False, header=False, sep=';', decimal=',')
>>>>>>> 1c981bd54011b2fa60b3c6790b2fd47c9c31d399
      return True
    # validar que no exista codigo
    if count == 0:
      # guardar el archivo
      df = pd.DataFrame(data)
<<<<<<< HEAD
      df.to_csv(r'D:\Documentos\Geomatic\G_Del1\mype\ficheros\scripts\{}'.format(nombre), mode='a+', index=False, header=False, sep=';', decimal=',')
=======
      df.to_csv(r'C:\Mundo\proyectos_python\proyecto-mype\mype\ficheros\scripts\{}'.format(nombre), mode='a+', index=False, header=False, sep=';', decimal=',')
>>>>>>> 1c981bd54011b2fa60b3c6790b2fd47c9c31d399
      return True
    else:
      return False

  # Lectura en el fichero
  def read(self):
<<<<<<< HEAD
    df = pd.read_csv(r'D:\Documentos\Geomatic\G_Del1\mype\ficheros\scripts\fichero.csv', sep=';', names=['clave', 'codigo_http', 'descripcion', 'metodo', 'tipo', 'fecha', 'hora'])
=======
    df = pd.read_csv(r'C:\Mundo\proyectos_python\proyecto-mype\mype\ficheros\scripts\fichero.csv', sep=';', names=['clave', 'codigo_http', 'descripcion', 'metodo', 'tipo', 'fecha', 'hora'])
>>>>>>> 1c981bd54011b2fa60b3c6790b2fd47c9c31d399
    print(df)

# c = Fichero()
# c.write(12312312,200,'djfjf','post','admin')
# c.write(12312312,200,'djfjf','post','admin')
# c.read()