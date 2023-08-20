class Screen:
    def __init__(self, scr):
        self.scr = scr
        self.maxy, self.maxx = scr.getmaxyx()
    def on_load(self):
        pass
    def on_unload(self):
        pass
    def on_press(self, key):
        pass
    def on_mouse(self, y, x):
        pass
    def on_resize(self):
        self.maxy, self.maxx = self.scr.getmaxyx()
