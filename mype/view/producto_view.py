from mype.controller.producto_controller import ProductoController
producto_controller=ProductoController()
class ProductoView:
    def registrar_producto(self,request):
        respuesta=producto_controller.registrar_producto(request)
        return respuesta