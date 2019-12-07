from kivy.uix.screenmanager import Screen

from utils.settings import Settings


class AppSettingsScene(Screen):
    user_new_data = {
        'width': None,
        'height': None,
        'user_color': ''
    }

    def get_new_data(self, new_width, new_height):
        self.user_new_data['width'] = new_width
        self.user_new_data['height'] = new_height
        s = Settings()
        s.update_and_save(self.user_new_data)
