#edit png image 

from PIL import Image 
import time
current_time = int(time.time())
n = (current_time % 100) + 50

if n % 2 == 0:
    n += 10

print(n)

def edit_image(input_path, output_path, n):
    # Open the image
    image = Image.open(input_path)

    # Get the image size
    width, height = image.size

    # Sum variable to store the total red pixel values
    red_sum = 0    

    # Iterate through each pixel and modify the RGB values
    for x in range(width):
        for y in range(height):
            # Get the original RGB values
            original_pixel = image.getpixel((x, y))

            # Add the number 'n' to each RGB component
            modified_pixel = tuple(component + n for component in original_pixel)

            # Set the modified pixel back to the image
            image.putpixel((x, y), modified_pixel)

    # Save the modified image
    image.save(output_path)
    
    return red_sum

#add n to each RGB component
output_path = "M:\WEDS01\Semester 3 2023\HIT137\Assignment 2\chapter1out.jpg"
sum_red_values = edit_image(
    "M:\WEDS01\Semester 3 2023\HIT137\Assignment 2\chapter1.jpg",
    output_path,
    n
)

# Calculate the sum of red pixel values in the modified image
modified_image = Image.open(output_path)
red_sum = sum(modified_image.getdata(band=0))  # band=0 corresponds to the red channel

print("Sum of red pixel values in the modified image:", red_sum)
