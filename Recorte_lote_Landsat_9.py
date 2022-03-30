# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:40:43 2022
RECORTE EM LOTE DE IMAGENS DO LANDSAT 9
@author: VictorHugo
"""
import os
from osgeo import gdal
import geopandas as gpd

#chacando arquivos na pasta das imagens
os.listdir('D:/Correia/USGS/Landsat_9/220122')

# dados de entrada e saida ATENÇÃO CRIAR UMA PASTA DE ENTRADA DAS IMAGENS E SAIDA
#aqui dei o nome da entrada de "Entrada_imagens" e saida "Recortada!
inputPath = 'D:/Correia/USGS/Landsat_9/220122/Entrada_imagens/'
outputPath = 'D:/Correia/USGS/Landsat_9/220122/Recortada/'

#listar imagens TIF
bandList = [band for band in os.listdir(inputPath) if band[-4:]== '.TIF']
bandList

#vizualizando a shape
shape_cuiaba = gpd.read_file('D:/Correia/USGS/CursoGIS/Cuiaba_shapes/Cuiaba.shp')
shape_cuiaba.plot()

# SHAPE para recorte

shap_clip = 'D:/Correia/USGS/CursoGIS/Cuiaba_shapes/Cuiaba.shp'


# recortando com Warp
for band in bandList:
    print(outputPath + band[:-4] +'_recor'+band[-4:])
    options = gdal.WarpOptions(cutlineDSName=shap_clip,cropToCutline=True)
    outBand = gdal.Warp(srcDSOrSrcDSTab= inputPath + band,
                        destNameOrDestDS= outputPath + band[:-4]+'_recor'+band[-4:],
                        options=options)
    outBand = None

#checando
import rasterio

banda_1 = rasterio.open('D:/Correia/USGS/Landsat_9/220122/Recortada/LC09_L2SP_226071_20220122_20220124_02_T1_ST_B10_recor.TIF') 
plot.show(banda_1)
