from mype.controller.solicitudes_controller import SolictudesController
solicitudes=SolictudesController();
class SolicitudesView:
    def solicitar_lista_admin_tiendas(self,request):
        respuesta=solicitudes.solicitudes_admin_gerente(request)
        return respuesta