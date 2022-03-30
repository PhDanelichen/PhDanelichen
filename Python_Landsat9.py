# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:11:21 2022

@author: VictorHugo

Calculando NDVI com landsat 9
"""
import os
import rasterio
from rasterio.plot import show
from matplotlib import pyplot as plt

# Mostrando imagens dentro da pasta
items = os.listdir('D:/Correia/USGS/Landsat_9/220122/')
print(items)

#definindo as bandas
band_3 = rasterio.open('D:/Correia/USGS/Landsat_9/220122/LC09_L2SP_226071_20220122_20220124_02_T1_SR_B3.tif') #caminho da pasta com as iamgens
band_4 = rasterio.open('D:/Correia/USGS/Landsat_9/220122/LC09_L2SP_226071_20220122_20220124_02_T1_SR_B4.tif')
band_5 = rasterio.open('D:/Correia/USGS/Landsat_9/220122/LC09_L2SP_226071_20220122_20220124_02_T1_SR_B5.tif')

# Plotar as bandas
show(band_4)
show(band_5)

################# NDVI - normalized difference vegetation index ############
# NDVI = (NIR-Red)/(NIR+Red)

# Abaixo um ex de uma imagem do google das bandas do L9 para ver 
# para o Landsat 9 NIR = band_5 e Red = band_4
import IPython
url = 'https://blogpnt.files.wordpress.com/2021/09/landsat9_bandas-2.png'
IPython.display.Image(url, width = 550)

#calculo do NDVI para o Landsat 9 convertendo para float

#generate nir and red objects as arrays in float64 format
red = band_4.read(1).astype('float64')
nir = band_5.read(1).astype('float64')

import numpy as np

#ndvi calculation, empty cells or nodata cells are reported as 0
ndvi = np.where((nir+red)==0., 0, (nir-red)/(nir+red))
ndvi[:5,:5]

#export ndvi image
ndviImage = rasterio.open('D:/Correia/USGS/Landsat_9/220122/ndviImage.tiff','w',driver='Gtiff',
                          width=band_4.width, 
                          height = band_4.height, 
                          count=1, crs=band_4.crs, 
                          transform=band_4.transform, 
                          dtype='float64')
ndviImage.write(ndvi,1)
ndviImage.close()

#plot ndvi
ndvi = rasterio.open('D:/Correia/USGS/Landsat_9/220122/ndviImage.tiff')
fig = plt.figure(figsize=(18,12))
show(ndvi)

# Plotando histograma dos valores de cada banda
rasterio.plot.show_hist(ndvi)
