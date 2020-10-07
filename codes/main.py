# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:10:45 2020

@author: rmbp
"""


from Regress import *
from Resampling import *
from list_of_func import *
from results import *


import pandas as pd
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, KFold, cross_validate, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge
import pandas as pd
import matplotlib.colors as colors
from imageio import imread
import random

import subprocess
from resizeimage import resizeimage
from PIL import Image
import skimage.measure
from skimage.io import imsave


def main():
    """
    Sample run for Franke function
    
    
    N.B, to change resampling method: 
    """
    np.random.seed(100)
    n = 20


    # Setting in number og data points
    x,y = generate_mesh(n) 
    z = FrankeWithNoise(x,y,n,sigma=0.1)
    z_flat = np.ravel(z)
    X = create_X(x, y, 5)
    
    
    
    #complexity(x, y, z_flat, 'OLS', min_deg=1, max_deg = 10, alpha = 10**-5)
    #confidence_intervals(X,z_flat)
    #learning_curve('OLS',X,z_flat)
    #generate_heatmaps(x, y, z_flat, "Ridge")



    """Terrain data"""
    m = 5 # number of poly_degree
    z, dimmer = terrain_reader("Hokkaido.tif")
    x,y = generate_mesh(dimmer)
    X_terrain = create_X(x, y, m)
    
    #complexity(x, y, z, "OLS",alpha=10**-5,min_deg=1,max_deg=5)
    #confidence_intervals(X_terrain,z)
    #generate_heatmaps(x, y, z, "Ridge",min_deg=20,max_deg=50)
    #learning_curve('Ridge',X_terrain,z)
    #alpha_tests(x,y,z,"Ridge")
    
    """Predicting terrain"""
    #terrainplotter("Hokkaido.tif")
    #predicted_terrain(x, y, z, "OLS", 100)
    
    
    """Original terrain, 2d"""
    #terrain = imread('Hokkaido.tif')/1000
    #plt.figure()
    #plt.colorbar(terrain)
    #plt.title("Terrain over Western Hokkaido, Japan")
    #plt.imshow(terrain)
    #plt.xlabel("X"); plt.ylabel("Y")
    #plt.show()
    

if __name__ == '__main__':
    main()