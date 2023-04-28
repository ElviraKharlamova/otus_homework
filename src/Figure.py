class Figure:
    area = 0
    summ_area = 0
    name = ""

    def __init__(self):
        pass


    def figure_info(self):
        print(f'area {self.area}')


    def add_area(self, figura, *args):
        self.summ_area = self.summ_area + figura.area
        for item in args:
            self.summ_area = self.summ_area + item.area
        return round(self.summ_area, 2)


