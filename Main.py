Simple Image Encryption Tool
Author: Piyush

Description:
This utility provides basic image encryption and decryption functionality using two lightweight techniques designed for educational or demonstration purposes:

Pixel Swapping – Performs adjacent pixel value swaps to lightly obfuscate the image structure.

Mathematical Transformation – Applies a reversible mathematical operation to each pixel, offering an additional layer of basic encryption.

from PIL import Image
import numpy as np
import argparse


def encrypt_image(image_path, output_path, method="swap"):
    image = Image.open(image_path).convert("RGB")
    pixels = np.array(image)

    if method == "swap":
        encrypted_pixels = swap_pixels(pixels)
    elif method == "math":
        encrypted_pixels = math_operation(pixels)
    else:
        raise ValueError("Choose 'swap' or 'math' as method.")

    Image.fromarray(encrypted_pixels.astype("uint8"), "RGB").save(output_path)
    print(f"✅ Encryption successful! Saved to: {output_path}")


def decrypt_image(image_path, output_path, method="swap"):
    image = Image.open(image_path).convert("RGB")
    pixels = np.array(image)

    if method == "swap":
        decrypted_pixels = swap_pixels(pixels)  # swap is reversible
    elif method == "math":
        decrypted_pixels = reverse_math_operation(pixels)
    else:
        raise ValueError("Choose 'swap' or 'math' as method.")

    Image.fromarray(decrypted_pixels.astype("uint8"), "RGB").save(output_path)
    print(f"🔓 Decryption successful! Saved to: {output_path}")


def swap_pixels(pixels):
    swapped = pixels.copy()
    rows, cols, _ = pixels.shape
    for i in range(rows):
        for j in range(0, cols - 1, 2):
            swapped[i, j], swapped[i, j + 1] = (
                swapped[i, j + 1],
                swapped[i, j],
            )  # Swapping horizontally
    return swapped


def math_operation(pixels):
    constant = 37
    return (pixels + constant) % 256


def reverse_math_operation(pixels):
    constant = 37
    return (pixels - constant) % 256


def main():
    parser = argparse.ArgumentParser(
        description="🖼️ Simple Image Encryption/Decryption Tool"
    )
    parser.add_argument(
        "mode",
        choices=["encrypt", "decrypt"],
        help="Choose to encrypt or decrypt an image.",
    )
    parser.add_argument("input", help="Path to the input image file.")
    parser.add_argument("output", help="Path to save the output image file.")
    parser.add_argument(
        "--method",
        choices=["swap", "math"],
        default="swap",
        help="Choose encryption method: 'swap' or 'math'.",
    )

    args = parser.parse_args()

    print("🔐 Processing...")
    if args.mode == "encrypt":
        encrypt_image(args.input, args.output, args.method)
    else:
        decrypt_image(args.input, args.output, args.method)


if __name__ == "__main__":
    main()
