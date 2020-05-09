from ficheros.codigo import Generador
from firebase_admin import db
generador = Generador()
class ZonaInfluencia:
    def solicitar_zona_Influencia(self,latitud,longitud):
        zona1=[(10.99474,-74.78343),(11.00338,-74.78591),(11.00982,-74.79145),(11.01434,-74.79428),(11.00726,-74.79969),(11.00225,-74.80638),(10.99786,-74.80295),(10.99891,-74.80162),(10.99297,-74.79149)]
        zona2=[(11.01434,-74.79428),(11.02578,-74.80297),(11.02073,-74.80709),(11.0139,-74.80915),(11.0086,-74.81413),(11.00514,-74.81121),(11.00225,-74.80638),(11.00726,-74.79969)]
        zona3=[(11.02578,-74.80297),(11.03121,-74.80859),(11.02598,-74.81794),(11.01385,-74.82653),(11.01166,-74.82129),(11.0086,-74.81413),(11.0139,-74.80915),(11.02073,-74.80709)]
        zona4=[(11.00464,-74.83399),(11.01166,-74.82129),(11.0086,-74.81413),(11.00514,-74.81121),(11.00354,-74.81451),(10.99925,-74.82498)]
        zona5=[(10.99925,-74.82498),(10.98787,-74.80824),(10.99297,-74.79149),(10.99891,-74.80162),(10.99786,-74.80295),(11.00275,-74.80655)]
        zonas=[zona1,zona2,zona3,zona4,zona5]
        num=len(zonas)
        for  i in range(num):
            estado_poligono=self.validar_punto_poligono(latitud,longitud,zonas[i])
            if estado_poligono==True:
                datos = db.reference('geoTIENDAS').order_by_child('zona_influencia').equal_to(i+1).get()
                if len(datos)!=0:
                    for m in datos:
                        return True,m
                else:
                    codigo = generador.validarGuardarInformacionError("000","validar si la zona de influencia tiene una tienda - zona influencia sin tienda- zona_influencia","post",'')
                    return False,codigo
        codigo = generador.validarGuardarInformacionError("000","validar zona de influencia- el cliente no se encuentra en ninguna zona de influencia- zonainfluencia","post",'')
        return {'estado':False,'codigo':codigo}        



    def validar_punto_poligono(self,latitud,longitud,lista_poligono):
        y=longitud
        x=latitud

        poly=lista_poligono

        num = len(poly)
        i = 0
        j = num - 1
        c = False
        for i in range(num):
            if ((poly[i][1] > y) != (poly[j][1] > y)) and \
                    (x < poly[i][0] + (poly[j][0] - poly[i][0]) * (y - poly[i][1]) /
                                    (poly[j][1] - poly[i][1])):
                c = not c
            j = i

        return c