# Bank-Check-Parser using OCR
A web application created using flask to parse and read checks and extract required information and insert into a database

Problem:
Extract information from the image of Bank Cheque by OCR in proper format.
	Information like - Amount paid/received , Sender's name.

Solution:

Steps: 
	-> Run the flask application and go to the port address on your web.
	-> Select the folder(containing check images) on flask web page(web portal)
	-> crop to box(which has required information in it)  
	-> save the cropped images in a folder "crop"
	-> give "crop" folder to tesseract
	-> retrieve text and display on the page.(output of tesseract)
	-> Store the data in an excel sheet

Prerequisites and dependent packages:

Download and Install Python IDE on your system

Then install the required packages:

1.Tesseract:
sudo apt-get install tesseract-ocr

2.Pytesseract:
sudo pip install pytesseract / sudo apt-get install pytesseract

3.Python Imaging Library (PIL):
sudo pip install pillow

4.Flask:
sudo pip install flask

Follow the instructions here to install flask and create and set up your virtual environment and directories.

https://www.pluralsight.com/courses/flask-micro-framework-introduction

5.Opencv
sudo apt-get install python-opencv

6.numpy:
	Ubuntu: 
		via pip: python -m pip install --user numpy
		system-wide installation: sudo apt-get install python-numpy

7.Re(regular expressions) and xlrd(for excel sheet)
-xlrd: pip install xlrd
-re: pip install re


Directories:

*check(main directory)-
	created as per flask requirement i.e, contains static,templates and all code files along with the images and crop folders.		
	
*images-
	which contains testing images

*crop
	it contains cropped images
	
*static-
	contains a folder containing .css files and another folder containing the uploaded files 

*templates-
	contains the .html files




Running the Application:
1.run the .profile code:
	~$ . .profile
	~$ workon check

2. change directory as created, in this case
	~$ cd check

3.Browse to the project folder in your terminal and run:
	~$ python ocr1.py

4.Open your browser and browse to the following address:

http://localhost:5000/upload

