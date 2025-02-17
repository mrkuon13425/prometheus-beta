import os
import sys
import pytest

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.file_writer import write_string_to_file

def test_write_string_to_file_success(tmp_path):
    # Create a temporary file path
    test_file = tmp_path / "test_file.txt"
    
    # Test writing a simple string
    test_content = "Hello, world!"
    write_string_to_file(str(test_file), test_content)
    
    # Verify file contents
    with open(test_file, 'r') as file:
        assert file.read() == test_content

def test_write_string_to_file_overwrite(tmp_path):
    # Create a temporary file path
    test_file = tmp_path / "test_file.txt"
    
    # Write initial content
    write_string_to_file(str(test_file), "Initial content")
    
    # Overwrite with new content
    new_content = "Overwritten content"
    write_string_to_file(str(test_file), new_content)
    
    # Verify new content
    with open(test_file, 'r') as file:
        assert file.read() == new_content

def test_write_string_to_file_empty_string(tmp_path):
    # Create a temporary file path
    test_file = tmp_path / "empty_file.txt"
    
    # Write empty string
    write_string_to_file(str(test_file), "")
    
    # Verify empty file
    with open(test_file, 'r') as file:
        assert file.read() == ""

def test_write_string_to_file_invalid_file_path_type():
    # Test invalid file_path type (not a string)
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "Test content")

def test_write_string_to_file_invalid_content_type():
    # Test invalid content type (not a string)
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("test.txt", 123)

def test_write_string_to_file_invalid_directory():
    # Test writing to an invalid directory
    with pytest.raises(IOError):
        write_string_to_file("/non/existent/directory/test.txt", "Test content")