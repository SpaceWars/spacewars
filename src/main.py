from cocos.layer import Layer
from cocos.director import director
from cocos.scene import Scene


class MainWindow(Layer):

    def __init__(self):
        super(MainWindow, self).__init__()


if __name__ == "__main__":
    director.init()
    main_window = MainWindow()
    main_scene = Scene(main_window)
    director.run(main_scene)
