# Image Brightness and Contrast Adjustment
This program allows users to interactively adjust the brightness and contrast of an image using OpenCV. The program creates a window with trackbars to control brightness and contrast and displays the adjusted image in real-time.

# How to Use
- Place an image file named test.jpg in the specified directory.
- Run the script.
- Use the trackbars to adjust the brightness and contrast of the image.

# Code Overview
 # 1- BrightnessContrast Function
 - Retrieves the current positions of the brightness and contrast trackbars.
- Applies the adjustments to the image using the controller function.
- Displays the modified image.
# 2- Controller Function
- Converts brightness and contrast values from the trackbar range to actual range.
- Adjusts the brightness of the image.
- Adjusts the contrast of the image.
- Adds text to the image displaying the current brightness and contrast values.
- Returns the adjusted image.

# 3- Main Function
- Loads the image from the specified path.
- Checks if the image is loaded correctly.
- Creates a copy of the image for processing.
- Creates a window named 'GEEK' for displaying the image and trackbars.
- Creates trackbars for brightness and contrast adjustment.
- Displays the original image in the window.
- Initializes the BrightnessContrast function.
- Waits indefinitely for a key press to close the window.
