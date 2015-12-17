class cSettings:
    def __call__(self,key):
        if key=='path:favicon.ico':
            return 'static/icons/favicon.ico'
        return None

#Settings = cSettings()
