import json

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
