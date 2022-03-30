#!/usr/bin/env python
# coding: utf-8

# # Sentinel 2 in Python
# ### PhD. Victor Danelichen

# In[1]:


import IPython
url_2 = 'http://www.engesat.com.br/wp-content/uploads/Sentinel2-450x343.jpeg'
IPython.display.Image(url_2, width = 550)


# In[2]:


import rasterio
from rasterio import plot
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplot', 'i')


# In[ ]:


# Abaixo um ex de uma imagem do google das bandas do sentinel 2 para ver 
import IPython
url = 'http://www.engesat.com.br/wp-content/uploads/Bandas-espectrais.png'
IPython.display.Image(url, width = 550)


# In[ ]:





# In[3]:


imagePath = 'D:/Correia/USGS/sentinel/2022/020522_DOIS_TALHOES/S2B_MSIL1C_20220205T140049_N0400_R067_T21LXC_20220205T154948.SAFE/GRANULE/L1C_T21LXC_A025690_20220205T140046/IMG_DATA/'
band_2 = rasterio.open(imagePath+'T21LXC_20220205T140049_B02.jp2', driver='JP2OpenJPEG') #blue
band_3 = rasterio.open(imagePath+'T21LXC_20220205T140049_B03.jp2', driver='JP2OpenJPEG') #green
band_4 = rasterio.open(imagePath+'T21LXC_20220205T140049_B04.jp2', driver='JP2OpenJPEG') #red
band_8 = rasterio.open(imagePath+'T21LXC_20220205T140049_B08.jp2', driver='JP2OpenJPEG') #nir


# In[ ]:


band_4.count


# In[ ]:


band_4.width


# In[ ]:


band_4.height


# In[ ]:


plot.show(band_4)


# In[ ]:


band_4.crs


# In[4]:


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))
plot.show(band_2, ax=ax1, cmap='Blues')
plot.show(band_3, ax=ax2, cmap='Greens')
plot.show(band_4, ax=ax3, cmap='Reds')
fig.tight_layout()


# In[25]:


# compor cor verdadeira
trueColor = rasterio.open('D:/Correia/USGS/sentinel/2022/020522_DOIS_TALHOES/S2B_MSIL1C_20220205T140049_N0400_R067_T21LXC_20220205T154948.SAFE/GRANULE/L1C_T21LXC_A025690_20220205T140046/IMG_DATA/SentinelTrueColor2.tiff','w',driver='Gtiff',
                         width=band_4.width, height=band_4.height,
                         count=3,
                         crs=band_4.crs,
                         transform=band_4.transform,
                         dtype=band_4.dtypes[0]
                         )
trueColor.write(band_2.read(1),3) #blue
trueColor.write(band_3.read(1),2) #green
trueColor.write(band_4.read(1),1) #red
trueColor.close()
src = rasterio.open(r"../Output/SentinelTrueColor2.tiff", count=3)
plot.show(src)


# In[27]:


trueColor = rasterio.open('D:/Correia/USGS/sentinel/2022/020522_DOIS_TALHOES/S2B_MSIL1C_20220205T140049_N0400_R067_T21LXC_20220205T154948.SAFE/GRANULE/L1C_T21LXC_A025690_20220205T140046/IMG_DATA/SentinelTrueColor2.tiff/')
plot.show(trueColor)


# In[9]:


# Falsa cor
falseColor = rasterio.open('D:/Correia/USGS/sentinel/2022/020522_DOIS_TALHOES/S2B_MSIL1C_20220205T140049_N0400_R067_T21LXC_20220205T154948.SAFE/GRANULE/L1C_T21LXC_A025690_20220205T140046/IMG_DATA/SentinelFalseColor.tiff','w',driver='Gtiff',
                         width=band_4.width, height=band_4.height,
                         count=3,
                         crs=band_4.crs,
                         transform=band_4.transform,
                         dtype=band_4.dtypes[0]
                         )
falseColor.write(band_3.read(1),3) #Blue
falseColor.write(band_4.read(1),2) #Green
falseColor.write(band_8.read(1),1) #Red

falseColor.close()


# In[23]:


falseColor = rasterio.open('D:/Correia/USGS/sentinel/2022/020522_DOIS_TALHOES/S2B_MSIL1C_20220205T140049_N0400_R067_T21LXC_20220205T154948.SAFE/GRANULE/L1C_T21LXC_A025690_20220205T140046/IMG_DATA/SentinelFalseColor.tiff/')
plot.show(falseColor)


# In[31]:


# gerar histograma
trueColor = rasterio.open(r'D:\Correia\USGS\sentinel\2022\020522_DOIS_TALHOES\S2B_MSIL1C_20220205T140049_N0400_R067_T21LXC_20220205T154948.SAFE\GRANULE\L1C_T21LXC_A025690_20220205T140046\IMG_DATA\SentinelTrueColor2.tiff')
plot.show_hist(trueColor, bins = 50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram")

