from kivy.app import App
from kivy.lang import Builder

kv = Builder.load_file('menuscene.kv')


class MenuScene(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MenuScene().run()
