import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyocr
import pyocr.builders
from PIL import Image
import pytesseract
import os
import csv

os.environ['TESSDATA_PREFIX'] = 'C:/Program Files/Tesseract-OCR/tessdata/'

def extract_text(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray_img, (5, 5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    # Apply threshold to get image with only b&w (binarization)
#    threshold_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)[1]

    custom_config = r'--oem 3 --psm 3'
    
    details = pytesseract.image_to_data(opening, output_type=pytesseract.Output.DICT, config=custom_config, lang='spa')
    
    parse_text = []
    word_list = []
    last_word = ''
    
    for word in details['text']:
        if word != '':
            word_list.append(word)
        if (last_word != '' and word == '') or (word == details['text'][-1]):
            parse_text.append(word_list)
            word_list = []

    # Print the extracted text
    return parse_text

if __name__ == "__main__":
    for i in range(1, 5):
        img_path = f"training/training{i}.png"
        parse_text = extract_text(img_path)
        with open(f"saved_texts/text{i}.txt", "w", newline = "") as file:
            csv.writer(file, delimiter = " ").writerows(parse_text)

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



