"""
Test for source.shape_checker
"""
from source.shape_checker import get_triangle_type
from source.shape_checker import get_square_type
from unittest import TestCase
from test.plugins.ReqTracer import requirements


class TestGetTriangleType(TestCase):
    # EQUILATERAL with all INT

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    # EQUILATERAL with mixed type

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_mixedTypeOne(self):
        result = get_triangle_type(1.0, 1, 1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_mixedTypeTwo(self):
        result = get_triangle_type(1, 1.0, 1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_mixedTypeThree(self):
        result = get_triangle_type(1, 1, 1.0)
        self.assertEqual(result, 'equilateral')

    # SCALENE with all INT

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(4, 3, 2)
        self.assertEqual(result, 'scalene')

    # SCALENE with mixed type

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_mixedTypeOne(self):
        result = get_triangle_type(4.0, 3, 2)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_mixedTypeTwo(self):
        result = get_triangle_type(4, 3.0, 2)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_all_mixedTypeThree(self):
        result = get_triangle_type(4, 3, 2.0)
        self.assertEqual(result, 'scalene')

    # SCALENE with invalid lengths

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_invalidAreaOne(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_invalidAreaTwo(self):
        result = get_triangle_type(3, 1, 2)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_invalidAreaThree(self):
        result = get_triangle_type(1, 3, 2)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_invalidAreaFour(self):
        result = get_triangle_type(1, 2, 4)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_invalidAreaFive(self):
        result = get_triangle_type(4, 1, 2)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_invalidAreaSix(self):
        result = get_triangle_type(1, 4, 2)
        self.assertEqual(result, 'invalid')

    # ISO where a=b

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_int_ab(self):
        result = get_triangle_type(2, 2, 1)
        self.assertEqual(result, 'isosceles')

    # ISO where a=c

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_int_ac(self):
        result = get_triangle_type(2, 1, 2)
        self.assertEqual(result, 'isosceles')

    # ISO where b=c

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_int_bc(self):
        result = get_triangle_type(1, 2, 2)
        self.assertEqual(result, 'isosceles')

    # ISO with mixed type a=b

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_mixedType_ab(self):
        result = get_triangle_type(2.0, 2, 1)
        self.assertEqual(result, 'isosceles')

    # a=c

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_mixedType_ac(self):
        result = get_triangle_type(2, 1.0, 2)
        self.assertEqual(result, 'isosceles')

    # b=c

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_all_mixedType_bc(self):
        result = get_triangle_type(1.0, 2, 2)
        self.assertEqual(result, 'isosceles')

    # EQUILATERAL with 1 side = 0

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_oneSideZero(self):
        result = get_triangle_type(0, 1, 1)
        self.assertEqual(result, 'invalid')

    # SCALENE with 1 side = 0

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_oneSideZero(self):
        result = get_triangle_type(4, 0, 2)
        self.assertEqual(result, 'invalid')

    # ISO with 1 side = 0

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_oneSideZero(self):
        result = get_triangle_type(2, 2, 0)
        self.assertEqual(result, 'invalid')

    # EQUILATERAL with all sides = 0

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_allSideZero(self):
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, 'invalid')

    # SCALENE with all sides = 0

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_allSideZero(self):
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, 'invalid')

    # ISO with all sides = 0

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_allSideZero(self):
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, 'invalid')

    # EQUILATERAL with 1 side < 0

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_oneSideNeg(self):
        result = get_triangle_type(-1, 1, 1)
        self.assertEqual(result, 'invalid')

    # SCALENE with 1 side < 0

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scalene_oneSideNeg(self):
        result = get_triangle_type(4, -3, 2)
        self.assertEqual(result, 'invalid')

    # ISO with 1 side < 0

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isosceles_oneSideNeg(self):
        result = get_triangle_type(2, 1, -2)
        self.assertEqual(result, 'invalid')

    # Too many ARGS

    @requirements(['#0001', '#0002'])
    def test_get_triangle_tooManyParams(self):
        self.assertRaises(Exception, get_triangle_type, 1, 2, 3, 4)


# SQUARE TESTS_________________________________________________________________________________________________________


class TestGetSquareType(TestCase):
    # Test valid cases for square and rectangle

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquare(self):
        result = get_square_type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004'])
    def test_get_square__TestRectangle(self):
        result = get_square_type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    # Test invalid side length

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquareLength(self):
        result = get_square_type(1, 2, 3, 4)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_square__TestRectangleLength(self):
        result = get_square_type(1, 2, 1, 4)
        self.assertEqual(result, 'invalid')

    # Test for mixed type

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquareMixedOne(self):
        result = get_square_type(1.0, 1, 1, 1)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004'])
    def test_get_square__TestRectangleMixedOne(self):
        result = get_square_type(1.0, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquareMixedTwo(self):
        result = get_square_type(1, 1.0, 1, 1)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004'])
    def test_get_square__TestRectangleMixedTwo(self):
        result = get_square_type(1, 2.0, 1, 2)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquareMixedThree(self):
        result = get_square_type(1, 1, 1.0, 1)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004'])
    def test_get_square__TestRectangleMixedThree(self):
        result = get_square_type(1, 2, 1.0, 2)
        self.assertEqual(result, 'rectangle')

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquareMixedFour(self):
        result = get_square_type(1, 1, 1, 1.0)
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004'])
    def test_get_square__TestRectangleMixedFour(self):
        result = get_square_type(1, 2, 1, 2.0)
        self.assertEqual(result, 'rectangle')

    # Test for 1 side = 0

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquareSideZeroOne(self):
        result = get_square_type(0, 1, 1, 1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_square__TestRectangleSideZeroOne(self):
        result = get_square_type(0, 2, 1, 2)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquareSideZeroTwo(self):
        result = get_square_type(1, 0, 1, 1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_square__TestRectangleSideZeroTwo(self):
        result = get_square_type(1, 0, 1, 2)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquareSideZeroThree(self):
        result = get_square_type(1, 1, 0, 1)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_square__TestRectangleSideZeroThree(self):
        result = get_square_type(1, 2, 0, 2)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquareSideZeroFour(self):
        result = get_square_type(1, 1, 1, 0)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_square__TestRectangleSideZeroFour(self):
        result = get_square_type(1, 2, 1, 0)
        self.assertEqual(result, 'invalid')

    # Test all sides = 0

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquareAllZero(self):
        result = get_square_type(0, 0, 0, 0)
        self.assertEqual(result, 'invalid')

    # COVERAGE______________________________________________________________________________________
    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_all_intTuple(self):
        result = get_triangle_type([1, 1, 1])
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_invalidDict(self):
        my_dict = {'one': 1, 'two': 2, 'three': 3}
        result = get_triangle_type(my_dict)
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquareAllEqualTuple(self):
        result = get_square_type([1, 1, 1, 1])
        self.assertEqual(result, 'square')

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquareInvalidlDict(self):
        my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
        result = get_square_type(my_dict)
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_charInvalid(self):
        result = get_triangle_type(chr(1), chr(1), chr(1))
        self.assertEqual(result, 'invalid')

    @requirements(['#0003', '#0004'])
    def test_get_square_TestSquare_charInvalid(self):
        result = get_square_type(chr(1), chr(1), chr(1), chr(1))
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equilateral_sideZero(self):
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, 'invalid')
