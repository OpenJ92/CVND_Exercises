import os
import glob 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2

class Load(object):
    def __init__(self, path="", im_type="", co=False):
        self.path = path
        self.im_type = im_type
        self.data = None if co else self.load_dataset()

    def __add__(self, other):
        if isinstance(other, type(self)):
            l = Load([self.path, other.path], [self.im_type, other.im_type], co=True)
            l.data = self.data + other.data
            return l

    def __getitem__(self, ix):
        if hasattr(self, 'data'):
            return self.data[ix]
        else:
            return (None, None, None)

    def __len__(self):
        if hasattr(self, 'data'):
            return len(self.data)
        else:
            return None
    
    def load_dataset(self):
        im_list = []
        image_types = ["day", "night"]
        for im_type in image_types:
            for file in glob.glob(os.path.join(self.path, self.im_type, "*")):
                im = mpimg.imread(file)
                if not im is None:
                    im_list.append((im, self.im_type, file))
        return im_list

    def show_image(self, ix):
        # should this be in here or in another class for display?
        # place this into the display class
        img, im_type, file = self[ix]
        plt.imshow(img)
        plt.show()

if __name__ == "__main__":
    l_train_N = Load("day_night_images/training/", "night")
    l_train_D = Load("day_night_images/training/", "day")
    e = l_train_D + l_train_N 

