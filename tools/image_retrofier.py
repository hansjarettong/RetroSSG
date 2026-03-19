import sys
from PIL import Image


def retroify(input_path, output_path, target_resolution=(640, 480), bit_depth=8):
    # Open the image
    original_image = Image.open(input_path)

    # Calculate the resolution factor to achieve the target resolution
    width, height = original_image.size
    resolution_factor = max(
        width // target_resolution[0], height // target_resolution[1]
    )

    # Reduce resolution
    new_size = (width // resolution_factor, height // resolution_factor)
    resized_image = original_image.resize(new_size)

    # Set bit depth
    reduced_bit_depth_image = resized_image.convert(
        "P", palette=Image.ADAPTIVE, colors=2**bit_depth
    )

    # Save the retro image
    reduced_bit_depth_image.save(output_path)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: python image_retrofier.py input_image_path output_image_path [bit_depth] [resolution_width resolution_height]"
        )
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    # Set default values
    target_resolution = (640, 480)
    bit_depth = 8

    # Check if bit_depth is provided
    if len(sys.argv) > 3:
        bit_depth = int(sys.argv[3])

    # Check if target_resolution is provided
    if len(sys.argv) == 6:
        target_resolution = (int(sys.argv[4]), int(sys.argv[5]))

    retroify(input_image_path, output_image_path, target_resolution, bit_depth)
