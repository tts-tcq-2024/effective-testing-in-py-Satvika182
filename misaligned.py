import io
import sys

# This function cannot be modified
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)

# Function to capture printed output
def capture_print_output(func):
    captured_output = io.StringIO()          # Create a string IO to capture output
    sys.stdout = captured_output             # Redirect stdout to the string IO
    func()                                   # Call the function whose output needs to be captured
    sys.stdout = sys.__stdout__              # Reset redirect.
    return captured_output.getvalue().splitlines()  # Return the output as a list of lines

# Generate the expected color map output
def generate_expected_output():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    expected_output = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            expected_output.append(f'{i * 5 + j} | {major} | {minor}')
    return expected_output

# Testing function to compare captured output with expected output
def test_print_color_map():
    expected_output = generate_expected_output()
    
    # Capture the output of print_color_map without modifying it
    captured_output = capture_print_output(print_color_map)
    
    # Test if the return value of print_color_map is correct
    result = print_color_map()
    assert result == 25, f"Expected 25, but got {result}"

    # Test if the captured output matches the expected output
    assert captured_output == expected_output, "The printed color map does not match the expected output."
    
    print("Test passed: All output matches expected values.")

if __name__ == "__main__":
    test_print_color_map()
