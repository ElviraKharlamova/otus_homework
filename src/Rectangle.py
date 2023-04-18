from src.Figure import Figure


class Rectangle(Figure):


    def __init__(self, side1: int, side2: int):
        if (side1 <= 0) or (side2 <= 0):
            print("Сторона должна быть больше 0!")
            raise ValueError
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.perimeter = 2*(self.side1 + self.side2)
        self.area = self.side1 * self.side2
        self.summ_area = self.area
        self.name = "Rectangle"

    def figure_info(self):
        print(f"area = {self.area}, perimetr = {self.perimeter}")