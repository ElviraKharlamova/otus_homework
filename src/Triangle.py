from math import sqrt

from src.Figure import Figure


class Triangle(Figure):


    def __init__(self, side1: int, side2: int, side3: int):
        if (side1 <= 0) or (side2 <= 0) or (side3 <= 0):
            print("Сторона должна быть больше 0!")
            raise ValueError
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.perimeter = self.side1 + self.side2 + self.side3
        self.poluperimeter = self.perimeter*0.5
        self.area = sqrt(self.poluperimeter*(self.poluperimeter - self.side1)*(self.poluperimeter - self.side2)*(self.poluperimeter - self.side3))
        self.summ_area = self.area
        self.name = "Triangle"

    def figure_info(self):
        print(f"area = {self.area}, perimetr = {self.perimeter}")

