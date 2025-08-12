from PIL import Image

# ==============================================================================
# ENCRYPTION FUNCTIONS
# ==============================================================================


def encrypt_swap_channels(image_path, output_path):
    """
    Encrypts an image by swapping the Red and Blue color channels.

    Args:
        image_path (str): The path to the input image.
        output_path (str): The path where the encrypted image will be saved.
    """
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")  # Ensure the image is in RGB format
        encrypted_img = img.copy()

        pixels = encrypted_img.load()
        width, height = encrypted_img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Swap the Red and Blue channels
                pixels[x, y] = (b, g, r)

        encrypted_img.save(output_path)
        print(f"Image successfully encrypted and saved to '{output_path}'")
        return True
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def encrypt_add_constant(image_path, output_path, constant=100):
    """
    Encrypts an image by adding a constant value to each color channel.

    Args:
        image_path (str): The path to the input image.
        output_path (str): The path where the encrypted image will be saved.
        constant (int): The value to add to each color channel (default is 100).
    """
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        encrypted_img = img.copy()

        pixels = encrypted_img.load()
        width, height = encrypted_img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                # Add the constant and use modulo 256 for wrap-around
                new_r = (r + constant) % 256
                new_g = (g + constant) % 256
                new_b = (b + constant) % 256

                pixels[x, y] = (new_r, new_g, new_b)

        encrypted_img.save(output_path)
        print(f"Image successfully encrypted and saved to '{output_path}'")
        return True
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# ==============================================================================
# DECRYPTION FUNCTIONS
# ==============================================================================


def decrypt_swap_channels(image_path, output_path):
    """
    Decrypts an image that was encrypted by swapping Red and Blue channels.
    """
    encrypt_swap_channels(image_path, output_path)


def decrypt_add_constant(image_path, output_path, constant=100):
    """
    Decrypts an image that was encrypted by adding a constant value.
    This function subtracts the constant to reverse the process.
    """
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        decrypted_img = img.copy()

        pixels = decrypted_img.load()
        width, height = decrypted_img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                # Subtract the constant and use modulo 256 for wrap-around
                new_r = (r - constant) % 256
                new_g = (g - constant) % 256
                new_b = (b - constant) % 256

                pixels[x, y] = (new_r, new_g, new_b)

        decrypted_img.save(output_path)
        print(f"Image successfully decrypted and saved to '{output_path}'")
        return True
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# ==============================================================================
# MAIN SCRIPT EXECUTION
# ==============================================================================


if __name__ == "__main__":
    # --- Configuration ---
    # Put an image file in the same directory as this script, or provide a full path.
    # Replace 'input_image.jpg' with the actual filename of your image.
    INPUT_IMAGE_FILE = 'R.jpeg'

    # --- Run the Encryption/Decryption Process ---

    # Example 1: Using channel swapping encryption
    print("\n--- Running Channel Swapping Encryption ---")
    if encrypt_swap_channels(INPUT_IMAGE_FILE, 'encrypted_swap.png'):
        print("\n--- Decrypting Channel Swapping Image ---")
        decrypt_swap_channels('encrypted_swap.png', 'decrypted_swap.png')

    # Example 2: Using constant addition encryption
    print("\n--- Running Constant Addition Encryption ---")
    if encrypt_add_constant(INPUT_IMAGE_FILE, 'encrypted_add.png', constant=100):
        print("\n--- Decrypting Constant Addition Image ---")
        decrypt_add_constant('encrypted_add.png',
                             'decrypted_add.png', constant=100)
