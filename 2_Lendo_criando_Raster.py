# -*- coding: utf-8 -*-
"""
Victor Danelichen
Visualizando imagens de satélites com Python
Precisa antes instalar os pacotes de geoprocessamento
"""



import matplotlib.pyplot as plt

# Mostrando imagens dentro da pasta
import os
os.listdir('D:/Correia/USGS/Landsat_9/220122/')

#Lendo imagem raster
from osgeo import gdal

ndvi = gdal.Open("D:/Correia/USGS/Landsat_9/220122/ndviImage.tif") #lendo imagem
gt = ndvi.GetGeoTransform() # informações do raster dos cantos e tamanho do pixel
proj = ndvi.GetProjection() #mostra a projeção
banda = ndvi.GetRasterBand(1) # mostra a info da banda
array = banda.ReadAsArray() #transformando para array "matriz" para operações algebricas

#Plotando raster
plt.figure()
plt.imshow(array)

#filtrando
import numpy as np
binmask = np.where((array >= np.mean(array)), 1, 0)
plt.figure()
plt.imshow(binmask)

#salvando raster filtrado em formato tif
driver = gdal.GetDriverByName("GTiff")
#se digitar binmask.shape no console mostra o numero de linhas e colunas do raster
driver.Register()
outndvi = driver.Create("D:/Correia/USGS/Landsat_9/220122/binmask.tif", xsize =
                        binmask.shape[1], ysize = binmask.shape[0], bands = 1,
                        eType = gdal.GDT_Int32)

outndvi.SetGeoTransform(gt)
outndvi.SetProjection(proj)
outband = outndvi.GetRasterBand(1)
outband.WriteArray(binmask)
outband.SetNoDataValue(np.nan)
outband.FlushCache()

#fechando nosso datasets e bandas
outband = None
outndvi = None


