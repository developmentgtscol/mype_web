class SolicitudesModel:
    def solicitudes_admin_gerente(self,uid):
        ref = db.reference()
        ref.child('geo').child(user.uid).set(datos_guardar)