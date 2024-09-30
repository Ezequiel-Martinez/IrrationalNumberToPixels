from PIL import Image
import math

# Step 1: Read the number from the txt file, with a limit on how many digits to read
def read_pi_digits(file_path, digit_limit=1000000):
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            # Extract the digits after the decimal point
            if '.' in content:
                digits = content.split('.')[1]  # Get digits after the decimal point
            else:
                digits = content

            return digits[:digit_limit]  # Return only up to the specified limit
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit(1)

# Step 2: Define the color schemes
color_schemes = [
    {
        '0': (255, 255, 255), '1': (227, 227, 227), '2': (199, 199, 199), '3': (171, 171, 171),
        '4': (143, 143, 143), '5': (115, 115, 115), '6': (87, 87, 87), '7': (59, 59, 59),
        '8': (31, 31, 31), '9': (3, 3, 3)
    },
    {
        '0': (255, 0, 0), '1': (255, 128, 0), '2': (255, 255, 0), '3': (128, 255, 0),
        '4': (0, 255, 0), '5': (0, 255, 128), '6': (0, 128, 255), '7': (0, 0, 255),
        '8': (128, 0, 255), '9': (255, 0, 255)
    },
    {
        '0': (0, 100, 0), '1': (34, 139, 34), '2': (107, 142, 35), '3': (154, 205, 50),
        '4': (218, 165, 32), '5': (184, 134, 11), '6': (139, 69, 19), '7': (160, 82, 45),
        '8': (188, 143, 143), '9': (216, 191, 216)
    },
    {
        '0': (0, 0, 112), '1': (0, 0, 224), '2': (0, 128, 255), '3': (0, 255, 255),
        '4': (0, 255, 128), '5': (128, 255, 0), '6': (255, 255, 0), '7': (255, 128, 0),
        '8': (255, 64, 0), '9': (255, 0, 0)
    }
]

# Step 3: Calculate the best 16:9 dimensions based on the number of digits
def calculate_image_dimensions(num_digits):
    # Calculate the width and height maintaining a 16:9 ratio (16/9 = width/height)
    # We need width * height >= num_digits
    aspect_ratio = 16 / 9
    height = math.ceil(math.sqrt(num_digits / aspect_ratio))  # Estimate height
    width = math.ceil(aspect_ratio * height)  # Calculate width based on 16:9 ratio
    return width, height

# Step 4: Create the image for a given color scheme
def create_pi_image(digits, color_scheme, output_file):
    num_digits = len(digits)
    width, height = calculate_image_dimensions(num_digits)
    
    img = Image.new('RGB', (width, height), color=(0, 0, 0))  # Default black background
    pixels = img.load()

    for i, digit in enumerate(digits):
        x = i % width  # Calculate the x coordinate
        y = i // width  # Calculate the y coordinate
        if y < height:  # Avoid overflow just in case
            pixels[x, y] = color_scheme.get(digit, (0, 0, 0))  # Map digit to color, default to black if invalid

    img.save(output_file)
    print(f"Image saved as {output_file}, Dimensions: {width}x{height}")

# Step 5: Main function to run the program
def main():
    # Parameters to change directly in the code
    input_file = 'phi-1_000_000.txt'  # Set the input file name here
    output_file_base = 'phi_1M'  # Set the base name for output files here
    digit_limit = 1_000_000  # Limit to 1 million digits

    pi_digits = read_pi_digits(input_file, digit_limit)
    
    # Create an image for each color scheme
    for idx, scheme in enumerate(color_schemes):
        output_file = f'{output_file_base}_{idx + 1}.png'
        create_pi_image(pi_digits, scheme, output_file)

if __name__ == "__main__":
    main()
