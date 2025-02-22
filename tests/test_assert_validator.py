import pytest
from src.assert_validator import validate_input_conditions

def test_valid_integer():
    """Test a valid integer input"""
    assert validate_input_conditions(50) == True

def test_valid_integer_with_custom_range():
    """Test a valid integer with custom range"""
    assert validate_input_conditions(75, min_value=50, max_value=100) == True

def test_minimum_value():
    """Test the minimum allowed value"""
    assert validate_input_conditions(0) == True

def test_maximum_value():
    """Test the maximum allowed value"""
    assert validate_input_conditions(100) == True

def test_invalid_type():
    """Test that an invalid type raises an AssertionError"""
    with pytest.raises(AssertionError, match="Value must be of type int"):
        validate_input_conditions("not an int")

def test_below_min_value():
    """Test that a value below the minimum raises an AssertionError"""
    with pytest.raises(AssertionError, match="Value must be between"):
        validate_input_conditions(-1)

def test_above_max_value():
    """Test that a value above the maximum raises an AssertionError"""
    with pytest.raises(AssertionError, match="Value must be between"):
        validate_input_conditions(101)

def test_custom_type_validation():
    """Test validation with a custom type"""
    class CustomInt:
        def __init__(self, value):
            self.value = value

    custom_int = CustomInt(50)
    assert validate_input_conditions(custom_int, required_type=CustomInt) == True

def test_custom_type_validation_failure():
    """Test validation failure with an incorrect type"""
    with pytest.raises(AssertionError, match="Value must be of type CustomInt"):
        validate_input_conditions(50, required_type=type('CustomInt', (), {}))