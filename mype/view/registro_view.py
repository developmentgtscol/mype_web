from controller.registrar_controller import RegistrarController
registrar=RegistrarController()
class RegistroView:
    def registrar_usuario_admin(self,request):
        respuesta=registrar.registrar_usuario_adm(request)
        return respuesta

    def registrar_tienda(self,request):
        respuesta=registrar.registrar_tienda(request)
        return respuesta    

    def registrar_cliente(self,request):
        respuesta=registrar.registrar_cliente(request)
        return respuesta      
    