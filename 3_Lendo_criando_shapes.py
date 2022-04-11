# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 11:19:51 2022
TRABALHANDO COM VETORES, SHAPES
@author: VictorHugo
"""

#LISTANDO ARQUIVOS na pasta onde esta a shape
import os
os.listdir('D:/Correia/USGS/CursoGIS/Cuiaba_shapes')


from osgeo import ogr

shape = ogr.Open("D:/Correia/USGS/CursoGIS/Cuiaba_shapes/Cuiaba.shp", 0)
layer = shape.GetLayer()
ext = layer.GetExtent()

feature = layer.GetFeature(0)

for feature in layer:
    print(feature.GetField("FID"))
