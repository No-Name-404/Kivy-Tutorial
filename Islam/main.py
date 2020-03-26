from kivymd.app import MDApp
from kivy.lang import Builder

Builder.load_file('style.kv')

class MainApp(MDApp):
	def __init__(self,**a):
		self.theme_cls.theme_style='Dark'
		super(MainApp,self).__init__(**a)

MainApp().run()
