import numpy as np
import matplotlib.pyplot as plt

def show_correct(img):
    img = np.array(img)
    img = np.array([np.pad(img[:,:,0], (3,3), 'constant', constant_values=(200,200)),np.pad(img[:,:,1], (3,3), 'constant',constant_values=(0,0)),np.pad(img[:,:,2], (3,3), 'constant',constant_values=(0,0))])
    plt.imshow(img.transpose(1,2,0))