from controller.chat_controller import ChatController
chat_controller=ChatController()
class ChatView:
    def guardar_mensaje_cliente(self,request):
        respuesta=chat_controller.chat_mensaje_cliente(request)
        return respuesta

    def chat_mensaje_soporte(self,request):
        respuesta=chat_controller.chat_mensaje_soporte(request)
        return respuesta    