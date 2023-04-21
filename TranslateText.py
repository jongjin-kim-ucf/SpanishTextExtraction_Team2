from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, src_lang='es', tgt_lang='en'):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)   
    inputs = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(inputs, num_beams=4, max_length=50, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

def translate_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    translated_text = translate_text(text)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

if __name__ == "__main__":
    input_file = "original_texts/text1.txt"
    output_file = "translated_texts/text1.txt"
    translate_file(input_file, output_file)
    print(f"Text translated and saved to '{output_file}'")

    text = "Hola, ¿cómo estás?"
    print(translate_text(text))
