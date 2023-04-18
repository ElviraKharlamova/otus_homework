from src.Figure import Figure


class Square(Figure):

    def __init__(self, side: int):
        if side <= 0:
            print("Сторона должна быть больше 0!")
            raise ValueError
        super().__init__()
        self.side = side
        self.area = side**2
        self.perimetr = 4*side
        self.summ_area = self.area
        self.name = "Square"
    def figure_info(self):
        print(f"area = {self.area}, perimetr = {self.perimetr}")