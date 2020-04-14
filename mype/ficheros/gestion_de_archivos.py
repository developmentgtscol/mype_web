# libretias necesarias
import math
import os.path

# clase que valida y crea el archivo donde se guardara la info
class Archivo:
  # metodo que gestiona la validacion y creacion del archivo
  def asignar_archivo(self, carpeta):
    # tomamo la ubicacion de los archivos esto devuelve una lista con los no,bres de los archivos existente
    archivos = [name for name in os.listdir(carpeta)
              if os.path.isfile(os.path.join(carpeta, name))]
    # tomamos la cantida de archivo
    cantidad = len(archivos)
    # validamos que no este vacia y si lo esta creamos un nombre default si no solo tomamos el utimo archivo
    if cantidad == 0:
      nombre = 'fichero_'+str(cantidad + 1)+'.csv'
    else:
      nombre = archivos[-1]

    # buscamos el archivo que filtramos y en caso de no exister tomamos el error y enviamos para que sea creado
    try:
      sizefile = os.path.getsize(carpeta+r'\{}'.format(nombre))
      tamaño_megas = (sizefile / 1024) / 1024
      megas = math.ceil(tamaño_megas)
    except:
      return nombre

    # si existe y pesa menos de 200 megas retornamos ese archivo para que se siga usando si no creamos un nuevo archivo
    if megas <= 200:
      return nombre
    else:
      nombre = 'fichero_'+str(cantidad + 1)+'.csv'
      return nombre