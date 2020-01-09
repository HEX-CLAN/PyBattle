from pybattle.run import Run
from kivy.core.window import Window
from kivy import Config


if __name__ == '__main__':
    # Config.set('graphics', 'fullscreen', 'auto')


    Config.set('graphics', 'fullscreen', False) # to nadpisuje config, ktory gra wlaczylaby domyslnie
    Config.write()

    Window.fullscreen = 'auto' # a to ustawia na chama fullscreena, True tez moze zadziala, ale polecam auto




    #
    # w = Window.size[0]
    # h = Window.size[1]

    # print("window: ", Window.size)
    # Config.set('graphics', 'width', w)
    # print("window: ", Window.size)
    # Config.set('graphics', 'height', h)
    # print("window: ", Window.size)
    #Config.write()

    # print("window:", Window.size)
    # print("config: (" + Config.get('graphics', 'width') + ", " + Config.get('graphics', 'height') + ")")
    r = Run()

    r.run()

    # pecet pokazuje 5120x2880 a ustawienie jest 1440x900-HIDPI
    # lapek pokazuje 2880x1800 a ustawienie jest 1440x900-HIDPI