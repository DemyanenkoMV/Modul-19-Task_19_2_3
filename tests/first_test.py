import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

# тест умножения
    def test_multiply_calculate_pass(self):
        assert self.calc.multiply(2, 2) == 4

# тест деления
    def test_division_calculate_pass(self):
        assert self.calc.division(6, 3) == 2

# тест вычитания
    def test_subtraction_calculation_pass(self):
        assert self.calc.subtraction(8, 4) == 4

# Тест сложения
    def test_adding_calculation_pass(self):
        assert self.calc.adding(6, 2) == 8
