from employee import Employee
import pytest

@pytest.fixture
def employee():
    employee = Employee('Robin', 'Che', 14000)
    return employee


def test_give_default_raise(employee):
    employee.give_raise()
    assert 19000 == employee.annual_salary

def test_give_custom_raise(employee):
    employee.give_raise(3000)
    assert 17000 == employee.annual_salary