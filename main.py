import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.lang import Builder

# Kivyの設定
kivy.config.Config.set('graphics', 'width', '400')
kivy.config.Config.set('graphics', 'height', '300')

#6つの画面
##class HomeScreen

# メインのアプリケーションクラス
class Init_App(App):
    def build(self):
        self.sm = ScreenManager(transition=NoTransition())
        
        # kv ファイルを読み込む
        Builder.load_file('HomeScreen.kv')
        # Builder.load_file('Projects.kv')
        # Builder.load_file('Browse.kv')
        # Builder.load_file('Downloading.kv')
        # Builder.load_file('Collections.kv')
        # Builder.load_file('Viewer.kv')
        screen = Screen(name='home')

        self.sm.add_widget(screen)
        # sm.add_widget(TwoScreen(name='two'))
        # sm.add_widget(ThreeScreen(name='three'))
        # sm.add_widget(FourScreen(name='four'))
        # sm.add_widget(FiveScreen(name='five'))
        # sm.add_widget(SixScreen(name='six'))

        return self.sm

    def switch_screen(self, screen_name):
        sm = self.root
        sm.current = screen_name

if __name__ == "__main__":
    Init_App().run()

