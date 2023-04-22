# This is the team project in the course STA 7722 by Dr. Alexander Mantzaris.

## Getting Started

To run the project, please execute `main.ipynb`. This notebook combines all the work from separate Python files, which have been organized by specific tasks.

### Running `main.ipynb`

1. Clone the repository to your local machine.
2. Ensure that you have installed the required dependencies mentioned in the `requirements.txt` file.
3. Open the Jupyter Notebook by running `jupyter notebook` in your terminal or command prompt.
4. Navigate to the project directory and open `main.ipynb`.
5. Run all the cells in the notebook to see the output.

By following these steps, you will be able to run the project and observe the results of the integrated tasks from the separate Python files.



## Team 2: Jongjin Kim, Ifte Khairul Islam, Chandra Kundu, Ibrahim Almansour.

The first thing to do is as follows:

1. Clone the repository `git clone`
2. Make changes in the document.
3. Stage changes in the local repository. `git add .`
4. Commit changes with message to the local repository. `git commit -m "New Update"`
5. Push changes. `git push` 

## (Works to do)
+ Analyze the image to identify the text areas
- Find the area of interest with texts or draw a box for the area with texts
+ Extract the text as a string
- Map the image to a spanish dictionary - Use the prebuilt model.
+ Translate the text into Englilsh
- Build a translator between spanish to english.
+ Then summarize the text
+ Final output is the text and summary

(Important Date)
April 21st - Due date of the project

(Assignment)\
Chandra Kundu - Identify Text Areas \
Jongjin Kim - Extract Texts \
Ifte Khairul Islam - Text Translator \
Ibrahim Almansour - Text Summarizer 

(Challenges) \
Picture 1 - Works best because there is no distortion. \
Picture 2 - Works better in the bottom part than the top part. The top part has a distortion. \
Picture 3 - A lot of distortion makes it hard to apprehend. \
Picture 4 - Multiple areas detection is needed. Also, the windows of the building were detected as a rectangle area. 

# Image 
![Original Image](training/training3.png)

# Text Area Detection
![Boxed Image](identified_textareas/img3.jpg)

# Text Extraction
[text3.txt](identified_text/text3.txt)

# English Translation
[translate_text3.txt](translated_text/translate_text3.txt)

# Summary of the text
[summary_text3.txt](summarized_text/summary_text3.txt)
