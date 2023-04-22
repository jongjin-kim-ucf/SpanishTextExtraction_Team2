import cv2
import pytesseract
import os
import csv

os.environ['TESSDATA_PREFIX'] = 'C:/Program Files/Tesseract-OCR/tessdata/'

def extract_text(img_path, out_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Apply threshold to get image with only b&w (binarization)
#    threshold_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)[1]
    
    details = pytesseract.image_to_data(thresh, output_type = pytesseract.Output.DICT, lang='spa')
    
    parse_text = []
    word_list = []
    last_word = ''
    
    for word in details['text']:
        if word != '':
            word_list.append(word)
        if (last_word != '' and word == '') or (word == details['text'][-1]):
            parse_text.append(word_list)
            word_list = []

    with open(out_path, "w", newline = "") as file:
        csv.writer(file, delimiter = " ").writerows(parse_text)

    results = []
    for inner_list in parse_text:
        if inner_list:  # check if the inner list is not empty
            string = ' '.join(inner_list)
            results.append(string)

    out = "".join(results)

    # Print the extracted text
    return out

if __name__ == "__main__":
    for i in range(1, 5):
        img_path = f"training/training{i}.png"
        out_path = f"saved_texts/text{i}.txt"
        parse_text = extract_text(img_path, out_path)
        print(parse_text)


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



