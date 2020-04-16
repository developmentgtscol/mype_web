from mype.controller.registrar_controller import RegistrarController
registrar=RegistrarController()
class RegistroView:
    def registrar_usuario_admin(self,request):
        respuesta=registrar.registrar_usuario_adm(request)
        return respuesta
    