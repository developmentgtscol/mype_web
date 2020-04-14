import os.path
import math
import pandas as pd
from mype.ficheros.gestion_de_archivos import Archivo
from datetime import datetime
ahora = datetime.now()
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
    nombre = archivos.asignar_archivo(r'D:\Documentos\Geosales\G_Del1\mype\ficheros')
    # sacar la columna clave para verifica si la clave esta repetida y tomar el error
    try:
      file = pd.read_csv(r'D:\Documentos\Geosales\G_Del1\mype\ficheros\fichero_1.csv', sep=';', names=['clave', 'codigo_http', 'descripcion', 'metodo', 'tipo', 'fecha', 'hora'])
      lista = list(file['clave'])
      clave = int(clave)
      count = lista.count(clave)
    except:
       # guardar el archivo
      df = pd.DataFrame(data)
      df.to_csv(r'D:\Documentos\Geosales\G_Del1\mype\ficheros\{}'.format(nombre), mode='a+', index=False, header=False, sep=';', decimal=',')
      return True
    # validar que no exista codigo
    if count == 0:
      # guardar el archivo
      df = pd.DataFrame(data)
      df.to_csv(r'D:\Documentos\Geosales\G_Del1\mype\ficheros\{}'.format(nombre), mode='a+', index=False, header=False, sep=';', decimal=',')
      return True
    else:
      return False

  # Lectura en el fichero
  def read(self):
    df = pd.read_csv(r'C:\Users\GEOMATIC\Desktop\proyecto_final\backend\api\common\fichero.csv', sep=';', names=['clave', 'codigo_http', 'descripcion', 'metodo', 'tipo', 'fecha', 'hora'])
    print(df)