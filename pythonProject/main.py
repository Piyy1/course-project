from PIL import Image, ImageTk
import tkinter as tk
import os

def compress_image(input_path, output_path, quality=95):
    # Open the input image
    with Image.open(input_path) as img:
        # Save the image with the specified quality
        img.save(output_path, quality=quality)

def crop_image(img, box):

    return img.crop(box)

def show_images(original_path, compressed_path, crop_box):

    # Create a new window
    root = tk.Tk()
    root.title("Image Comparison")
    root.geometry("1480x1920")  # Set window size

    # Load the original image
    original_img = Image.open(original_path)
    original_width, original_height = original_img.size
    # Load the compressed image
    compressed_img = Image.open(compressed_path)

    # Convert percentage values to absolute pixel values
    left, upper, right, lower = crop_box
    left_pixel = int(left * original_width)
    upper_pixel = int(upper * original_height)
    right_pixel = int(right * original_width)
    lower_pixel = int(lower * original_height)

    # Crop the original image
    original_cropped_img = crop_image(original_img, (left_pixel, upper_pixel, right_pixel, lower_pixel))

    # Crop the compressed image
    compressed_cropped_img = crop_image(compressed_img, (left_pixel, upper_pixel, right_pixel, lower_pixel))

    # Load and display the cropped original image
    original_photo = ImageTk.PhotoImage(original_cropped_img)
    original_label = tk.Label(root, image=original_photo)
    original_label.grid(row=0, column=0, padx=5, pady=5)

    # Load and display the cropped compressed image
    compressed_photo = ImageTk.PhotoImage(compressed_cropped_img)
    compressed_label = tk.Label(root, image=compressed_photo)
    compressed_label.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Original Image", font=("Helvetica", 12)).grid(row=1, column=0)
    tk.Label(root, text="Compressed Image", font=("Helvetica", 12)).grid(row=1, column=1)

    # Save the compressed image along the path of the original image
    output_dir = os.path.dirname(original_path)
    compressed_filename = os.path.basename(compressed_path)
    compressed_output_path = os.path.join(output_dir, compressed_filename)
    compressed_img.save(compressed_output_path)

    # Start the GUI event loop
    root.mainloop()

# Paths for input image
input_image_path = 'file:///D://Dimas//Task1.jpg'

# Output path for compressed image
output_image_path = os.path.join(os.path.dirname(input_image_path), 'compressed_output.jpg')

# Compress the images without loss
compress_image(input_image_path, output_image_path)

# Specify the bounding box for cropping as percentages (left, upper, right, lower)
crop_box = (0.2, 0.3, 0.4, 0.6)

# Display the original and compressed images, cropped to the specified bounding box
show_images(input_image_path, output_image_path, crop_box)
