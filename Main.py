Simple Image Encryption Tool
Author: Piyush

Description:
This utility provides basic image encryption and decryption functionality using two lightweight techniques designed for educational or demonstration purposes:

Pixel Swapping – Performs adjacent pixel value swaps to lightly obfuscate the image structure.

Mathematical Transformation – Applies a reversible mathematical operation to each pixel, offering an additional layer of basic encryption.

from PIL import Image

def encrypt_image(image_path, output_path, operation_type, key=None):
    """
    🔒 Encrypt an image by changing its pixels.

    Args:
        image_path (str): Path to the original image.
        output_path (str): Where to save the encrypted image.
        operation_type (str): 'swap' to swap colors, or 'math' to modify color values.
        key (int, optional): A number used only if 'math' is selected.
    """
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    if operation_type == 'swap':
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (b, g, r)
    elif operation_type == 'math':
        if key is None:
            raise ValueError("⚠️ You need to provide a key when using 'math' operation.")
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    else:
        raise ValueError("❌ Invalid operation_type. Use 'swap' or 'math'.")

    img.save(output_path)
    print(f"✅ Image encrypted successfully! Saved to: {output_path} 🔐")

def decrypt_image(image_path, output_path, operation_type, key=None):
    """
    🔓 Decrypt an image back to its original form.

    Args:
        image_path (str): Path to the encrypted image.
        output_path (str): Where to save the decrypted image.
        operation_type (str): 'swap' or 'math' (must match encryption).
        key (int, optional): The same number used for 'math' encryption.
    """
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    if operation_type == 'swap':
        for y in range(height):
            for x in range(width):
                b, g, r = pixels[x, y]
                pixels[x, y] = (r, g, b)
    elif operation_type == 'math':
        if key is None:
            raise ValueError("⚠️ You need to provide the key used during encryption.")
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    else:
        raise ValueError("❌ Invalid operation_type. Use 'swap' or 'math'.")

    img.save(output_path)
    print(f"✅ Image decrypted successfully! Saved to: {output_path} 🔓")


# 🧪 Example usage
if __name__ == "__main__":
    print("🔄 Starting image encryption and decryption examples...\n")

    # Example 1: Swap method
    print("🔁 Using 'swap' method...")
    encrypt_image("input.png", "encrypted_swap.png", "swap")
    decrypt_image("encrypted_swap.png", "decrypted_swap.png", "swap")

    # Example 2: Math method
    encryption_key = 50
    print("\n➕ Using 'math' method with key =", encryption_key)
    encrypt_image("input.png", "encrypted_math.png", "math", key=encryption_key)
    decrypt_image("encrypted_math.png", "decrypted_math.png", "math", key=encryption_key)

    print("\n🎉 All done! Check your output images.")
