from kivymd.app import MDApp
from kivy.factory import Factory

class MyApp(MDApp):
    def __init__(self,**kwargs):
        self.title = 'Calculator'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_light_hue = '50'
        super(MyApp,self).__init__(**kwargs)

    def on_start(self):
        num = [7,8,9,4,5,6,1,2,3,'%',0,'*']
        for i in num:
            i = str(i)
            self.root.ids.number.add_widget(
            Factory.NumButton(text=i)
            )
        cal = [False,'+','-','/']
        for i in cal:
            if i:
                i = str(i)
                self.root.ids.Cal.add_widget(
                Factory.NumButton(text=i)
                )
            else:
                self.root.ids.Cal.add_widget(
                Factory.delete(text='clear')
                )

    def Equal(self):
        try:
            return str(eval(self.root.ids.Text.text))
        except:
            return self.root.ids.Text_hint.text

MyApp().run()
