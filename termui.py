from termpixels import Color, App
from mako.template import Template


class DoomTerm(App):
    def __init__(self):
        self.state = {
            'counter': 0
        }
        super().__init__(framerate=24)

    def on_key(self, key):
        self.state['counter'] += 1

    def on_frame(self):
        self.screen.clear()
        title = Template(filename="templates/title.tpl").render(**self.state)
        title_width = max(len(row) for row in title.splitlines())

        self.screen.print(title, self.screen.w // 2 - title_width // 2, 2,
                          fg=Color.rgb(0.368, 0.850, 0.560),
                          bg=Color.rgb(0, 0, 0)
                          )
        self.screen.update()


if __name__ == "__main__":
    DoomTerm().start()
