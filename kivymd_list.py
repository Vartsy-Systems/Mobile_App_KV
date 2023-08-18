from kivymd.app import MDApp
from kivymd.uix.list import MDList,OneLineListItem,TwoLineListItem,ThreeLineIconListItem
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import IconLeftWidget


class ListApp(MDApp):
    def build(self):
        Window.size = ([300,600])
        screen = Screen()
        scroll = ScrollView()
        list = MDList()
        for items in range(1,21):
            icon = IconLeftWidget(icon = "language-python")
            item = ThreeLineIconListItem(text = "Program " + str(items),secondary_text = "User",tertiary_text="code_beast")
            item.add_widget(icon)
            list.add_widget(item)
        scroll.add_widget(list)
        screen.add_widget(scroll)
        return screen

if __name__=='__main__':
    ListApp().run()