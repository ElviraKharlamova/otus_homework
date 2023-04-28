import math

from src.Figure import Figure


class Circle(Figure):


    def __init__(self, radius: int):
        if radius <= 0:
            print("Радиус должен быть больше 0!")
            raise ValueError
        super().__init__()
        self.radius = radius
        self.perimeter = round((self.radius * math.pi * 2), 2)
        self.area = round(math.pi*(self.radius)**2, 2)
        self.summ_area = self.area
        self.name = "Circle"

    def figure_info(self):
        print(f"area = {self.area}, perimetr = {self.perimeter}")