import cv2 

def BrightnessContrast(*args): 
    # Get the current positions of the trackbars
    brightness = cv2.getTrackbarPos('Brightness', 'controlWindow') 
    contrast = cv2.getTrackbarPos('Contrast', 'controlWindow') 

    # Apply the brightness and contrast adjustments
    effect = controller(img, brightness, contrast) 

    # Display the modified image
    cv2.imshow('Effect', effect) 

def controller(img, brightness=255, contrast=127): 
    # Convert brightness and contrast from trackbar range to actual range
    brightness = int((brightness - 255) * (255 / 255))
    contrast = int((contrast - 127) * (127 / 127))

    # Apply brightness adjustment
    if brightness != 0: 
        if brightness > 0: 
            shadow = brightness 
            max = 255
        else: 
            shadow = 0
            max = 255 + brightness 

        al_pha = (max - shadow) / 255
        ga_mma = shadow 
        cal = cv2.addWeighted(img, al_pha, img, 0, ga_mma) 
    else: 
        cal = img 

    # Apply contrast adjustment
    if contrast != 0: 
        alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast)) 
        gamma = 127 * (1 - alpha) 
        cal = cv2.addWeighted(cal, alpha, cal, 0, gamma) 

    # Add text to the image displaying the current brightness and contrast values
    cv2.putText(cal, 'B:{},C:{}'.format(brightness, contrast), (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) 

    return cal 

if __name__ == '__main__': 
    # Load the image
    original = cv2.imread("/Users/sparshsinghal/Desktop/sorting visualizer/image_processing/images/test.jpg") 

    if original is None:
        raise FileNotFoundError("The image file 'test.jpeg' could not be read. Please check the file path and ensure the file exists.")

    # Make a copy of the image
    img = original.copy() 

    # Create a window for the trackbars
    cv2.namedWindow('controlWindow') 

    # Create trackbars for brightness and contrast
    cv2.createTrackbar('Brightness', 'controlWindow', 255, 2 * 255, BrightnessContrast)
    cv2.createTrackbar('Contrast', 'controlWindow', 127, 2 * 127, BrightnessContrast)

    # Display the original image
    cv2.imshow('controlWindow', original) 

    # Call the function once to initialize
    BrightnessContrast() 

    # Wait indefinitely until a key is pressed
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
