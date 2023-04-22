import cv2
import matplotlib.pyplot as plt
import easyocr

def detect_extract(img_path):
    reader = easyocr.Reader(['es', 'en'])
    results = reader.readtext(img_path, paragraph=True)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.imread(img_path)
    spacer = 100

    full_text = ''
    for detection in results: 
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        text = detection[1]
        full_text += text + '\n'
        img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
        # img = cv2.putText(img,text,(20,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)
        spacer+=15

    return full_text, img

if __name__ == '__main__':
    img_path = "training/training4.png"
    out_path = "boxed_images/rectanglebox1.jpg"
    text, img = detect_extract(img_path,out_path)
    print(text)
