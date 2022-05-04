class DrawAPIOne:
    def draw_circle(self, x, y, radius):
        return f"Draw API 1, X: {x}, Y: {y}, Radius: {radius}"


class DrawAPITwo:
    def draw_circle(self, x, y, radius):
        return f"Draw API 2, X: {x}, Y: {y}, Radius: {radius}"


class Circle:
    def __init__(self, x, y, radius, drawing_api) -> None:
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        return self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, scale):
        self._radius *= scale
