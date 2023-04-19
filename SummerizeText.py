from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.utils import get_stop_words

# Load the text to be summarized
text = "Las morsas son conocidas por su apariencia distintiva, que incluye largos colmillos, bigotes y un cuerpo masivo en forma de barril. Se encuentran principalmente en el Océano Ártico y los mares subárticos del hemisferio norte. Las morsas pueden pesar hasta 1,5 toneladas (3000 libras) o más, y los machos suelen ser más grandes que las hembras. Su piel es gruesa y arrugada, con una capa de grasa debajo para mantenerlos calientes en las frías aguas del Ártico. Los colmillos de una morsa pueden crecer hasta 3 pies (1 metro) de largo y sirven para múltiples propósitos, como establecer el dominio, romper el hielo y ayudar a la morsa a arrastrarse hacia la tierra o el hielo. Tienen bigotes largos que juegan un papel clave en la búsqueda de comida en el fondo marino, que son muy sensibles y pueden detectar pequeños movimientos. Las morsas son animales sociales y, a menudo, se reúnen en grandes grupos llamados manadas, que pueden constar de cientos o incluso miles de individuos. Están bien adaptados para la vida en el Ártico, con la capacidad de sumergirse en las profundidades del océano en busca de alimento, que consiste principalmente en moluscos bivalvos como las almejas. Sus bigotes juegan un papel crucial en la localización de alimentos en el fondo marino, ya que son muy sensibles y pueden detectar pequeños movimientos o vibraciones. Las morsas se encuentran más en el Océano Ártico y en el polo sur. A las morsas les gusta socializar animales y para grupos"

# Set up the parser and tokenizer
parser = PlaintextParser.from_string(text, Tokenizer("spanish"))

# Set up the summarizer
summarizer = TextRankSummarizer()

# Set the language for stop words
summarizer.stop_words = get_stop_words("spanish")

# Generate a summary of 2 sentences
summary = summarizer(parser.document, sentences_count=2)

# Print the summary
for sentence in summary:
    print(sentence)
  
# Toy Example untill I get the translated text

# Load the text to be summarized
text = "This methodology will be developed within a Github repo and although this is a group effort your individual contributions to the implementation will be tracked through the commits. You can use libraries for various aspects such as the character recognition part, or use pretrained models, but if you use an ’online resource’ such as Google Translate points will be deducted although partial credit will be awarded (advisable if you cannot progress to the next stages being stuck on the translation phase). The implementation should receive as input a file name to a new image, and produce the translated text as well as the summarized text as output. It will help for partial credit if you also demonstrate the intermediate stages, eg. with the bounding boxes on the original image. Documentation and code comments will help award partial credit"

# Set up the parser and tokenizer
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Set up the summarizer
summarizer = TextRankSummarizer()

# Set the language for stop words
summarizer.stop_words = get_stop_words("english")

# Generate a summary of 2 sentences
summary = summarizer(parser.document, sentences_count=2)

# Print the summary
for sentence in summary:
    print(sentence)
