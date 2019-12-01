import json

from kivy import Config
from kivy.uix.screenmanager import Screen

json_settings = json.dumps([
    {
        "type": "numeric",
        "title": "Width",
        "section": "General",
        "key": "width"
    },
    {
        "type": "numeric",
        "title": "Height",
        "section": "General",
        "key": "height"
    }
])


class SettingsScene(Screen):
    def on_enter(self):
        print("Settings")

    def update_changes(self, key, value):
        if key == "width":
            print(value)
            if int(value) < 1024:
                Config.set('graphics', 'width', 1024)
            elif int(value) > 1920:
                Config.set('graphics', 'width', 1920)
            else:
                Config.set('graphics', 'width', value)
        elif key == "height":
            print(value)
            if int(value) < 768:
                Config.set('graphics', 'width', 768)
                value = '768'
            elif int(value) > 1080:
                Config.set('graphics', 'width', 1080)
            else:
                Config.set('graphics', 'width', value)
        print(value)
        Config.write()
