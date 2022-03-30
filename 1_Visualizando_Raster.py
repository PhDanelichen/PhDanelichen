# -*- coding: utf-8 -*-
"""
Victor Danelichen
Visualizando imagens de satélites com Python
Precisa antes instalar os pacotes de geoprocessamento
"""


import rasterio
from rasterio.plot import show
from matplotlib import pyplot as plt

# Mostrando imagens dentro da pasta

img = rasterio.open('D:/Correia/USGS/Landsat_9/220122/LC09_L2SP_226071_20220122_20220124_02_T1_SR_B3.tif') #caminho da pasta com as iamgens
show(img)

# mostra a quantidades de bandas, linhas e colunas na imagem
full_img = img.read()

#Ver quantidades de bandas na imagem
num_bands = img.count
print("Numero de bandas na imagem = ", num_bands)

# Mostrando o sistema de coordenadas
print("Sistema de coordenadas", img.crs)

# Ler os metadados da imagem
metadata = img.meta
print('Metadados: {metadata}\n'.format(metadata = metadata))

# ler as descrições da imagem
desc = img.descriptions
print("Descrição do raster: {desc}\n".format(desc=desc))

# Encontrar greo transformação
print("Geotransformação: ", img.transform)

# Plotando histograma dos valores de cada banda
rasterio.plot.show_hist(full_img)

