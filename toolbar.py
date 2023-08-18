from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

style = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title:'WhatsApp'
                        left_action_items:[['menu',lambda x:nav_drawer.set_state("open")]]
                        right_action_items:[['clock']]
                        
                        elevation:3
                    MDBottomAppBar:
                        MDTopAppBar:
                            #title: "Title"
                            icon :"phone"
                            type:"bottom"
                            elevation: 0
                            #mode: "free-center"
                            
                
                    Widget:
        MDNavigationDrawer:
            id:nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing:'8dp'
                padding: '8dp'
                Image:
                    source:'id_1.png'
                MDLabel:
                    text:" BraKobby"
                    font_style:"Subtitle1"
                    height: self.texture_size[1]
                    size_hint_y:None
                MDLabel:
                    text:" www.instagram.com/brakobby7"
                    font_style:"Caption"
                    height: self.texture_size[1]
                    size_hint_y: None
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Profile"
                            IconLeftWidget:
                                icon:"account"
                        OneLineIconListItem:
                            text: "Security"
                            IconLeftWidget:
                                icon:"key"
                        OneLineIconListItem:
                            text: "Upload"
                            IconLeftWidget:
                                icon:"file-upload"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon:"logout"
            
                  

"""

Window.size = (300,600)
class VartsyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        design = Builder.load_string(style)
        return design


if __name__ =='__main__':
    VartsyApp().run()