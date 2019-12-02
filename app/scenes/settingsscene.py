import json

from kivy import Config
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen


class SettingsScene(Screen):
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

    def on_enter(self):
        print("Settings")

    def update_changes(self, key, value):
        if key == "width":
            if int(value) < 1024 or int(value) > 1920:
                wrong_value_popup = Popup(title='Wrong value',
                                          content=Label(text='Enter a value between 1024 and 1920.'),
                                          size_hint=(None, None), size=(400, 200))
                wrong_value_popup.open()
            # else:
            #     Config.set('graphics', 'width', value)
            #     Config.write()
        elif key == "height":
            if int(value) < 768 or int(value) > 1080:
                wrong_value_popup = Popup(title='Wrong value',
                                          content=Label(text='Enter a value between 768 and 1080.'),
                                          size_hint=(None, None), size=(400, 200))
                wrong_value_popup.open()
            # else:
            #     Config.set('graphics', 'width', value)
            #     Config.write()
