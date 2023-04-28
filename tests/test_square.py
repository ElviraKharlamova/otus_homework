import pytest

from src.Square import Square


@pytest.mark.parametrize('side, expected_perimeter, expected_area',
                         [
                             (7, 28, 49),
                             (5, 20, 25)
                         ]
                         )
def test_square_creation_positive(side, expected_perimeter, expected_area):
    square = Square(side)
    assert square.name == "Square", 'Expected name is Square'
    assert square.perimetr == expected_perimeter, 'Expected correct perimeter'
    assert square.area == expected_area, 'Expected correct area'


@pytest.mark.parametrize('side',
                         [
                             0,
                             -8
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative'
                         ])
def test_square_creation_negative(side):
    with pytest.raises(ValueError):
        Square(side)


def test_two_square_areas_sum():
    expected_sum = 73
    square_1 = Square(8)
    square_2 = Square(3)
    assert square_1.add_area(square_2) == expected_sum, f'Expected sum is {expected_sum}'
