def validate_input_conditions(value, min_value=0, max_value=100, required_type=int):
    """
    A function that uses assertions to validate input conditions.
    
    Args:
        value: The input value to validate
        min_value (int, optional): Minimum allowed value. Defaults to 0.
        max_value (int, optional): Maximum allowed value. Defaults to 100.
        required_type (type, optional): Expected type of the value. Defaults to int.
    
    Returns:
        bool: True if all conditions are met
    
    Raises:
        AssertionError: If any validation condition fails
    """
    # Check type of the value
    assert isinstance(value, required_type), f"Value must be of type {required_type.__name__}"
    
    # Check value is within specified range
    assert min_value <= value <= max_value, f"Value must be between {min_value} and {max_value}"
    
    # Additional optional condition checks can be added here
    
    return True