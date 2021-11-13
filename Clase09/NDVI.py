#%%
# El ejercicio no esta finalizado, llegue hasta un cierto punto por cuestión de tiempo
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import axes_grid1

def add_color_bar(im, aspect=20, pad_fraction=0.5, **kwargs):
    divider = axes_grid1.make_axes_locatable(im.axes)
    width = axes_grid1.axes_size.AxesY(im.axes, aspect=1./aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    current_ax = plt.gca()
    cax = divider.append_axes("right", size=width, pad=pad)
    plt.sca(current_ax)
    return im.axes.figure.colorbar(im, cax=cax, **kwargs)

bNIR = np.load('../Data/clip/LC08_L1TP_225084_20180213_20180222_01_T1_sr_band5_clip.npy')
bR = np.load('../Data/clip/LC08_L1TP_225084_20180213_20180222_01_T1_sr_band4_clip.npy')
bG = np.load('../Data/clip/LC08_L1TP_225084_20180213_20180222_01_T1_sr_band3_clip.npy')
bB = np.load('../Data/clip/LC08_L1TP_225084_20180213_20180222_01_T1_sr_band2_clip.npy')

# Azul
plt.figure(figsize=(7, 7), dpi=150)
im = plt.imshow(bR)
add_color_bar(im)

h = plt.hist(bR.flatten(),bins=250)

j = plt.hist(bR.flatten(),bins=250, range=(0, 2))

# Rojo
plt.figure(figsize=(7, 7), dpi=150)
im = plt.imshow(bR, vmin=0.3, vmax=2)
add_color_bar(im)

# Infrarojo
plt.figure(figsize=(7, 7), dpi=150)
im = plt.imshow(bNIR, vmin=1, vmax=5)
add_color_bar(im)
# %%
