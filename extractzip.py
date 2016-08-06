#unzip a file
import os, zipfile, glob

zip =  open("C:/Users/sande/Downloads", 'r')
zip1 = zipfile.ZipFile(zip)
os.chdir("C:/Users/sande/Downloads/wellsFargo.zip")
filenames = glob.glob('*.*')

for x in filename :
	zip1.extract(x, "C:/Users/sande/Desktop/python")