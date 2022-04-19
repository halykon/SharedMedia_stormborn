import os

folder = r'./'
for file in os.listdir(folder):
    filename, ext = os.path.splitext(folder + file)
    if(ext == ".ogg"):
        source = folder + file
        dest = folder + "Stormborm - " + file
        os.rename(source, dest)

