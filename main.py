from src.Circle import Circle
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle

figura1 = Figure()
print(figura1.area)
figura1.figure_info()
figura2 = Square(10)
figura2.figure_info()
figura3 = Triangle(16,26,17)
figura3.figure_info()
figura3.add_area(figura2,figura2)
print(figura3.summ_area)
figura2.add_area(figura3,figura3)
print(figura2.summ_area)
figura4 = Rectangle(4,9)
figura4.figure_info()
figura5 = Circle(6)
figura5.figure_info()
figura5.add_area(figura4,figura3,figura2)
print("площадь всех фигур= ", figura5.summ_area)