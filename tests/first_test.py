import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

# тест умножения
    def test_multiply_calculate_pass(self):
        assert self.calc.multiply(1, 2) == 2

    def test_multiply_calculate_fail(self):
        assert self.calc.multiply(1, 2) == 1

# тест деления
    def test_division_calculate_pass(self):
        assert self.calc.division(2, 1) == 2

    def test_division_calculate_fail(self):
        assert self.calc.division(2, 1) == 1

# тест вычитания
    def test_subtraction_calculation_pass(self):
        assert self.calc.subtraction(2, 1) == 1

    def test_subtraction_calculation_fail(self):
        assert self.calc.subtraction(2, 1) == 2

# Тест сложения

    def test_adding_calculation_pass(self):
        assert self.calc.adding(1, 1) == 2

    def test_adding_calculation_fail(self):
        assert self.calc.adding(1, 1) == 1