from mype.controller.pedido_controller import PedidoController
pedido_controller=PedidoController()
class PedidoView:
    def registrar_pedido(self,request):
        respuesta=pedido_controller.registrar_pedido(request)
        return respuesta