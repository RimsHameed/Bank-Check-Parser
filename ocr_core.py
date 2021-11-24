try:
    from PIL import Image
except ImportError:
    import Image
import glob
import re
import pytesseract
import xlrd

def ocr_core(path):
    """
    This function will handle the core OCR processing of images.
    """
    path = "/home/raniya/dev/check/crop/*.*" #give the path of the image folder where the cropped images are saved
    for file in glob.glob(path):
        text = pytesseract.image_to_string(Image.open(file))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
        y="".join(text).replace('\n'," ")
        Outputfile = open('out1.txt','a+')
        Outputfile.write('\n')
        for k in str(y.split("\n")).split('FOR'):
            Outputfile.write(re.sub(r"[^a-zA-Z0-9.]+",' ',k))
        Outputfile1=open('out1.xlsx','a+')
        for k1 in str(y.split("\n")).split('FOR'):
            Outputfile1.write(re.sub(r"[^a-zA-Z0-9.]+",' ',k1))
            Outputfile1.write('\t')
        
        Outputfile1.write('\n')
        Outputfile.close()
        Outputfile1.close()
    return k # Then we will print the text in the image
   
