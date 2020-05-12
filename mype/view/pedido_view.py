from controller.pedido_controller import PedidoController
pedido_controller=PedidoController()
class PedidoView:
    def registrar_pedido(self,request):
        respuesta=pedido_controller.registrar_pedido(request)
        return respuesta

    def solicitar_pedido_tienda(self,request):
        respuesta=pedido_controller.solicitar_pedido_tienda(request)
        return respuesta

    def solicitar_pedido_cliente(self,request):
        respuesta=pedido_controller.solicitar_pedido_cliente(request)
        return respuesta

    def solicitar_pedido(self,request):
        respuesta=pedido_controller.solicitar_pedido(request)
        return respuesta                