import cv2
import numpy as np
#import matplotlib.pyplot as plt

import pytesseract
import csv 
import os

# Get the current file location
file_location = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the file location
os.chdir(file_location)

def identify_text_areas(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply threshold to get image with only b&w (binarization)
    _, thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Get structuring element/kernel that will be used for dilation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 7))

    # Dilate the image - blurring the image vertically
    dilated_step1 = cv2.dilate(thresh, kernel, iterations=3)

    # Get structuring element/kernel that will be used for dilation
    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 1))

    # Dilate the image - Blurring the image horizontally
    dilated = cv2.dilate(dilated_step1, kernel2, iterations=3)

    # Find contours
    ctrs, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    img_copy = img.copy()

    # Initialize an empty list to store the bounding rectangles and OCR outputs
    results = []

    for ctr in ctrs:
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)
        rect = cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0,255,0), 2)
        
        # Crop the bounding rectangle from the grayscale image
        crop_img = gray_img[y:y+h, x:x+w]
        
        # Pass the cropped image to Tesseract OCR and get the output text
        ocr_output = pytesseract.image_to_string(crop_img, lang='spa')
        
        # If the OCR output contains text, store the bounding rectangle coordinates and the OCR output in a list
        if ocr_output.strip():
            results.append((x, y, w, h, ocr_output.strip()))
            
    text = ""
    # Display the results
    for result in results:
        x, y, w, h, new_text = result

        # When we get the largest number of text in the rectangle, replace it.
        if(len(new_text)>=len(text)):
            text = new_text
        
        # Add a green rectangle to the image
        rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return rect, text


if __name__ == "__main__":
    for i in range(1, 5):
        img_path = f"training/training{i}.png"
        rects, texts = identify_text_areas(img_path)
        print(texts)
        cv2.imwrite(f"saved_images/rectanglebox{i}.jpg", rects)
        with open(f"saved_texts/text{i}.txt", "w") as file:
            file.write(texts)
    

    # img = cv2.imread("training/training4.png")
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    # cv2.imwrite('saved_images/threshold_image.jpg',thresh1)

    
    # rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # dilation = cv2.dilate(thresh1, rect_kernel, iterations = 3)
    # cv2.imwrite('saved_images/dilation_image.jpg',dilation)

    # contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # im2 = img.copy()

    # for cnt in contours:
    #     x, y, w, h = cv2.boundingRect(cnt)
        
    #     # Draw the bounding box on the text area
    #     rect=cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    #     # Crop the bounding box area
    #     cropped = im2[y:y + h, x:x + w]
        
    #     cv2.imwrite(f'saved_images/rectanglebox.jpg',rect)
        
        


    # plt.imshow(gray, cmap="gray")
    # plt.savefig("saved_images/gray1.png")



