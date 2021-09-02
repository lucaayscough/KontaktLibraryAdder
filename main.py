import os
from tkinter import filedialog as fd


filename = fd.askopenfilename()
library_name = filename[filename.rfind("/") + 1 : filename.find(".")]

contents = open(filename, "r", encoding="iso-8859-1").read()
contents = contents[contents.find("<?xml") : contents.find("</ProductHints>") + len("</ProductHints>")]

xml = open("/Library/Application Support/Native Instruments/Service Center/" + library_name + ".xml", "w")
xml.write(contents)