from mype.controller.asignar_controller import AsignarController
asignar_controller=AsignarController()
class AsignarView:
    def asignar_tienda(self,request):
        respuesta=asignar_controller.asignar_tienda(request)
        return respuesta