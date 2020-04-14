from flask import jsonify
from mype.controller.login_controller import LoginController
def login_view(request):
    login_controller=LoginController()
    # validar paramentros headers

    return login_controller.validar_login(request)