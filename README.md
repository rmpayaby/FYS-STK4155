# FYS-STK4155

The codes-folder contains the code implemented for project 1. The plots produced from the sample run folder comes from main.py in the codes-folder. For the case of simplicity, I've only included the MSE analyses for OLS Franke funtion using bootstrap. The complexity function ran in main.py should also produce the mse and r2-score for the optimal polynomial degree. In the sample run, those values were:

min mse: 0.005057859199036065, 
r2: 0.9268786637993607, 
deg: 5.0

N.B the heatmap/grid search were produced in the Python library Altair, thus it will not work if that package is not installed.

In order to change the resampling technique, go to result.py, and change line 71. Replace bootstrap with one of the following methods: "train_test" (prior to resampling of data), "kfold_cross_val" (own code), "sklearns_kfold". 

The terrain data can be found on the terrain_data folder.


