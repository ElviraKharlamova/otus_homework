import pytest

from src.Circle import Circle


@pytest.mark.parametrize('radius, expected_perimeter, expected_area',
                         [
                             (5, 31.42, 78.54),
                             (2, 12.57, 12.57),
                             (1, 6.28, 3.14),
                         ]
                         )
def test_circle_creation_positive(radius, expected_perimeter, expected_area):
    сircle = Circle(radius)
    assert сircle.name == "Circle", 'Expected name is Circle'
    assert сircle.perimeter == expected_perimeter, 'Expected correct perimeter'
    assert сircle.area == expected_area, 'Expected correct area'


@pytest.mark.parametrize('radius',
                         [
                             (0),
                             (-1)
                         ],
                         ids=[
                             'radius is zero',
                             'radius is negative'
                         ])
def test_circle_creation_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_two_circle_areas_sum():
    expected_sum = 125.67
    circle_1 = Circle(6)
    circle_2 = Circle(2)
    assert circle_1.add_area(circle_2) == expected_sum, f'Expected sum is {expected_sum}'


