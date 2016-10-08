import fnmatch
import os
import numpy as np
from PIL import Image

def find_files(directory, pattern='*.jpg'):
    '''Recursively finds all files matching the pattern.'''
    files = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, pattern):
            files.append(os.path.join(root, filename))
    return files

def _read_image(filename):
  return Image.open(filename).convert('L')

def load_generic_text(directory):
    '''Generator that yields image raw from the directory.'''
    files = find_files(directory)
    for filename in files:
        pic = _read_image(filename)
        pic = pic.resize((128,128), Image.ANTIALIAS)
        img = np.array(pic)
        print (img)
        img = img.reshape(-1, 1)
        print (img)
        img = img.reshape(128, 128)
        print(img)
        new_img = Image.fromarray(img)
        new_img.save('output_file.jpg')
        
        yield img, filename
        
def main():
    iterator = load_generic_text("./data")
    for text, filename in iterator:
        print ("Filename", filename)

if __name__ == '__main__':
    main()