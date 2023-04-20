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
  
    
# Load the text to be summarized 1st image   
text = "Walruses are known for their distinctive appearance, which includes long tusks, whiskers, and a massive barrel-shaped body. They are found mainly in the Arctic Ocean and the subarctic seas of the Northern Hemisphere. Walruses can weigh up to 1.5 tons (3,000 pounds) or more, with males often being larger than females. Their skin is thick and wrinkled, with a layer of fat underneath to keep them warm in the cold arctic waters. A walrus' tusks can grow up to 3 feet (1 meter) long and serve multiple purposes, such as establishing dominance, breaking ice, and helping the walrus crawl onto land or ice. They have long whiskers that play a key role in searching for food on the seabed, which are very sensitive and can detect small movements. Walruses are social animals and often gather in large groups called herds, which can number hundreds or even thousands of individuals. They are well adapted for life in the Arctic, with the ability to dive deep into the ocean in search of food, which mainly consists of bivalve molluscs such as clams. Their whiskers play a crucial role in locating food on the seabed, since they are very sensitive and can detect small movements or vibrations. Walruses are found more in the Arctic Ocean and at the south pole. Walruses like to socialize animals and for groups."

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

#They have long whiskers that play a key role in searching for food on the seabed, which are very sensitive and can detect small movements.
#Walruses are found more in the Arctic Ocean and at the south pole.




# Load the text to be summarized 2nd image 
text = "Come in and try the famous cheese we have to offer. This cheese is world famous and has received positive reviews from critics who know the best cheeses. Many say that it is the best cheese they have ever tasted and we believe that you will have the same opinion. We store the cheese here ourselves and it is never inside plastic. We also serve wine with the cheese if you wish, but our cheese is so good that most come just for the cheese. We close at 6pm every day. Lots of people stay until we close at 6 pm because the cheese is so famous. When you receive your cheese there will be no plastic. You will be one of the many who think that we have the best cheese in the world and we have to see that and hopefully soon. Join us in celebrating the best cheese of the world."

# Set up the parser and tokenizer
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Set up the summarizer
summarizer = TextRankSummarizer()

# Set the language for stop words
summarizer.stop_words = get_stop_words("english")

# Generate a summary of 2 sentences
summary2 = summarizer(parser.document, sentences_count=2)

# Print the summary
for sentence in summary2:
    print(sentence)
#We also serve wine with the cheese if you wish, but our cheese is so good that most come just for the cheese.
#You will be one of the many who think that we have the best cheese in the world and we have to see that and hopefully soon.





# Load the text to be summarized 3rd image 
text = "The Honda Civic is a popular compact car manufactured by the Honda Motor Company, with a long history dating back to 1972. Over the years, the Civic has gone through several generations and has been available in various body styles, including sedans. , hatchback and coupe.. As a result, the specifications of a Honda Civic can vary depending on the model year and toe level. To the best of my knowledge, in September 2021, the last generation of the equipment. up to 177 lb-ft of torque. Here are some general specifications of the 2022 Honda Civic: Body Styles: The 2022 Honda Civic is available in sedan and hatchback body styles. Engine Options: The 2022 Civic offers two engine options: a 2.0-liter naturally aspirated 4-cylinder engine that produces 158 horsepower and 138 lb-ft of torque, and a 1.5-liter turbocharged 4-cylinder engine that generates 180 horsepower and Transmission Options: The base engine comes with a continuously variable transmission (CVT), while the turbocharged engine is available with a CVT or 6-speed manual transmission (for Sport hatchback model only). Fuel Economy: The 2022 Honda Civic boasts impressive fuel efficiency, with EPA-estimated ratings ranging from 28-31 mpg city and 37-40 mpg highway, depending on engine and transmission combination. doors in September. With a 1169cc transverse engine and front-wheel drive like the British Mini, the car provided a The first generation Civic was introduced in July 1972 as a two-door coupe model, followed by a reliable and fuel-friendly three-fuel hatchback. environmentally friendly, but later iterations have become known for their performance and good interior space despite small overall dimensions. It initially earned a reputation for fuel-efficient sportiness, especially the Civic Type R, Civic VTi, Civic GTi, and Civic SiR/Si."

# Set up the parser and tokenizer
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Set up the summarizer
summarizer = TextRankSummarizer()

# Set the language for stop words
summarizer.stop_words = get_stop_words("english")

# Generate a summary of 2 sentences
summary3 = summarizer(parser.document, sentences_count=2)

# Print the summary
for sentence in summary3:
    print(sentence)
# Here are some general specifications of the 2022 Honda Civic: Body Styles: The 2022 Honda Civic is available in sedan and hatchback body styles.
# Engine Options: The 2022 Civic offers two engine options: a 2.0-liter naturally aspirated 4-cylinder engine that produces 158 horsepower and 138 lb-ft 
# of torque, and a 1.5-liter turbocharged 4-cylinder engine that generates 180 horsepower and Transmission Options: The base engine comes with 
# a continuously variable transmission (CVT), while the turbocharged engine is available with a CVT or 6-speed manual transmission (for Sport hatchback 
#model only).





# Load the text to be summarized 4th image 
text = "In the kingdom of numbers, where data resides, A world of patterns and secrets hides. Statistics, the art that seeks the truth to transmit, From chaos, order, finds a way. With tools in hand, the statistician delves, Through samples and graphics, a story that tells. mean, median, mode, the measures of the center, Spread and bias, no details will go into it. A dance of probability, an intricate ballet, Normal distributions lead the way. Confidence intervals, a range to display. The truth, with margins, portray."

# Set up the parser and tokenizer
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Set up the summarizer
summarizer = TextRankSummarizer()

# Set the language for stop words
summarizer.stop_words = get_stop_words("english")

# Generate a summary of 2 sentences
summary4 = summarizer(parser.document, sentences_count=2)

# Print the summary
for sentence in summary4:
    print(sentence)
#In the kingdom of numbers, where data resides, A world of patterns and secrets hides.
#Statistics, the art that seeks the truth to transmit, From chaos, order, finds a way.
