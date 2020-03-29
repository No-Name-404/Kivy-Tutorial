from kivymd.uix.button import MDIconButton
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.properties import *

class FullImage(Image):
    pass


class IconImage(MDIconButton):
    pass

class MCard(BoxLayout):
    def __init__(self,url=False,image=False,**kwargs):
        self.url=url if url else 'https://google.com'
        self.radius=[dp(20)]
        self.image=image if image else ''
        super(MCard,self).__init__(**kwargs)

class VideoBox(BoxLayout):
    pass
