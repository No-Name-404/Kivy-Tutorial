from kivymd.app import MDApp

class MainApp(MDApp):
    def __init__(self,**kwargs):
        self.title = 'My Code'
        self.theme_cls.theme_style = 'Dark'
        super(MainApp,self).__init__(**kwargs)

MainApp().run()
