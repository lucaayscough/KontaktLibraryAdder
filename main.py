import os

lib_dir = "/Volumes/Extreme SSD/Librerie/"

for dir in os.listdir(lib_dir):
    if os.path.isdir(lib_dir + "/" + dir) and dir[0] != ".":
        lib_files = os.listdir(lib_dir + "/" + dir)
        for lib_file in lib_files:
            if lib_file.find(".nicnt") != -1:
                filename = lib_dir + "/" + lib_file
                library_name = filename[filename.rfind("/") + 1 : filename.find(".")]

                contents = open(filename, "r", encoding="iso-8859-1").read()
                contents = contents[contents.find("<?xml") : contents.find("</ProductHints>") + len("</ProductHints>")]

                xml = open("/Library/Application Support/Native Instruments/Service Center/" + library_name + ".xml", "w")
                xml.write(contents)