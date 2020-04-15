class Config:
    def iniciar(self):
        return dict(
            SECRET_KEY="powerful secretkey",
            WTF_CSRF_SECRET_KEY="a csrf secret key",
            WTF_CSRF_TIME_LIMIT=None
        )