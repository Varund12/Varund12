#name: Varun Dawrha
# pytesseract library, is a Optical Character Recognition tool 
# To read and recognize the text in images,.
import pytesseract

#Importing the `Image` class from the PIL (Python Imaging Library).
from PIL import Image

# Setting the path to the Tesseract where it is installed in the computer.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Loading the image from the location in the computer
image_path = 'C:/Users/conra/OneDrive/Intern Project_2023_7/Varun\VDTEXT.png'

#Opening the image from the path
image = Image.open(image_path)


# The extracted text is assigned to the variable `text`
#Using string because of the text
text = pytsesseract.image_to_string(image)
#Title
print("                          Extracting the text from the image \n")

# Printting the extracted text
print(text)

#total no. of characters.
print("Total Number of characters: ")
print(len(text))

#=================================================================================#


# Importing the library.
import matplotlib.pyplot as plt

# Line graphing x and y.


# Opening lines in the text file.
for line in open(r'', 'r'):
    # Splitting the lines into x and y.
    
    
    # Checking if the line has enough elements.

        # Appending x and y values.
        
    
# Labels.


# Display the graph.
