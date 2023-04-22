### Main Functions ####
from FindTextAreas import detecttextarea
from ExtractText import extract_text
from TranslateText import translate_text
from SummerizeText import summarize_text

for i in range(1, 5):
    
    
    # Detect Text Area of the images
    img_path = f"training/training{i}.png"
    out_path = f"boxed_images/rectanglebox{i}.jpg"
    
    print("############## Text Area Detection ###############")
    boxes, _ = detecttextarea(img_path, out_path)
    print("There are {} boxes detected.".format(boxes.shape[0]))
        
    # Extract the text
    img_path = f"training/training{i}.png"
    out_path = f"saved_texts/text{i}.txt"
    print("############## Extract Text ###############")
    texts = extract_text(img_path, out_path)
    print(texts)
    
    # Translate the text    
    print("############## Translate Text to English ###############")
    text_eng = translate_text(texts)
    print(text_eng)
    
    # Summarize the text
    print("############## Summarize Text ###############")
    summary = summarize_text(text_eng)
    print(summary)