import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.lang import Builder

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Kivyの設定
# kivy.config.Config.set('graphics', 'width', '400')
# kivy.config.Config.set('graphics', 'height', '300')

#6つの画面
class HomeScreenApp(Screen):
    pass
class ProjectScreenApp(Screen):
    pass
class BrowseScreenApp(Screen):
    pass
class DownloadScreenApp(Screen):
    pass
class CollectScreenApp(Screen):
    pass
class ViewScreenApp(Screen):
    pass

# メインのアプリケーションクラス
class InitApp(App):
    sm = ScreenManager()

    def build(self):
        #self.sm = ScreenManager(transition=NoTransition())
        
        # kv ファイルを読み込む
        Builder.load_file('HomeScreen.kv')
        Builder.load_file('ProjectScreen.kv')
        Builder.load_file('BrowseScreen.kv')
        Builder.load_file('DownloadScreen.kv')
        Builder.load_file('CollectScreen.kv')
        Builder.load_file('ViewScreen.kv')
        # screen = Screen(name='home')

        self.sm.add_widget(HomeScreenApp(name='home'))
        self.sm.add_widget(ProjectScreenApp(name='project'))
        self.sm.add_widget(BrowseScreenApp(name='browse'))
        self.sm.add_widget(DownloadScreenApp(name='download'))
        self.sm.add_widget(CollectScreenApp(name='collect'))
        self.sm.add_widget(ViewScreenApp(name='view'))

        self.sm.current = 'view'


        return self.sm

    def switch_screen(self, screen_name):
        self.sm.current = screen_name

if __name__ == "__main__":
    InitApp().run()

