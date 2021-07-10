import os
import shutil

validExtensions = ['.jpg','.jpeg','.png','.gif','.webp','.tiff','.psd','.raw','.bmp','.heif','.indd','.svg','.ai','.eps','.pdf']

def checkValidPath(path):
    while not (os.path.exists(path) and os.path.isdir(path)):
        print("Error: Please specifiy a valid directory path.")
        path = input()
    return path

def checkValidFolder(name,path):
    while (not name.isprintable()) or os.path.exists(os.path.join(path,name)):
        print("Error: Please enter a valid directory name.")
        name = input()
    return name

def extractAllImages(directory,output):
    for child in os.listdir(directory):
        childPath = os.path.join(directory,child)
        for extension in validExtensions:
            if child.endswith(extension):
                print("Found valid file with " + extension)
                shutil.copy(childPath,output)
                break
        if os.path.isdir(childPath):
            if len(os.listdir(childPath)) > 0:
                extractAllImages(childPath,output)