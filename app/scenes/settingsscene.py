from kivy.uix.screenmanager import Screen

from utils.settings import Settings


class SettingsScene(Screen):
    user_new_data = {
        'width': None,
        'height': None,
        'user_color': ''
    }

    def get_new_data(self, new_width, new_height,
                     red, orange, yellow, green, blue, violet):
        self.user_new_data['width'] = new_width
        self.user_new_data['height'] = new_height
        colors = [red, orange, yellow, green, blue, violet]
        self.user_new_data['user_color'] = self.choose_color(colors)
        s = Settings()
        s.update_and_save(self.user_new_data)

    def choose_color(self, colors):
        counter = 0
        for color in colors:
            if color:
                break
            else:
                counter += 1
        if counter == 0:
            return 'red'
        elif counter == 1:
            return 'orange'
        elif counter == 2:
            return 'yellow'
        elif counter == 3:
            return 'green'
        elif counter == 4:
            return 'blue'
        elif counter == 5:
            return 'violet'
