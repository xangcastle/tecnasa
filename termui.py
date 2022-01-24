from termpixels import Color, App
from mako.template import Template
from time import time
from math import sin


class DoomTerm(App):
    def __init__(self):
        self.state = {}
        super().__init__(framerate=24)

    def on_key(self, key):
        pass

    def on_frame(self):
        self.screen.clear()
        title = Template(filename="templates/title.tpl").render()
        title_width = max(len(row) for row in title.splitlines())

        self.screen.print(title, self.screen.w // 2 - title_width // 2, 2,
                          fg=Color.rgb(0.368, 0.850, 0.560),
                          bg=Color.rgb(0, 0, 0)
                          )
        self.screen.update()


if __name__ == "__main__":
    DoomTerm().start()
