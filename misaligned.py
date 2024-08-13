
def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append((i * 5 + j, major, minor))  # Store as tuple
    return color_map

def print_color_map(color_map):
    for entry in color_map:
        print(f'{entry[0]:<2} | {entry[1]:<6} | {entry[2]:<6}')  # Format output with fixed width

def test_generate_color_map():
    expected_color_map = [
        (0, 'White', 'Blue'), (1, 'White', 'Orange'), (2, 'White', 'Green'),
        (3, 'White', 'Brown'), (4, 'White', 'Slate'), (5, 'Red', 'Blue'),
        (6, 'Red', 'Orange'), (7, 'Red', 'Green'), (8, 'Red', 'Brown'),
        (9, 'Red', 'Slate'), (10, 'Black', 'Blue'), (11, 'Black', 'Orange'),
        (12, 'Black', 'Green'), (13, 'Black', 'Brown'), (14, 'Black', 'Slate'),
        (15, 'Yellow', 'Blue'), (16, 'Yellow', 'Orange'), (17, 'Yellow', 'Green'),
        (18, 'Yellow', 'Brown'), (19, 'Yellow', 'Slate'), (20, 'Violet', 'Blue'),
        (21, 'Violet', 'Orange'), (22, 'Violet', 'Green'), (23, 'Violet', 'Brown'),
        (24, 'Violet', 'Slate')
    ]
    generated_color_map = generate_color_map()
    
    # Test if the generated color map matches the expected color map
    assert generated_color_map == expected_color_map, "Generated color map does not match the expected output"

if __name__ == "__main__":
    color_map = generate_color_map()
    print_color_map(color_map)
    test_generate_color_map()
