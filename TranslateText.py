from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, src_lang='es', tgt_lang='en'):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)   
    inputs = tokenizer.encode(text, return_tensors="pt")
    max_length = inputs.shape[1] 
    outputs = model.generate(inputs, num_beams=4, max_length=max_length, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text



def translate_file(input_file, output_file):
    orig_text = ""
    with open(input_file, 'r', encoding='utf-8') as file:        
        orig_text = file.readlines()


    for line in orig_text:
        translated_text = translate_text(line)
        with open(output_file, 'a', encoding='utf-8') as file:
            file.write(translated_text)



if __name__ == "__main__":
    input_file = "identified_text/text4.txt"
    with open(input_file, 'r', encoding='utf-8') as file:        
        text = file.read()

    # print("Original text:")
    # print(orig_text[0])
    # # word count
    # print(f"Word count: {len(orig_text[0])}")
    # print("Translated text:")
    # for line in orig_text:
    #     translated_text = translate_text(line)
    #     print(translated_text)
    #     # word count
    #     print(f"Word count: {len(translated_text.split())}")
    # # output_file = "translated_texts/text1.txt"
    # # translate_file(input_file, output_file)
    # # print(f"Text translated and saved to '{output_file}'")"

    # text = "Las morsas son conocidas por su apariencia distintiva, que incluye largos colmillos, bigotes y un cuerpo masivo en forma de barril. Se encuentran principalmente en el Océano Ártico y los mares subárticos del hemisferio norte. Las morsas pueden pesar hasta 1,5 toneladas (3000 libras) 0 más, los machos suelen ser más grandes que las hembras. Su piel es gruesa arrugada, con una capa de grasa debajo para mantenerlos calientes en las frías aguas del Ártico _ Los colmillos de una morsa pueden crecer hasta 3 pies (1 metro) de largo y sirven para múltiples propósitos, como establecer el dominio, romper el hielo y ayudar a la morsa a arrastrarse hacia la tierra el hielo. Tienen bigotes largos que juegan un papel clave en la búsqueda de comida en el fondo marino, que son muy sensibles y pueden detectar pequeños movimientos Las morsas son animales sociales y, a menudo, se reúnen en grandes grupos Ilamados manadas que pueden constar de cientos incluso miles de individuos. Están bien adaptados para la vida en el Ártico, con la capacidad de sumergirse en las profundidades del océano en busca de alimento, que consiste principalmente en moluscos bivalvos como las almejas_ Sus bigotes juegan un papel crucial en la localización de alimentos en el fondo marino, ya que son muy sensibles y pueden detectar pequeños movimientos vibraciones. Las morsas se encuentran más en el Océano Ártico y en el polo sur. las morsas les gusta socializar animales y para grupos"
    print(len(text.split()))
    trans = translate_text(text)
    print(trans)
    print(len(trans.split()))
