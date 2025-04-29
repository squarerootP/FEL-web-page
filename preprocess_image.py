from PIL import Image

def overlay_three_images(background_path, middle_image_path, foreground_path, output_path, position1=(0, 0), position2=(0, 0)):
    """
    Overlays a middle image and a foreground image (with transparency) onto a background image.
    If background and foreground have different dimensions, resizes the larger to match the smaller.

    Args:
        background_path (str): Path to the background image file.
        middle_image_path (str): Path to the middle image file (must be PNG for transparency).
        foreground_path (str): Path to the foreground image file (must be PNG for transparency).
        output_path (str): Path to save the resulting overlaid image.
        position1 (tuple): (x, y) coordinates for the top-left corner of the middle image.
        position2 (tuple): (x, y) coordinates for the top-left corner of the foreground image.
    """
    try:
        background = Image.open(background_path).convert("RGBA")
        middle_image = Image.open(middle_image_path).convert("RGBA")
        foreground = Image.open(foreground_path).convert("RGBA")

        # Check and resize background and foreground to match dimensions
        bg_width, bg_height = background.size
        fg_width, fg_height = foreground.size
        
        if bg_width != fg_width or bg_height != fg_height:
            print("Background and foreground dimensions don't match. Resizing the larger one.")
            if bg_width * bg_height > fg_width * fg_height:
                # Background is larger, resize it to match foreground
                background = background.resize((fg_width, fg_height))
                bg_width, bg_height = fg_width, fg_height
            else:
                # Foreground is larger, resize it to match background
                foreground = foreground.resize((bg_width, bg_height))

        # Check and resize middle image if it's larger than bg/fg
        mid_width, mid_height = middle_image.size
        if mid_width > bg_width or mid_height > bg_height:
            print("Middle image is larger than background/foreground. Resizing to fit.")
            # Calculate the resize ratio while maintaining aspect ratio
            ratio = min(bg_width / mid_width, bg_height / mid_height)
            new_size = (int(mid_width * ratio), int(mid_height * ratio))
            middle_image = middle_image.resize(new_size)
            mid_width, mid_height = middle_image.size

        # Ensure the middle image has an alpha channel
        if middle_image.mode != 'RGBA':
            print("Warning: Middle image does not have an alpha channel. Transparency might not work as expected.")
            
        # Make sure the middle image fits within the background
        if position1[0] + mid_width > bg_width or position1[1] + mid_height > bg_height:
            print("Warning: Middle image goes beyond the bounds of the background.")
            
        # Create a new composite image starting with background
        composite = background.copy()
        
        # Overlay the middle image onto the background
        composite.paste(middle_image, position1, middle_image)
        
        # Overlay the foreground
        composite.paste(foreground, position2, foreground)

        # Save the result
        composite.save(output_path)
        print(f"Successfully overlaid '{middle_image_path}' and '{foreground_path}' onto '{background_path}' and saved to '{output_path}'.")

    except FileNotFoundError:
        print("Error: One or more of the image files were not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    background_image = r"C:\Users\Admin\Desktop\FEL\FEL-main\fel-webpage\assets\images\automation\back.png"    # Background image path
    middle_image = r"C:\Users\Admin\Desktop\FEL\FEL-main\fel-webpage\assets\images\people\creator_1.png"                     # Middle image to be overlaid
    foreground_image = r"C:\Users\Admin\Desktop\FEL\FEL-main\fel-webpage\assets\images\automation\front.png"   # Foreground image path
    output_image = r"C:\Users\Admin\Desktop\FEL\FEL-main\fel-webpage\assets\images\people\output.png"                        # Output path
    middle_position = (0, 0)                                  # Position for middle image
    foreground_position = (0, 0)                              # Position for foreground (usually 0,0 to cover entire bg)

    overlay_three_images(background_image, middle_image, foreground_image, output_image, middle_position, foreground_position)