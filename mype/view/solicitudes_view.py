from controller.solicitudes_controller import SolictudesController
solicitudes=SolictudesController();
class SolicitudesView:
    def solicitar_lista_admin_tiendas(self,request):
        respuesta=solicitudes.solicitudes_admin_gerente(request,'LISTA_ADMIN_TIENDAS')
        return respuesta

    def solicitar_lista_tiendas(self,request):
        respuesta=solicitudes.solicitudes_admin_gerente(request,'LISTA_TIENDAS')
        return respuesta

    def solicitar_informacion(self,request):
        respuesta=solicitudes.solicitar_informacion(request)
        return respuesta        