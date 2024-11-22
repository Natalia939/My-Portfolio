import sys
import os
from PIL import Image, ImageOps


def main():
    # Ensure correct number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" if len(sys.argv)
                 < 3 else "Too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Check if input and output files have valid extensions
    valid_extensions = (".jpg", ".jpeg", ".png")
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid output")

    # Ensure input and output files have the same extension
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # Ensure the input file exists
    if not os.path.exists(input_path):
        sys.exit("Input does not exist")

    try:
        # Open the input image and the shirt image
        input_image = Image.open(input_path)
        shirt_image = Image.open("shirt.png")

        # Resize and crop the input image to match the shirt's size
        resized_image = ImageOps.fit(input_image, shirt_image.size)

        # Overlay the shirt on the resized input image
        resized_image.paste(shirt_image, shirt_image)

        # Save the result to the output path
        resized_image.save(output_path)

    except Exception as e:
        sys.exit(f"Error: {e}")


if __name__ == "__main__":
    main()
