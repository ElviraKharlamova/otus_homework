import pytest

from src.Rectangle import Rectangle


@pytest.mark.parametrize('side1, side2, expected_perimeter, expected_area',
                         [
                             (10, 9, 38, 90),
                             (5, 3, 16, 15)
                         ]
                         )
def test_rectangle_creation_positive(side1, side2, expected_perimeter, expected_area):
    rectangle = Rectangle(side1, side2)
    assert rectangle.name == "Rectangle", 'Expected name is Rectangle'
    assert rectangle.perimeter == expected_perimeter, 'Expected correct perimeter'
    assert rectangle.area == expected_area, 'Expected correct area'


@pytest.mark.parametrize('side1, side2',
                         [
                             (0, 8),
                             (-2, 6),
                             (10, 10),
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative',
                             'it is a square'
                         ])
def test_rectangle_creation_negative(side1, side2):
    with pytest.raises(ValueError):
        Rectangle(side1, side2)


def test_two_rectangle_areas_sum():
    expected_sum = 48
    rectangle_1 = Rectangle(8, 5)
    rectangle_2 = Rectangle(4, 2)
    assert rectangle_1.add_area(rectangle_2) == expected_sum, f'Expected sum is {expected_sum}'
