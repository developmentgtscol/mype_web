from firebase_admin import db
class LoginModel:
    def validarlogin(self,uid):
        datos=db.reference('adminGeo').child(uid).get()
        if datos is not None:
                return True,''
        else:
            #codigo=self.generador.validarGuardarInformacionError("403","Usuario no posee permiso","post","undefined")
            return False,'no exite codigo' 
        