class Screen(object):
    def __init__(self,width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def resolution(self):
        return str(self._width) + ' X ' + str(self._height)

    @width.setter
    def width(self, width):
        self._width = width

    @height.setter
    def height(self, height):
        self._height = height




s = Screen(0,0)
s.width = 1400
s.height = 900

print(s.resolution)
