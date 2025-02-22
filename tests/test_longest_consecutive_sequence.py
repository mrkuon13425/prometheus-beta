import pytest
from src.longest_consecutive_sequence import find_longest_consecutive_sequence

def test_basic_consecutive_sequence():
    """Test a basic consecutive sequence"""
    assert find_longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == [1, 2, 3, 4]

def test_multiple_consecutive_sequences():
    """Test when multiple consecutive sequences exist"""
    assert find_longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def test_empty_list():
    """Test empty input list"""
    assert find_longest_consecutive_sequence([]) == []

def test_single_element():
    """Test list with single element"""
    assert find_longest_consecutive_sequence([42]) == [42]

def test_non_consecutive_numbers():
    """Test list with no consecutive numbers"""
    assert find_longest_consecutive_sequence([10, 20, 30, 40]) == [10]

def test_repeated_numbers():
    """Test list with repeated numbers"""
    assert find_longest_consecutive_sequence([1, 2, 2, 3, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    """Test consecutive sequence with negative numbers"""
    assert find_longest_consecutive_sequence([-3, -2, -1, 0, 1, 3, 4, 5]) == [-3, -2, -1, 0, 1]