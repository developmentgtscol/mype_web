from controller.producto_controller import ProductoController
producto_controller=ProductoController()
class ProductoView:
    def registrar_producto(self,request):
        respuesta=producto_controller.registrar_producto(request)
        return respuesta

    def solicitar_producto(self,request):
        respuesta=producto_controller.solicitar_producto(request)
        return respuesta    

    def solicitar_producto_cliente(self,request):
        respuesta=producto_controller.solicitar_producto_cliente(request)
        return respuesta        