from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import Screen

Window.size = (300,600)

style = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    CodeScreen:

<MenuScreen>:
    name: "menu"
    MDRectangleFlatButton:
        text: "Profile"
        pos_hint: {"center_x":.5,"center_y":.5}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: "Start Code"
        pos_hint: {"center_x":.5,"center_y":.4}
        on_press: root.manager.current = 'code'

<ProfileScreen>:
    name: "profile"
    MDLabel:
        text: "Welcome to Programming Hub"
        halign: "center"
    MDRectangleFlatButton:
        text: "Home"
        pos_hint: {"center_x":.5,"center_y":.4}
        on_press: root.manager.current = 'menu'
    
<CodeScreen>:
    name: "code"
    MDLabel:
        text: "Lets start coding"
        halign: "center"
    MDRectangleFlatButton:
        text: "Home"
        pos_hint: {"center_x":.5,"center_y":.4}
        on_press: root.manager.current = 'menu'
    
        

"""
class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class CodeScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name = 'menu'))
sm.add_widget(ProfileScreen(name = 'profile'))
sm.add_widget(CodeScreen(name = 'screen'))
class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        design = Builder.load_string(style)
        return design

if __name__=="__main__":
    MyApp().run()