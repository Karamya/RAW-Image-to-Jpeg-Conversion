# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:25:08 2016

@author: karthick
"""

import numpy as np
import os
import matplotlib.pyplot as plt
import rawpy
import imageio
###############################################################################

###############################################################################



def convert_raw(foldername):
    """
    READ *.cr2 file into dictionary of arrays
    """
    #os.chdir('U:/p08/2016/data/11001203/raw/'+foldertoread)
    os.chdir('H:/'+foldername)
        
    for file in os.listdir():
        #print(type(file))
        cr2_image = rawpy.imread(file)
        rgb = cr2_image.postprocess()
        filename = file[0:-4]
        imageio.imsave('H:/Raja mama JPEG/'+filename+'.jpeg', rgb)
        #print(file)        
    return

###############################################################################


###############################################################################

os.chdir('H:/')
foldername = 'temp'
###############################################################################
#### Plotting 1D data
###############################################################################
   
convert_raw(foldername)
    
###############################################################################

###############################################################################
