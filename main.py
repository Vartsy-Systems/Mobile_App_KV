from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
import designer
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.toolbar import MDTopAppBar
class LoginApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Purple"
        Window.size=(300,600)
        self.style = Builder.load_string(designer.design)
        button = MDRectangleFlatButton(text= "Signin",pos_hint= {'center_x': 0.5,'center_y': 0.25},on_release = self.Login)
        screen.add_widget(self.style)
        screen.add_widget(button)
        top_nav = MDTopAppBar(title = "Demo")
        return screen
        
    def Login(self,obj):
        close_button = MDFlatButton(text = "close", on_release= self.close_window)
        self.dialog = MDDialog(title = 'Login',text = 'Login Successfully',size_hint=(0.7,1),buttons = [close_button])
        self.dialog.open()
    def close_window(self,obj):
        self.dialog.dismiss()



if __name__ =='__main__':
    LoginApp().run()