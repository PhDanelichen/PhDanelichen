# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:09:00 2022

@author: VictorHugo
"""

import matplotlib.pyplot as plt
import geopandas as gpd
import rasterio
from rasterio.plot import show

#abrindo a shape
pontos_dados = gpd.read_file(r'D:\Correia\USGS\Landsat_9\220122\Shape_pontos\pivo_pontos.shp')
print(pontos_dados)
pontos_dados.plot()

#abrindo arquivo raster
ndvi_Raster = rasterio.open(r'C:\Victor_TESE_Correia\Imagens\Produtos_espa\2017\28082017\LC08_L1TP_226071_20170828_20170914_01_T1_sr_ndvi.tif')
print(ndvi_Raster.crs)
print(ndvi_Raster.count)

#mostra os pontos e o raster no matplotlib plot
fig, ax = plt.subplots(figsize=(12,12))
pontos_dados.plot(ax=ax, color='orangered')
show(ndvi_Raster, ax=ax)

#extrair xy dos point geometry "mostrar pontos" das coordenadas
for ponto in pontos_dados['geometry']:
    print(ponto.xy[0][0], ponto.xy[1][0])

#extrair valores dos pontos do raster "nvdi"

for ponto in pontos_dados['geometry']:
    x = ponto.xy[0][0]
    y = ponto.xy[1][0]
    row, col = ndvi_Raster.index(x, y)
    print("Ponto correspondente para linha, coluna: %d, %d"% (row, col))
    print("Ponto correspondente para coordendas: %d, %d"%(x,y))
    print("Valor do raster no ponto %.2f \n"%ndvi_Raster.read(1)[row,col])
    

#o programa esta feito, mas vamos gravar a tabela EM CONSTRUÇÃO
import pandas as pd

for ponto in pontos_dados['geometry']:
    x = ponto.xy[0][0]
    y = ponto.xy[1][0]
    row, col = ndvi_Raster.index(x, y)
    
  
    tabela = {'x':[x], 'y':[y], 'valor_raster':[ndvi_Raster.read(1)[row,col]]}

    df = pd.DataFrame(tabela)
    #df.to_excel('tabela_valores_pixels.xls') #arquivo vai para pasta do usuário C:\Users\VictorHugo
    #print(tabela)
    print(df)
    #print("Ponto correspondente para linha, coluna: %d, %d"% (row, col))
    #print("Ponto correspondente para coordendas: %d, %d"%(x,y))
    #print("Valor do raster no ponto %.2f "%ndvi_Raster.read(1)[row,col])
    #print("\n")
